# Queue

Displays the agent's todo list, split into what is left and what is done.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import CircleIcon from "@lucide/svelte/icons/circle";
  import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
  import CircleDotIcon from "@lucide/svelte/icons/circle-dot";
  import ListChecksIcon from "@lucide/svelte/icons/list-checks";
  import ListTodoIcon from "@lucide/svelte/icons/list-todo";
  import { Chat } from "@ai-sdk/svelte";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import type { UIDataTypes, UIMessage } from "ai";
  type ChatMessage = UIMessage<
    unknown,
    UIDataTypes,
    {
      writeTodos: {
        input: {
          todos: {
            content: string;
            status: "pending" | "in_progress" | "completed";
          }[];
        };
        output: string;
      };
    }
  >;
  type Todo = Extract<
    ChatMessage["parts"][number],
    { type: "tool-writeTodos"; state: "input-available" }
  >["input"]["todos"][number];
  const TODOS = [
    "Add a dark variant to the theme tokens",
    "Read the theme from a cookie",
    "Add a toggle to the settings page",
    "Check contrast on the charts"
 ];
  function todosAt(current: number) {
    return TODOS.map(
      (content, index) =>
        ({
          content,
          status:
            index < current
              ? "completed"
              : index === current
                ? "in_progress"
                : "pending"
        }) satisfies Todo
    );
  }
  const script = createChat<ChatMessage>()
    .user("Add dark mode to the settings page.")
    .assistant(({ writer }) => {
      TODOS.forEach((_, index) => {
        writer
          .tool("writeTodos", { input: { todos: todosAt(index) } })
          .output("Updated the todo list.");
        writer.sleep(1400);
      });
      writer
        .tool("writeTodos", { input: { todos: todosAt(TODOS.length) } })
        .output("Updated the todo list.");
      writer.text("Dark mode is in. The toggle is under Settings, Appearance.");
    });
  const transcript = script.get();
  const [question] = script.get(1);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat<ChatMessage>({ messages: transcript, transport });
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
</script>
{#snippet todoLine(todo: Todo, streaming: boolean)}
  <Trace.Line
    status={streaming && todo.status === "in_progress" ? "running" : undefined}
  >
    <Trace.Icon>
      {#if todo.status === "completed"}
        <CircleCheckIcon />
      {:else if todo.status === "in_progress"}
        <CircleDotIcon />
      {:else}
        <CircleIcon />
      {/if}
    </Trace.Icon>
    <Trace.Title>{todo.content}</Trace.Title>
  </Trace.Line>
{/snippet}
{#snippet todoQueue(todos: Todo[], streaming: boolean)}
  {@const pending = todos.filter((todo) => todo.status !== "completed")}
  {@const completed = todos.filter((todo) => todo.status === "completed")}
  <Trace.Root>
    {#if pending.length > 0}
      <Trace.Collapsible open>
        <Trace.CollapsibleTrigger>
          <Trace.Line>
            <Trace.Icon>
              <ListTodoIcon />
            </Trace.Icon>
            <Trace.Title>{pending.length} to do</Trace.Title>
          </Trace.Line>
        </Trace.CollapsibleTrigger>
        <Trace.CollapsibleContent>
          <Trace.Root>
            {#each pending as todo, index (index)}
              {@render todoLine(todo, streaming)}
            {/each}
          </Trace.Root>
        </Trace.CollapsibleContent>
      </Trace.Collapsible>
    {/if}
    {#if completed.length > 0}
      <Trace.Collapsible open>
        <Trace.CollapsibleTrigger>
          <Trace.Line>
            <Trace.Icon>
              <ListChecksIcon />
            </Trace.Icon>
            <Trace.Title>{completed.length} completed</Trace.Title>
          </Trace.Line>
        </Trace.CollapsibleTrigger>
        <Trace.CollapsibleContent>
          <Trace.Root>
            {#each completed as todo, index (index)}
              {@render todoLine(todo, streaming)}
            {/each}
          </Trace.Root>
        </Trace.CollapsibleContent>
      </Trace.Collapsible>
    {/if}
  </Trace.Root>
{/snippet}
<div class="flex min-h-72 w-full max-w-sm flex-col gap-4 py-6 text-sm">
  {#each chat.messages as message (message.id)}
    {#if message.role === "user"}
      <Message.Root align="end">
        <Message.Content>
          <Bubble.Root align="end" variant="muted">
            <Bubble.Content>{getMessageText(message)}</Bubble.Content>
          </Bubble.Root>
        </Message.Content>
      </Message.Root>
    {:else}
      {@const streaming = busy && message === chat.messages.at(-1)}
      {@const todos = message.parts
        .filter((part) => part.type === "tool-writeTodos")
        .filter((part) => part.state !== "input-streaming")
        .at(-1)?.input?.todos}
      {@const text = getMessageText(message)}
      <Message.Root>
        <Message.Content class="gap-4">
          {#if todos}
            {@render todoQueue(todos, streaming)}
          {/if}
          {#if text}
            <p>{text}</p>
          {/if}
        </Message.Content>
      </Message.Root>
    {/if}
  {/each}
  {#if !busy}
    <Button
      variant="outline"
      size="sm"
      class="mt-auto self-start"
      onclick={() => {
        chat.messages = [];
        void chat.sendMessage(question);
      }}
    >
      Replay
    </Button>
  {/if}
</div>
```

View Code

Queue is the agent's todo list. Todos sit in two sections, To do and Completed, and the icon on each todo shows its status. The agent updates the list as it works, so a todo moves from one section to the other when it is done.

Queue is built with `Trace` with a `Trace.Collapsible` for each section.

## [Installation](#installation)

Queue is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) component.

```bash
pnpm dlx shadcn-svelte@latest add trace
```

```bash
npx shadcn-svelte@latest add trace
```

```bash
bun x shadcn-svelte@latest add trace
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Trace from "$lib/components/ui/trace/index.js";
</script>
```

```svelte
<Trace.Root>
  <Trace.Collapsible open>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <ListTodoIcon />
        </Trace.Icon>
        <Trace.Title>2 to do</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        <Trace.Line>
          <Trace.Icon>
            <CircleIcon />
          </Trace.Icon>
          <Trace.Title>Update the registry snapshots</Trace.Title>
        </Trace.Line>
        <Trace.Line>
          <Trace.Icon>
            <CircleIcon />
          </Trace.Icon>
          <Trace.Title>Add tests for the combobox</Trace.Title>
        </Trace.Line>
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <ListChecksIcon />
        </Trace.Icon>
        <Trace.Title>1 completed</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        <Trace.Line>
          <Trace.Icon>
            <CircleCheckIcon />
          </Trace.Icon>
          <Trace.Title>Add a changeset</Trace.Title>
        </Trace.Line>
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [Descriptions](#descriptions)

A todo with a description is a `Trace.Collapsible` that opens to show it. A todo without one stays a `Trace.Line`.

```svelte
<script lang="ts">
  import CircleIcon from "@lucide/svelte/icons/circle";
  import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
  import ListChecksIcon from "@lucide/svelte/icons/list-checks";
  import ListTodoIcon from "@lucide/svelte/icons/list-todo";
  import * as Trace from "$lib/components/ui/trace/index.js";
  type Todo = { title: string; description?: string; done: boolean };
  const todos: Todo[] = [
    {
      title: "Write the migration guide",
      description: "Cover the renamed props and the new data attributes.",
      done: true
    },
    { title: "Add a changeset", done: true },
    {
      title: "Fix the focus ring on the select trigger",
      description: "It is clipped by overflow-hidden on the field.",
      done: false
    },
    { title: "Update the registry snapshots", done: false },
    {
      title: "Add tests for the combobox",
      description: "Typing, clearing and keyboard selection.",
      done: false
    }
 ];
  const pending = todos.filter((todo) => !todo.done);
  const completed = todos.filter((todo) => todo.done);
</script>
{#snippet todoRow(todo: Todo)}
  {#snippet line()}
    <Trace.Line>
      <Trace.Icon>
        {#if todo.done}
          <CircleCheckIcon />
        {:else}
          <CircleIcon />
        {/if}
      </Trace.Icon>
      <Trace.Title>{todo.title}</Trace.Title>
    </Trace.Line>
  {/snippet}
  {#if !todo.description}
    {@render line()}
  {:else}
    <Trace.Collapsible>
      <Trace.CollapsibleTrigger>{@render line()}</Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent>{todo.description}</Trace.CollapsibleContent>
    </Trace.Collapsible>
  {/if}
{/snippet}
<Trace.Root class="max-w-sm">
  <Trace.Collapsible open>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <ListTodoIcon />
        </Trace.Icon>
        <Trace.Title>{pending.length} to do</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        {#each pending as todo, index (index)}
          {@render todoRow(todo)}
        {/each}
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <ListChecksIcon />
        </Trace.Icon>
        <Trace.Title>{completed.length} completed</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        {#each completed as todo, index (index)}
          {@render todoRow(todo)}
        {/each}
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

View Code

```svelte
<Trace.Collapsible>
  <Trace.CollapsibleTrigger>
    <Trace.Line>
      <Trace.Icon>
        <CircleIcon />
      </Trace.Icon>
      <Trace.Title>Fix the focus ring on the select trigger</Trace.Title>
    </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
    It is clipped by overflow-hidden on the field.
  </Trace.CollapsibleContent>
</Trace.Collapsible>
```

## [AI SDK](#ai-sdk)

The agent writes its todos with a tool, `writeTodos` in this example. Each call sends the whole list, so render the last call and skip one whose input is still streaming.

```svelte
{@const todos = message.parts
  .filter((part) => part.type === "tool-writeTodos")
  .filter((part) => part.state !== "input-streaming")
  .at(-1)?.input?.todos}
```

Map each todo status to a section, an icon and a `Trace.Line` status. Set `"running"` on the todo in progress only while the chat streams, so its title stops shimmering when the agent stops.

| Todo status                 | Section   | Icon                     | `Trace.Line` status                |
| ----------------------------------------- | ------------------------------ | --------------------------------------------- | ---------------------------------------------------------------------------- |
| `pending`     | To do     | `CircleIcon`      | none                                      |
| `in_progress` | To do     | `CircleDotIcon`   | `"running"` while the chat streams |
| `completed`   | Completed | `CircleCheckIcon` | none                        |

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).