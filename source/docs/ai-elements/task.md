# Task

Displays the steps the agent takes, as it takes them.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import CircleAlertIcon from "@lucide/svelte/icons/circle-alert";
  import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
  import LoaderCircleIcon from "@lucide/svelte/icons/loader-circle";
  import { Chat } from "@ai-sdk/svelte";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import type { UIMessage } from "ai";
  type ChatMessage = UIMessage<
    unknown,
    {
      task: {
        title: string;
        steps: { title: string; status: "done" | "running" | "error" }[];
      };
    }
  >;
  type TaskPart = Extract<ChatMessage["parts"][number], { type: "data-task" }>;
  type Status = "running" | "error" | undefined;
  const TASKS = [
    {
      id: "find",
      title: ["Finding the project files", "Found the project files"],
      steps: [
        ["Searching for generateMetadata", "Searched for generateMetadata"],
        ["Reading app/layout.tsx", "Read app/layout.tsx"],
        ["Reading app/page.tsx", "Read app/page.tsx"]
      ]
    },
    {
      id: "update",
      title: ["Updating the page metadata", "Updated the page metadata"],
      steps: [
        ["Editing app/layout.tsx", "Edited app/layout.tsx"],
        ["Editing app/page.tsx", "Edited app/page.tsx"]
      ]
    }
  ];
  function taskAt(task: (typeof TASKS)[number], done: number) {
    return {
      title: task.title[done < task.steps.length ? 0 : 1],
      steps: task.steps
        .slice(0, done + 1)
        .map(([running, finished], index) => ({
          title: index < done ? finished : running,
          status: index < done ? "done" : "running"
        }))
    } satisfies TaskPart["data"];
  }
  const script = createChat<ChatMessage>()
    .user("Add Open Graph metadata to the home page.")
    .assistant(({ writer }) => {
      TASKS.forEach((task) => {
        for (let done = 0; done <= task.steps.length; done++) {
          writer
            .data({ type: "data-task", id: task.id, data: taskAt(task, done) })
            .sleep(900);
        }
      });
      writer.text(
        "Added Open Graph defaults to app/layout.tsx and a title, description and image for the home page in app/page.tsx."
      );
    });
  const transcript = script.get();
  const [question] = script.get(1);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat<ChatMessage>({ messages: transcript, transport });
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  // The reader's choice for each task. Until they click, it follows the task's status.
  let taskOpen = $state<Record<string, boolean>>({});
  function getStepStatus(
    status: TaskPart["data"]["steps"][number]["status"],
    streaming: boolean
  ): Status {
    if (status === "done") {
      return undefined;
    }
    return status === "running" && streaming ? "running" : "error";
  }
</script>
{#snippet statusIcon(status: Status)}
  {#if status === "running"}
    <LoaderCircleIcon class="animate-spin" />
  {:else if status === "error"}
    <CircleAlertIcon />
  {:else}
    <CircleCheckIcon />
  {/if}
{/snippet}
{#snippet taskRow(id: string, task: TaskPart["data"], streaming: boolean)}
  {@const steps = task.steps.map((step) => ({
    title: step.title,
    status: getStepStatus(step.status, streaming)
  }))}
  {@const status = steps.some((step) => step.status === "error")
    ? "error"
    : steps.some((step) => step.status === "running")
      ? "running"
      : undefined}
  <Trace.Collapsible
    open={taskOpen[id] ?? status === "running"}
    onOpenChange={(open) => (taskOpen[id] = open)}
  >
    <Trace.CollapsibleTrigger>
      <Trace.Line {status}>
        <Trace.Icon>
          {@render statusIcon(status)}
        </Trace.Icon>
        <Trace.Title>{task.title}</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        {#each steps as step, index (index)}
          <Trace.Line status={step.status}>
            <Trace.Title>{step.title}</Trace.Title>
          </Trace.Line>
        {/each}
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
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
      {@const tasks = message.parts.filter((part) => part.type === "data-task")}
      {@const text = getMessageText(message)}
      <Message.Root>
        <Message.Content class="gap-4">
          {#if tasks.length > 0}
            <Trace.Root>
              {#each tasks as part (part.id)}
                {@render taskRow( `${message.id}-${part.id}`,
                  part.data,
                  streaming
                )}
              {/each}
            </Trace.Root>
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
        taskOpen = {};
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

Task is a piece of work the agent is doing, such as finding the project files or updating a page. Each step, like a search, a read or an edit, appears under the task when the agent takes it.

Task is built with `Trace` with a `Trace.Collapsible` for each task.

## [Task or Plan](#task-or-plan)

Both are a list of steps under a collapsible line. The difference is when the steps are known.

Use [Plan](https://shadcn-svelte.com/docs/ai-elements/plan) when the agent decides the steps before it starts. Use Task when the steps come from the work itself, and the agent only knows the next one once it has taken the last.

|                             | Plan                                   | Task                                                          |
| ---------------------------------- | ----------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| Steps         | Every step, from the start             | Each step, once the agent takes it                            |
| Pending steps | Yes, waiting their turn                | None                                                          |
| Title         | The goal, with progress: "2 of 4 done" | What the agent is doing, then what it did                     |
| Per reply     | One plan                               | One or more tasks, each closing when it is done |

## [Installation](#installation)

Task is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) component.

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
        <Trace.Title>Found the project files</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        <Trace.Line>
          <Trace.Icon>
            <SearchIcon />
          </Trace.Icon>
          <Trace.Title>Searched for app/page.tsx</Trace.Title>
        </Trace.Line>
        <a href="/files/app/page.tsx">
          <Trace.Line>
            <Trace.Icon>
              <FileTextIcon />
            </Trace.Icon>
            <Trace.Title>Read app/page.tsx</Trace.Title>
          </Trace.Line>
        </a>
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [Status](#status)

Set the task's status from its steps. Write the title in the present tense while the task runs, and in the past tense once it is done.

| Steps                          | `status`    | Title                                   |
| -------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------- |
| A step is still running | `"running"` | Updating the page metadata              |
| A step failed           | `"error"`   | Failed to update the page metadata      |
| Every step is done      | none               | Updated the page metadata |

Put several tasks in one `Trace`. Keep the running task open, and close each task once it is done.

## [AI SDK](#ai-sdk)

Stream each task as a data part with its own `id`. The AI SDK replaces a data part with the same `id`, so writing a task again with a new step updates it in place.

src/routes/api/chat/+server.ts

```ts
const stream = createUIMessageStream({
  execute: async ({ writer }) => {
    writer.write({ type: "data-task", id: "update", data: { title, steps } });
  },
});
```

```svelte
{@const tasks = message.parts.filter((part) => part.type === "data-task")}
```

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).