# Tool

Displays a tool call the agent makes, from input to output.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import TerminalIcon from "@lucide/svelte/icons/terminal";
  import { Chat } from "@ai-sdk/svelte";
  import { untrack } from "svelte";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import type { UIDataTypes, UIMessage } from "ai";
  type ChatMessage = UIMessage<
    unknown,
    UIDataTypes,
    {
      runCommand: {
        input: { command: string };
        output: { stdout: string };
      };
    }
  >;
  type ToolPart = Extract<
    ChatMessage["parts"][number],
    { type: "tool-runCommand" }
  >;
  const script = createChat<ChatMessage>()
    .user("Which package managers are installed?")
    .assistant(({ writer }) => {
      writer
        .tool("runCommand", { input: { command: "node --version" } })
        .sleep(900)
        .output({ stdout: "v24.18.0" });
      writer
        .tool("runCommand", { input: { command: "npm --version" } })
        .sleep(900)
        .output({ stdout: "11.6.2" });
      writer
        .tool("runCommand", { input: { command: "pnpm --version" } })
        .sleep(900)
        .error("command not found: pnpm");
      writer.text("Node 24 and npm 11 are installed. pnpm is not.");
    });
  const transcript = script.get();
  const [question] = script.get(1);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat<ChatMessage>({ messages: transcript, transport });
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
</script>
{#snippet toolRow(part: ToolPart, streaming: boolean, defaultOpen?: boolean)}
  {@const command = part.input?.command}
  {#if part.state === "output-available" || part.state === "output-error"}
    {@const failed = part.state === "output-error"}
    <Trace.Collapsible open={defaultOpen}>
      <Trace.CollapsibleTrigger>
        <Trace.Line status={failed ? "error" : undefined}>
          <Trace.Icon>
            <TerminalIcon />
          </Trace.Icon>
          <Trace.Title>
            {failed ? "Failed to run" : "Ran"}
            {command}
          </Trace.Title>
        </Trace.Line>
      </Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent>
        <CodeBlock.Root size="sm">
          <CodeBlock.Content
            wrap
            class="max-h-64"
            code={failed ? part.errorText : part.output.stdout}
          />
        </CodeBlock.Root>
      </Trace.CollapsibleContent>
    </Trace.Collapsible>
  {:else}
    <Trace.Line status={streaming ? "running" : "error"}>
      <Trace.Icon>
        <TerminalIcon />
      </Trace.Icon>
      <Trace.Title>
        {streaming ? "Running" : "Failed to run"}
        {command}
      </Trace.Title>
    </Trace.Line>
  {/if}
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
      {@const tools = message.parts.filter(
        (part) => part.type === "tool-runCommand"
      )}
      {@const text = getMessageText(message)}
      <Message.Root>
        <Message.Content class="gap-4">
          {#if tools.length > 0}
            <Trace.Root>
              {#each tools as part (part.toolCallId)}
                {@render toolRow(
                  part,
                  streaming,
                  untrack(() =>
                    busy ? undefined : part.state === "output-error"
                  )
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

Tool is a tool call the agent makes, such as running a command or reading a file. The line follows the call from input to output, including errors and calls that wait for approval.

Tool is built with `Trace` with a `Trace.Collapsible` for each call that has output.

## [Installation](#installation)

Tool is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) and [Code Block](https://shadcn-svelte.com/docs/components/code-block) components.

```bash
pnpm dlx shadcn-svelte@latest add trace code-block
```

```bash
npx shadcn-svelte@latest add trace code-block
```

```bash
bun x shadcn-svelte@latest add trace code-block
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
</script>
```

```svelte
<Trace.Root>
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <TerminalIcon />
        </Trace.Icon>
        <Trace.Title>Ran git status --short</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <CodeBlock.Root size="sm">
        <CodeBlock.Content wrap class="max-h-64" code={output} />
      </CodeBlock.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [States](#states)

Trace does not read tool parts. Map each part's `state` to a `status` and a title.

```svelte
<script lang="ts">
  import TerminalIcon from "@lucide/svelte/icons/terminal";
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  const status = ` M app/api/chat/route.ts
 M components/chat.tsx`;
</script>
<Trace.Root class="max-w-sm">
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <TerminalIcon />
        </Trace.Icon>
        <Trace.Title>Ran git status --short</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <CodeBlock.Root size="sm">
        <CodeBlock.Content wrap class="max-h-64" code={status} />
      </CodeBlock.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line status="error">
        <Trace.Icon>
          <TerminalIcon />
        </Trace.Icon>
        <Trace.Title>Failed to run pnpm dev</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <CodeBlock.Root size="sm">
        <CodeBlock.Content
          wrap
          class="max-h-64"
          code="Command timed out after 120 seconds."
        />
      </CodeBlock.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
  <Trace.Line>
    <Trace.Icon>
      <TerminalIcon />
    </Trace.Icon>
    <Trace.Title>Denied rm -rf dist</Trace.Title>
  </Trace.Line>
  <Trace.Line status="running">
    <Trace.Icon>
      <TerminalIcon />
    </Trace.Icon>
    <Trace.Title>Running pnpm test</Trace.Title>
  </Trace.Line>
</Trace.Root>
```

View Code

| Tool part state                                                                       | `status`                             | Title                                                                                            |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------- |
| `input-streaming`, `input-available`                      | `"running"` while the chat streams   | Running                                                                                         |
| `input-streaming`, `input-available` after the chat stops | `"error"`                            | Failed to run                                                                                   |
| `approval-requested`                                                    | -                                           | Not a line. An `Item` outside `Trace` with Approve and Deny buttons. |
| `approval-responded`                                                    | `"running"` if approved, none if not | Running  if approved, Denied  if not                                                           |
| `output-available`                                                      | none                                        | Ran                                                                                             |
| `output-error`                                                          | `"error"`                            | Failed to run                                                                                   |
| `output-denied`                                                         | none                                        | Denied                                                                            |

A tool is a plain `Trace.Line` while it runs, and a `Trace.Collapsible` once its output arrives.

```svelte
{#snippet toolLine(part: ToolPart, streaming: boolean)}
  {@const command = part.input?.command}
  {#if part.state === "output-denied" || (part.state === "approval-responded" && !part.approval.approved)}
    <Trace.Line>
      <Trace.Icon>
        <TerminalIcon />
      </Trace.Icon>
      <Trace.Title>Denied {command}</Trace.Title>
    </Trace.Line>
  {:else if part.state === "output-available" || part.state === "output-error"}
    {@const failed = part.state === "output-error"}
    <Trace.Collapsible>
      <Trace.CollapsibleTrigger>
        <Trace.Line status={failed ? "error" : undefined}>
          <Trace.Icon>
            <TerminalIcon />
          </Trace.Icon>
          <Trace.Title>{failed ? "Failed to run" : "Ran"} {command}</Trace.Title>
        </Trace.Line>
      </Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent>
        <CodeBlock.Root size="sm">
          <CodeBlock.Content
            wrap
            class="max-h-64"
            code={failed ? part.errorText : part.output.stdout}
          />
        </CodeBlock.Root>
      </Trace.CollapsibleContent>
    </Trace.Collapsible>
  {:else}
    <Trace.Line status={streaming ? "running" : "error"}>
      <Trace.Icon>
        <TerminalIcon />
      </Trace.Icon>
      <Trace.Title>{streaming ? "Running" : "Failed to run"} {command}</Trace.Title>
    </Trace.Line>
  {/if}
{/snippet}
```

```svelte
<Trace.Root>
  {#each message.parts.filter((part) => part.type === "tool-runCommand") as part (part.toolCallId)}
    {@render toolLine(part, streaming)}
  {/each}
</Trace.Root>
```

A tool that runs on the client stays `input-available` after the chat stops until you call `addToolOutput`. Treat it as waiting, not failed.

## [Output in a Sheet](#output-in-a-sheet)

For long output, wrap the `Trace.Line` in a `Sheet.Trigger` and show the output in the sheet.

```svelte
<script lang="ts">
  import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import { Chat } from "@ai-sdk/svelte";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Sheet from "$lib/components/ui/sheet/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import type { UIDataTypes, UIMessage } from "ai";
  type ChatMessage = UIMessage<
    unknown,
    UIDataTypes,
    {
      readFile: {
        input: { path: string };
        output: { path: string; content: string };
      };
    }
  >;
  const PACKAGE_JSON = `{
  "name": "acme-chat",
  "private": true,
  "dependencies": {
    "@ai-sdk/react": "^4.0.0",
    "ai": "^7.0.0",
    "next": "^16.3.0"
  }
}`;
  const script = createChat<ChatMessage>()
    .user("Which AI SDK version does this app use?")
    .assistant(({ writer }) => {
      writer
        .tool("readFile", { input: { path: "package.json" } })
        .sleep(900)
        .output({ path: "package.json", content: PACKAGE_JSON });
      writer.text("It uses ai 7 with @ai-sdk/react 4.");
    });
  const initialMessages = script.get(0);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat<ChatMessage>({ messages: initialMessages, transport });
  const nextMessage = $derived(script.next(chat.messages));
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
</script>
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
      <Message.Root>
        <Message.Content class="gap-4">
          {#each message.parts as part, index (index)}
            {#if part.type === "text"}
              <p>{part.text}</p>
            {:else if part.type === "tool-readFile"}
              {#if part.state !== "output-available"}
                {@const running =
                  streaming &&
                  (part.state === "input-streaming" ||
                    part.state === "input-available")}
                <Trace.Root>
                  <Trace.Line status={running ? "running" : "error"}>
                    <Trace.Icon>
                      <FileTextIcon />
                    </Trace.Icon>
                    <Trace.Title>
                      {running ? "Reading" : "Failed to read"}
                      {part.input?.path}
                    </Trace.Title>
                  </Trace.Line>
                </Trace.Root>
              {:else}
                <Trace.Root>
                  <Sheet.Root>
                    <Sheet.Trigger>
                      <Trace.Line>
                        <Trace.Icon>
                          <FileTextIcon />
                        </Trace.Icon>
                        <Trace.Title>Read {part.output.path}</Trace.Title>
                        <Trace.Icon>
                          <ChevronRightIcon />
                        </Trace.Icon>
                      </Trace.Line>
                    </Sheet.Trigger>
                    <Sheet.Content>
                      <Sheet.Header>
                        <Sheet.Title class="font-mono"
                          >{part.output.path}</Sheet.Title
                        >
                        <Sheet.Description>
                          {part.output.content.split("\n").length} lines
                        </Sheet.Description>
                      </Sheet.Header>
                      <CodeBlock.Root class="mx-6 mb-6 w-auto">
                        <CodeBlock.Content
                          lineNumbers
                          code={part.output.content}
                        />
                      </CodeBlock.Root>
                    </Sheet.Content>
                  </Sheet.Root>
                </Trace.Root>
              {/if}
            {/if}
          {/each}
        </Message.Content>
      </Message.Root>
    {/if}
  {/each}
  {#if !busy}
    <Button
      variant="outline"
      size="sm"
      class="mt-auto self-start"
      onclick={() =>
        nextMessage
          ? void chat.sendMessage(nextMessage)
          : (chat.messages = initialMessages)}
    >
      {nextMessage ? "Send message" : "Reset"}
    </Button>
  {/if}
</div>
```

View Code

See [Trace](https://shadcn-svelte.com/docs/components/trace#dialog).

## [Approval](#approval)

A pending approval is a question for the person, not a step the agent took, so it sits outside `Trace` as an `Item`. Once the person answers, the tool goes back to being a line. See [Confirmation](https://shadcn-svelte.com/docs/ai-elements/confirmation).

```svelte
<script lang="ts">
  import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
  import LoaderCircleIcon from "@lucide/svelte/icons/loader-circle";
  import TerminalIcon from "@lucide/svelte/icons/terminal";
  import { Chat } from "@ai-sdk/svelte";
  import {
    lastAssistantMessageIsCompleteWithApprovalResponses,
    type UIDataTypes,
    type UIMessage
  } from "ai";
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as Item from "$lib/components/ui/item/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Button } from "$lib/components/ui/button/index.js";
  type ChatMessage = UIMessage<
    unknown,
    UIDataTypes,
    {
      runCommand: {
        input: { command: string };
        output: { stdout: string };
      };
    }
  >;
  const script = createChat<ChatMessage>()
    .user("Clean up the build folder.")
    .sleep(600)
    .assistant(({ writer }) => {
      writer.reasoning(
        "The build output lives in dist. Deleting it cannot be undone, so I should ask before I run the command."
      );
      writer.sleep(400);
      writer.tool("runCommand", {
        input: { command: "rm -rf dist" },
        needsApproval: true,
        output: { stdout: "" }
      });
    })
    .assistant(({ writer, toolCall }) => {
      writer.sleep(600);
      writer.text(
        toolCall?.approved
          ? "Removed the dist folder."
          : "Okay, I left the dist folder in place."
      );
    });
  const initialMessages = script.get(0);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat<ChatMessage>({
    messages: initialMessages,
    transport,
    sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithApprovalResponses
  });
  const nextMessage = $derived(script.next(chat.messages));
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  // The reader's choice for each reasoning row. Until they click, it follows `running`.
  let reasoningOpen = $state<Record<string, boolean>>({});
</script>
{#snippet reasoningLine(id: string, text: string, running: boolean)}
  <Trace.Collapsible
    open={reasoningOpen[id] ?? running}
    onOpenChange={(open) => (reasoningOpen[id] = open)}
  >
    <Trace.CollapsibleTrigger>
      <Trace.Line status={running ? "running" : undefined}>
        <Trace.Icon>
          {#if running}
            <LoaderCircleIcon class="animate-spin" />
          {:else}
            <CircleCheckIcon />
          {/if}
        </Trace.Icon>
        <Trace.Title>{running ? "Thinking" : "Thought"}</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent class="whitespace-pre-wrap"
      >{text}</Trace.CollapsibleContent
    >
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
      <Message.Root>
        <Message.Content class="gap-4">
          {#each message.parts as part, index (index)}
            {#if part.type === "text"}
              <p>{part.text}</p>
            {:else if part.type === "reasoning"}
              <Trace.Root>
                {@render reasoningLine( `${message.id}-${index}`,
                  part.text,
                  part.state === "streaming"
                )}
              </Trace.Root>
            {:else if part.type === "tool-runCommand"}
              {#if part.state === "approval-requested"}
                {@const approvalId = part.approval.id}
                <Item.Root variant="outline" size="sm">
                  <Item.Media variant="icon">
                    <TerminalIcon />
                  </Item.Media>
                  <Item.Content>
                    <Item.Title>Run {part.input.command}?</Item.Title>
                    <Item.Description
                      >The command runs in this project.</Item.Description
                    >
                  </Item.Content>
                  <Item.Actions>
                    <Button
                      size="sm"
                      variant="outline"
                      onclick={() =>
                        chat.addToolApprovalResponse({
                          id: approvalId,
                          approved: false
                        })}
                    >
                      Deny
                    </Button>
                    <Button
                      size="sm"
                      onclick={() =>
                        chat.addToolApprovalResponse({
                          id: approvalId,
                          approved: true
                        })}
                    >
                      Approve
                    </Button>
                  </Item.Actions>
                </Item.Root>
              {:else}
                {@const denied =
                  part.state === "output-denied" ||
                  (part.state === "approval-responded" &&
                    !part.approval.approved)}
                <Trace.Root>
                  <Trace.Line
                    status={!denied && part.state !== "output-available"
                      ? "running"
                      : undefined}
                  >
                    <Trace.Icon>
                      <TerminalIcon />
                    </Trace.Icon>
                    <Trace.Title>
                      {denied
                        ? "Denied"
                        : part.state === "output-available"
                          ? "Ran"
                          : "Running"}
                      {part.input?.command}
                    </Trace.Title>
                  </Trace.Line>
                </Trace.Root>
              {/if}
            {/if}
          {/each}
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
        if (nextMessage) {
          void chat.sendMessage(nextMessage);
        } else {
          reasoningOpen = {};
          chat.messages = initialMessages;
        }
      }}
    >
      {nextMessage ? "Send message" : "Reset"}
    </Button>
  {/if}
</div>
```

View Code

```svelte
{#if part.state === "approval-requested"}
  <Item.Root variant="outline" size="sm">
    <Item.Media variant="icon">
      <TerminalIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Run {part.input.command}?</Item.Title>
    </Item.Content>
    <Item.Actions>
      <Button
        size="sm"
        variant="outline"
        onclick={() =>
          chat.addToolApprovalResponse({
            id: part.approval.id,
            approved: false,
          })}
      >
        Deny
      </Button>
      <Button
        size="sm"
        onclick={() =>
          chat.addToolApprovalResponse({
            id: part.approval.id,
            approved: true,
          })}
      >
        Approve
      </Button>
    </Item.Actions>
  </Item.Root>
{/if}
```

Pass `sendAutomaticallyWhen: lastAssistantMessageIsCompleteWithApprovalResponses` to `new Chat()` so the chat continues once every approval has an answer.

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).