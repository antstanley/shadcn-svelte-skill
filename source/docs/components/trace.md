# Trace

The building block for reasoning, tool calls, sources and more.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
 import CircleAlertIcon from "@lucide/svelte/icons/circle-alert";
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import GlobeIcon from "@lucide/svelte/icons/globe";
 import LoaderCircleIcon from "@lucide/svelte/icons/loader-circle";
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
 type Part = ChatMessage["parts"][number];
 type ToolPart = Extract<Part, { type: "tool-runCommand" }>;
 type SourcePart = Extract<Part, { type: "source-url" }>;
 const script = createChat<ChatMessage>()
  .user("Why does pnpm install fail in CI?")
  .assistant(({ writer }) => {
   writer.reasoning(
    "CI installs with a frozen lockfile, so the install stops when package.json and pnpm-lock.yaml disagree. I should check what the last commit changed, then reproduce the install.",
    { delayMs: 40 }
   );
   writer
    .tool("runCommand", { input: { command: "pnpm --version" } })
    .sleep(700)
    .output({ stdout: "10.18.0" });
   writer
    .tool("runCommand", {
     input: {
      command: "git diff --stat HEAD~1 -- package.json pnpm-lock.yaml", },
    })
    .sleep(900)
    .output({
     stdout: " package.json | 2 +-\n 1 file changed, 1 insertion(+), 1 deletion(-)",
    });
   writer
    .tool("runCommand", {
     input: { command: "pnpm install --frozen-lockfile" },
    })
    .sleep(1200)
    .error(
     'ERR_PNPM_OUTDATED_LOCKFILE  Cannot install with "frozen-lockfile" because pnpm-lock.yaml is not up to date with package.json'
    );
   writer.sourceUrl({
    url: "https://pnpm.io/cli/install#--frozen-lockfile",
    title: "pnpm install | pnpm.io",
   });
   writer.sourceUrl({
    url: "https://pnpm.io/continuous-integration",
    title: "Continuous Integration | pnpm.io",
   });
   writer.sleep(1000);
   writer.text(
    "The last commit bumped a version in package.json without updating pnpm-lock.yaml, so the frozen install fails. Run pnpm install locally and commit the lockfile."
   );
  });
 const transcript = script.get();
 const [question] = script.get(1);
 const transport = script.transport({ delayMs: 20 });
 const chat = new Chat<ChatMessage>({ messages: transcript, transport });
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
 // The reader's choice for each thinking row. Until they click, it follows `running`.
 let thinkingOpen = $state<Record<string, boolean>>({});
</script>
{#snippet thinkingLine(running: boolean)}
 <Trace.Line status={running ? "running" : undefined}>
  <Trace.Icon>
   {#if running}
    <LoaderCircleIcon class="animate-spin" />
   {:else}
    <CircleCheckIcon />
   {/if}
  </Trace.Icon>
  <Trace.Title>{running ? "Thinking" : "Thought for 5s"}</Trace.Title>
 </Trace.Line>
{/snippet}
{#snippet thinkingRow(id: string, text: string, running: boolean)}
 {#if text.length === 0}
  {@render thinkingLine(running)}
 {:else}
  <Trace.Collapsible
   open={thinkingOpen[id] ?? running}
   onOpenChange={(open) => (thinkingOpen[id] = open)}
  >
   <Trace.CollapsibleTrigger>{@render thinkingLine(running)}</Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent class="whitespace-pre-wrap">
    {text}
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
 {/if}
{/snippet}
{#snippet toolRow(part: ToolPart, streaming: boolean, defaultOpen?: boolean)}
 {@const command = part.input?.command}
 {#if part.state === "output-available" || part.state === "output-error"}
  {@const failed = part.state === "output-error"}
  <Trace.Collapsible open={defaultOpen}>
   <Trace.CollapsibleTrigger>
    <Trace.Line status={failed ? "error" : undefined}>
     <Trace.Icon>
      {#if failed}
       <CircleAlertIcon />
      {:else}
       <CircleCheckIcon />
      {/if}
     </Trace.Icon>
     <Trace.Title>
      {failed ? "Failed to run" : "Ran"}
      {command}
     </Trace.Title>
    </Trace.Line>
   </Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent>
    {#if failed}
     <CodeBlock.Root size="sm" variant="destructive">
      <CodeBlock.Content wrap class="max-h-64" code={part.errorText} />
     </CodeBlock.Root>
    {:else}
     <CodeBlock.Root size="sm">
      <CodeBlock.Content wrap class="max-h-64" code={part.output.stdout} />
     </CodeBlock.Root>
    {/if}
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
 {:else}
  <Trace.Line status={streaming ? "running" : "error"}>
   <Trace.Icon>
    {#if streaming}
     <LoaderCircleIcon class="animate-spin" />
    {:else}
     <CircleAlertIcon />
    {/if}
   </Trace.Icon>
   <Trace.Title>
    {streaming ? "Running" : "Failed to run"}
    {command}
   </Trace.Title>
  </Trace.Line>
 {/if}
{/snippet}
{#snippet sourcesRow(sources: SourcePart[], running: boolean)}
 <Trace.Collapsible>
  <Trace.CollapsibleTrigger>
   <Trace.Line status={running ? "running" : undefined}>
    <Trace.Icon>
     {#if running}
      <LoaderCircleIcon class="animate-spin" />
     {:else}
      <GlobeIcon />
     {/if}
    </Trace.Icon>
    <Trace.Title>
     {running ? "Using" : "Used"}
     {sources.length} sources
    </Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <Trace.Root>
    {#each sources as source (source.sourceId)}
     <a href={source.url} target="_blank" rel="noreferrer">
      <Trace.Line>
       <Trace.Icon>
        <GlobeIcon />
       </Trace.Icon>
       <Trace.Title>
        {source.title ?? new URL(source.url).hostname}
        <span class="sr-only"> (opens in a new tab)</span>
       </Trace.Title>
       <Trace.Icon>
        <ArrowUpRightIcon />
       </Trace.Icon>
      </Trace.Line>
     </a>
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
   {@const rows = message.parts.filter(
    (part) => part.type === "reasoning" || part.type === "tool-runCommand"
   )}
   {@const sources = message.parts.filter((part) => part.type === "source-url")}
   {@const text = getMessageText(message)}
   <Message.Root>
    <Message.Content class="gap-4">
     {#if rows.length + sources.length > 0}
      <Trace.Root>
       {#each rows as part, index (part.type === "tool-runCommand" ? part.toolCallId : index)}
        {#if part.type === "reasoning"}
         {@render thinkingRow( `${message.id}-${index}`,
          part.text,
          streaming && part.state === "streaming"
         )}
        {:else if part.type === "tool-runCommand"}
         {@render toolRow(
          part,
          streaming,
          untrack(() => index === 2)
         )}
        {/if}
       {/each}
       {#if sources.length > 0}
        {@render sourcesRow(sources, streaming && text.length === 0)}
       {/if}
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
    thinkingOpen = {};
    chat.messages = [];
    void chat.sendMessage(question);
   }}
  >
   Replay
  </Button>
 {/if}
</div>
```

View Code `Trace` is a list of lines. Each line has an icon, a title, and an optional description and status. A line can expand to show more detail, link to a page, or open a dialog or sheet.

Every line has the same shape, so reasoning, tool calls, sources and plans built from `Trace` look and behave the same.

Use `Trace` for the steps an agent takes, like calling a tool, running a subagent or editing a file. Use [Message](https://shadcn-svelte.com/docs/components/message) for its reply, and [Marker](https://shadcn-svelte.com/docs/components/marker) for notes and dividers between turns.

## [Built with Trace](#built-with-trace)

Every pattern below is a composition of `Trace` parts. See [AI Elements](https://shadcn-svelte.com/docs/ai-elements) for examples and code.

| Pattern                                                                                                        | Shows                                                             |
| -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| [Chain of Thought](https://shadcn-svelte.com/docs/ai-elements/chain-of-thought) | A summary that expands into the steps behind it.                  |
| [Plan](https://shadcn-svelte.com/docs/ai-elements/plan)                         | The steps the agent plans to take, and how far it has got.        |
| [Queue](https://shadcn-svelte.com/docs/ai-elements/queue)                       | The agent's todo list, split into what is left and what is done.  |
| [Reasoning](https://shadcn-svelte.com/docs/ai-elements/reasoning)               | The agent's thinking as it streams.                               |
| [Sources](https://shadcn-svelte.com/docs/ai-elements/sources)                   | The links the agent used for a reply.                             |
| [Stack Trace](https://shadcn-svelte.com/docs/ai-elements/stack-trace)           | A failed tool call and its stack frames.                          |
| [Subagent](https://shadcn-svelte.com/docs/ai-elements/subagent)                 | A subagent run, with its tool calls and result.                   |
| [Task](https://shadcn-svelte.com/docs/ai-elements/task)                         | The steps the agent takes, as it takes them.                      |
| [Terminal](https://shadcn-svelte.com/docs/ai-elements/terminal)                 | A command the agent runs, with its output as it streams.          |
| [Test Results](https://shadcn-svelte.com/docs/ai-elements/test-results)         | A test run by the agent, with its suites and failures.            |
| [Tool](https://shadcn-svelte.com/docs/ai-elements/tool)                         | A tool call the agent makes, from input to output. |

## [Installation](#installation)

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

Use a `Trace.Line` for a single step:

```svelte
<script lang="ts">
  import * as Trace from "$lib/components/ui/trace/index.js";
</script>
```

```svelte
<Trace.Root>
  <Trace.Line>
    <Trace.Icon>
      <SearchIcon />
    </Trace.Icon>
    <Trace.Title>Searched for minimumReleaseAge</Trace.Title>
  </Trace.Line>
</Trace.Root>
```

Wrap the line in a `Trace.Collapsible` to show more detail when it expands:

```svelte
<Trace.Root>
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <TerminalIcon />
        </Trace.Icon>
        <Trace.Title>Ran node --version</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>v24.18.0</Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [Composition](#composition)

Use the following composition to build a trace line:

```text
Trace.Root
 Trace.Line
     Trace.Icon
     Trace.Title
     Trace.Description
     Trace.Icon
```

Wrap the line in a `Trace.Collapsible` to show more detail when it expands:

```text
Trace.Root
 Trace.Collapsible
     Trace.CollapsibleTrigger
        Trace.Line
     Trace.CollapsibleContent
``` `Trace.Line` is always the line. To make a line do something, wrap it in that thing's trigger.

## [Features](#features)

- One row for reasoning, tool calls, sources, plans and tasks  
- Rows that expand, link out, or open a dialog, sheet, drawer or popover  
- `running` , `error` and `pending` states, with a shimmer while running
- Nested rows, so a summary expands into steps and a step into its output  
- Keyboard and screen reader support from the trigger that wraps each row  
- Customizable styling through the `class` prop on every part

## [Trace Line](#trace-line)

Use a `Trace.Line` on its own for a step with no detail to show. It reads as plain text.

```svelte
<script lang="ts">
 import GitBranchIcon from "@lucide/svelte/icons/git-branch";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<Trace.Root class="max-w-sm">
 <Trace.Line>
  <Trace.Icon>
   <GitBranchIcon />
  </Trace.Icon>
  <Trace.Title>Created branch fix/frozen-lockfile</Trace.Title>
 </Trace.Line>
</Trace.Root>
```

View Code

## [Status](#status)

Set `status` on `Trace.Line` when a step is running, has failed or hasn't started yet.

```svelte
<script lang="ts">
 import CircleIcon from "@lucide/svelte/icons/circle";
 import CircleAlertIcon from "@lucide/svelte/icons/circle-alert";
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import LoaderCircleIcon from "@lucide/svelte/icons/loader-circle";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<Trace.Root class="max-w-sm">
 <Trace.Line>
  <Trace.Icon>
   <CircleCheckIcon />
  </Trace.Icon>
  <Trace.Title>Ran pnpm install</Trace.Title>
 </Trace.Line>
 <Trace.Line status="error">
  <Trace.Icon>
   <CircleAlertIcon />
  </Trace.Icon>
  <Trace.Title>Failed to run pnpm lint</Trace.Title>
 </Trace.Line>
 <Trace.Line status="running">
  <Trace.Icon>
   <LoaderCircleIcon class="animate-spin" />
  </Trace.Icon>
  <Trace.Title>Running pnpm build</Trace.Title>
 </Trace.Line>
 <Trace.Line status="pending">
  <Trace.Icon>
   <CircleIcon />
  </Trace.Icon>
  <Trace.Title>Run pnpm test</Trace.Title>
 </Trace.Line>
</Trace.Root>
```

View Code

| Status                     | Use for                                                                         |
| -------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| none               | Work that is done: "Ran pnpm install".                                          |
| `"error"`   | Work that failed. Say so in the title: "Failed to run pnpm lint".               |
| `"running"` | Work in progress. Write the title in the present tense: "Running pnpm build".   |
| `"pending"` | Work that has not started, such as a plan step: "Run pnpm test". |

## [Description](#description)

Put secondary text such as a diff stat, a duration or a count in a `Trace.Description` after the `Trace.Title`. It does not truncate.

```svelte
<script lang="ts">
 import FilePenIcon from "@lucide/svelte/icons/file-pen";
 import SearchIcon from "@lucide/svelte/icons/search";
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<Trace.Root class="max-w-sm">
 <Trace.Line>
  <Trace.Icon>
   <FilePenIcon />
  </Trace.Icon>
  <Trace.Title>Edited components/settings/notification-preferences-form.tsx</Trace.Title>
  <Trace.Description class="font-mono">+48 12</Trace.Description>
 </Trace.Line>
 <Trace.Line>
  <Trace.Icon>
   <TerminalIcon />
  </Trace.Icon>
  <Trace.Title>Ran pnpm test</Trace.Title>
  <Trace.Description>14s</Trace.Description>
 </Trace.Line>
 <Trace.Line>
  <Trace.Icon>
   <SearchIcon />
  </Trace.Icon>
  <Trace.Title>Searched for useChat</Trace.Title>
  <Trace.Description>8 results</Trace.Description>
 </Trace.Line>
</Trace.Root>
```

View Code

## [Collapsible](#collapsible)

Wrap the line in a `Trace.Collapsible` to show more detail when it expands. Put the `Trace.Line` inside `Trace.CollapsibleTrigger` and the detail in `Trace.CollapsibleContent`.

```svelte
<script lang="ts">
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 const output = "$ node --version\nv24.18.0";
</script>
<div class="w-full max-w-sm">
 <Trace.Collapsible>
  <Trace.CollapsibleTrigger>
   <Trace.Line>
    <Trace.Icon>
     <TerminalIcon />
    </Trace.Icon>
    <Trace.Title>Ran node --version</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <CodeBlock.Root size="sm">
    <CodeBlock.Content wrap class="max-h-64" code={output} />
   </CodeBlock.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</div>
```

View Code

## [Open State](#open-state)

Rows start closed. Bind `open` on `Trace.Collapsible` to start open or to control a row.

```svelte
<script lang="ts">
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 let open = $state(false);
 const nodeOutput = "$ node --version\nv24.18.0";
 const pnpmOutput = "$ pnpm --version\n10.33.4";
</script>
<div class="flex w-full max-w-sm flex-col items-start gap-4">
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line>
    <Trace.Icon>
     <TerminalIcon />
    </Trace.Icon>
    <Trace.Title>Ran node --version</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <CodeBlock.Root size="sm">
    <CodeBlock.Content wrap class="max-h-64" code={nodeOutput} />
   </CodeBlock.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
 <Trace.Collapsible bind:open>
  <Trace.CollapsibleTrigger>
   <Trace.Line>
    <Trace.Icon>
     <TerminalIcon />
    </Trace.Icon>
    <Trace.Title>Ran pnpm --version</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <CodeBlock.Root size="sm">
    <CodeBlock.Content wrap class="max-h-64" code={pnpmOutput} />
   </CodeBlock.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
 <Button variant="outline" size="sm" onclick={() => (open = !open)}>
  {open ? "Hide" : "Show"} the pnpm output
 </Button>
</div>
```

View Code

To open a row while it streams and let the reader's click win, pass `open ?? running`.

```svelte
<script lang="ts">
  let open = $state<boolean>();
</script>
<Trace.Collapsible
  open={open ?? running}
  onOpenChange={(value) => (open = value)}
>
  <Trace.CollapsibleTrigger>
    <Trace.Line status={running ? "running" : undefined}></Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>{text}</Trace.CollapsibleContent>
</Trace.Collapsible>
```

## [Link](#link)

Wrap the `Trace.Line` in an anchor. For a new tab, use an arrow-up-right icon and sr-only "(opens in a new tab)".

```svelte
<script lang="ts">
 import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
 import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
 import FileTextIcon from "@lucide/svelte/icons/file-text";
 import GlobeIcon from "@lucide/svelte/icons/globe";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<Trace.Root class="max-w-sm">
 <a href="#link">
  <Trace.Line>
   <Trace.Icon>
    <FileTextIcon />
   </Trace.Icon>
   <Trace.Title>Read apps/v4/lib/docs.ts</Trace.Title>
   <Trace.Icon>
    <ChevronRightIcon />
   </Trace.Icon>
  </Trace.Line>
 </a>
 <a href="https://docs.astro.build/en/install-and-setup/" target="_blank" rel="noreferrer">
  <Trace.Line>
   <Trace.Icon>
    <GlobeIcon />
   </Trace.Icon>
   <Trace.Title>
    Install Astro | docs.astro.build
    <span class="sr-only"> (opens in a new tab)</span>
   </Trace.Title>
   <Trace.Icon>
    <ArrowUpRightIcon />
   </Trace.Icon>
  </Trace.Line>
 </a>
</Trace.Root>
```

View Code

```svelte
<a href="https://docs.astro.build" target="_blank" rel="noreferrer">
  <Trace.Line>
    <Trace.Title>
      Install Astro
      <span class="sr-only"> (opens in a new tab)</span>
    </Trace.Title>
    <Trace.Icon>
      <ArrowUpRightIcon />
    </Trace.Icon>
  </Trace.Line>
</a>
```

## [Dialog](#dialog)

Wrap the `Trace.Line` in the dialog's trigger. The dialog owns its open state, Escape and focus return.

```svelte
<script lang="ts">
 import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
 import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
 import GlobeIcon from "@lucide/svelte/icons/globe";
 import * as Dialog from "$lib/components/ui/dialog/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 const results = [
  {
   title: "Caching build outputs",
   url: "https://nextjs.org/docs/app/guides/caching",
  },
  {
   title: "Image optimization reference",
   url: "https://nextjs.org/docs/app/api-reference/components/image",
  },
  {
   title: "Deploy hooks and cache keys",
   url: "https://vercel.com/docs/deploy-hooks",
  },
];
</script>
<Trace.Root class="max-w-sm">
 <Dialog.Root>
  <Dialog.Trigger>
   <Trace.Line>
    <Trace.Icon>
     <GlobeIcon />
    </Trace.Icon>
    <Trace.Title>Searched the web for cache keys</Trace.Title>
    <Trace.Icon>
     <ChevronRightIcon />
    </Trace.Icon>
   </Trace.Line>
  </Dialog.Trigger>
  <Dialog.Content>
   <Dialog.Header>
    <Dialog.Title>Searched the web for cache keys</Dialog.Title>
    <Dialog.Description>Three results were used in the response.</Dialog.Description>
   </Dialog.Header>
   <Trace.Root>
    {#each results as result, index (index)}
     <a href={result.url} target="_blank" rel="noreferrer">
      <Trace.Line>
       <Trace.Icon>
        <GlobeIcon />
       </Trace.Icon>
       <Trace.Title>
        {result.title}
        <span class="sr-only"> (opens in a new tab)</span>
       </Trace.Title>
       <Trace.Icon>
        <ArrowUpRightIcon />
       </Trace.Icon>
      </Trace.Line>
     </a>
    {/each}
   </Trace.Root>
  </Dialog.Content>
 </Dialog.Root>
</Trace.Root>
```

View Code

```svelte
<Dialog.Root>
  <Dialog.Trigger>
    <Trace.Line>
      <Trace.Title>Searched the web for cache keys</Trace.Title>
      <Trace.Icon>
        <ChevronRightIcon />
      </Trace.Icon>
    </Trace.Line>
  </Dialog.Trigger>
  <Dialog.Content></Dialog.Content>
</Dialog.Root>
```

## [Sheet](#sheet)

The same shape as the dialog. Drawer and Popover work the same way.

```svelte
<script lang="ts">
 import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
 import FolderSearchIcon from "@lucide/svelte/icons/folder-search";
 import * as Sheet from "$lib/components/ui/sheet/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<Trace.Root class="max-w-sm">
 <Sheet.Root>
  <Sheet.Trigger>
   <Trace.Line>
    <Trace.Icon>
     <FolderSearchIcon />
    </Trace.Icon>
    <Trace.Title>Explored 4 files</Trace.Title>
    <Trace.Icon>
     <ChevronRightIcon />
    </Trace.Icon>
   </Trace.Line>
  </Sheet.Trigger>
  <Sheet.Content>
   <Sheet.Header>
    <Sheet.Title>Explored 4 files</Sheet.Title>
    <Sheet.Description>Files read while preparing the response.</Sheet.Description>
   </Sheet.Header>
   <ul class="flex flex-col gap-2 px-6 font-mono text-xs">
    <li>apps/v4/lib/docs.ts</li>
    <li>apps/v4/lib/components.ts</li>
    <li>apps/v4/next.config.mjs</li>
    <li>apps/v4/package.json</li>
   </ul>
  </Sheet.Content>
 </Sheet.Root>
</Trace.Root>
```

View Code

## [Group](#group)

Put rows that sit next to each other in a `Trace.Root`. It also styles any trigger or link that wraps a `Trace.Line`.

```svelte
<script lang="ts">
 import FileTextIcon from "@lucide/svelte/icons/file-text";
 import SearchIcon from "@lucide/svelte/icons/search";
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<Trace.Root class="max-w-sm">
 <Trace.Line>
  <Trace.Icon>
   <SearchIcon />
  </Trace.Icon>
  <Trace.Title>Searched for minimumReleaseAge</Trace.Title>
 </Trace.Line>
 <Trace.Line>
  <Trace.Icon>
   <FileTextIcon />
  </Trace.Icon>
  <Trace.Title>Read pnpm-workspace.yaml</Trace.Title>
 </Trace.Line>
 <Trace.Line>
  <Trace.Icon>
   <TerminalIcon />
  </Trace.Icon>
  <Trace.Title>Ran pnpm install</Trace.Title>
 </Trace.Line>
</Trace.Root>
```

View Code

## [Sources](#sources)

A collapsible row whose detail is a `Trace.Root` of link rows.

```svelte
<script lang="ts">
 import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
 import GlobeIcon from "@lucide/svelte/icons/globe";
 import * as Trace from "$lib/components/ui/trace/index.js";
 const sources = [
  {
   title: "Install Astro | docs.astro.build",
   href: "https://docs.astro.build/en/install-and-setup/",
  },
  {
   title: "create-astro | npmjs.com",
   href: "https://www.npmjs.com/package/create-astro",
  },
  {
   title: "Settings: minimumReleaseAge | pnpm.io",
   href: "https://pnpm.io/settings#minimumreleaseage",
  },
];
</script>
<div class="w-full max-w-sm">
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line>
    <Trace.Icon>
     <GlobeIcon />
    </Trace.Icon>
    <Trace.Title>Used {sources.length} sources</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <Trace.Root>
    {#each sources as source, index (index)}
     <a href={source.href} target="_blank" rel="noreferrer">
      <Trace.Line>
       <Trace.Icon>
        <GlobeIcon />
       </Trace.Icon>
       <Trace.Title>
        {source.title}
        <span class="sr-only"> (opens in a new tab)</span>
       </Trace.Title>
       <Trace.Icon>
        <ArrowUpRightIcon />
       </Trace.Icon>
      </Trace.Line>
     </a>
    {/each}
   </Trace.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</div>
```

View Code

See [Sources](https://shadcn-svelte.com/docs/ai-elements/sources) for more examples.

## [Chain of Thought](#chain-of-thought)

A chain of thought is a collapsible row with step rows inside. Set the parent's status and title from its children.

```svelte
<script lang="ts">
 import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
 import FileTextIcon from "@lucide/svelte/icons/file-text";
 import SearchIcon from "@lucide/svelte/icons/search";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { Badge } from "$lib/components/ui/badge/index.js";
</script>
<div class="w-full max-w-sm">
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line status="running">
    <Trace.Title>Looking into the slow deploy</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <Trace.Root>
    <Trace.Collapsible>
     <Trace.CollapsibleTrigger>
      <Trace.Line>
       <Trace.Icon>
        <SearchIcon />
       </Trace.Icon>
       <Trace.Title>Searched for the checkout build log</Trace.Title>
      </Trace.Line>
     </Trace.CollapsibleTrigger>
     <Trace.CollapsibleContent class="flex flex-wrap gap-1.5">
      <Badge variant="secondary">vercel.com</Badge>
      <Badge variant="secondary">github.com</Badge>
     </Trace.CollapsibleContent>
    </Trace.Collapsible>
    <a href="#steps">
     <Trace.Line>
      <Trace.Icon>
       <FileTextIcon />
      </Trace.Icon>
      <Trace.Title>Read the last twelve deploys</Trace.Title>
      <Trace.Icon>
       <ChevronRightIcon />
      </Trace.Icon>
     </Trace.Line>
    </a>
    <Trace.Collapsible>
     <Trace.CollapsibleTrigger>
      <Trace.Line status="running">
       <Trace.Icon>
        <SearchIcon />
       </Trace.Icon>
       <Trace.Title>Searching for the cache key</Trace.Title>
      </Trace.Line>
     </Trace.CollapsibleTrigger>
     <Trace.CollapsibleContent>
      <CodeBlock.Root size="sm">
       <CodeBlock.Content wrap class="max-h-64" code="cache key image optimization" />
      </CodeBlock.Root>
     </Trace.CollapsibleContent>
    </Trace.Collapsible>
   </Trace.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</div>
```

View Code

See [Chain of Thought](https://shadcn-svelte.com/docs/ai-elements/chain-of-thought) and [Task](https://shadcn-svelte.com/docs/ai-elements/task) for more examples.

## [Commit](#commit)

A commit is a collapsible row with a line for each changed file. Say what changed in the title, Added, Edited or Deleted, and put the line counts in the description. Each file opens its diff in a [Sheet](#sheet).

```svelte
<script lang="ts">
 import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
 import FilePenIcon from "@lucide/svelte/icons/file-pen";
 import FilePlusIcon from "@lucide/svelte/icons/file-plus";
 import GitCommitHorizontalIcon from "@lucide/svelte/icons/git-commit-horizontal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Sheet from "$lib/components/ui/sheet/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 const files = [
  {
   path: "app/login/page.tsx",
   added: false,
   additions: 2,
   deletions: 2,
   diff: `@@ -14,7 +14,7 @@ export default async function LoginPage({
   searchParams,
 }) {
   const { next } = await searchParams
-  const redirectTo =
-    next && next.startsWith("/") ? next : "/"
+  const redirectTo = safeRedirect(next)
+
   return <LoginForm redirectTo={redirectTo} />
 }`,
  },
  {
   path: "lib/auth/redirect.ts",
   added: true,
   additions: 7,
   deletions: 0,
   diff: `@@ -0,0 +1,7 @@
+export function safeRedirect(next: string | undefined) {
+  if (!next || !next.startsWith("/") || next.startsWith("//")) {
+    return "/"
+  }
+
+  return next
+}`,
  },
];
 function getVariant(line: string) {
  if (line.startsWith("+")) {
   return "added";
  }
  if (line.startsWith("-")) {
   return "removed";
  }
  return "default";
 }
</script>
{#snippet diffLines(diff: string)}
 {#each diff.split("\n") as line, index (index)}
  {#if line.startsWith("@@")}
   <CodeBlock.Line class="text-muted-foreground">{line}</CodeBlock.Line>
  {:else}
   <CodeBlock.Line variant={getVariant(line)}>{line.slice(1)}</CodeBlock.Line>
  {/if}
 {/each}
{/snippet}
<Trace.Root class="max-w-sm">
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line>
    <Trace.Icon>
     <GitCommitHorizontalIcon />
    </Trace.Icon>
    <Trace.Title>Committed a1b2c3: Fix the login redirect</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
   <Trace.Root>
    {#each files as file (file.path)}
     <Sheet.Root>
      <Sheet.Trigger>
       <Trace.Line>
        <Trace.Icon>
         {#if file.added}
          <FilePlusIcon />
         {:else}
          <FilePenIcon />
         {/if}
        </Trace.Icon>
        <Trace.Title>
         {file.added ? "Added" : "Edited"}
         {file.path}
        </Trace.Title>
        <Trace.Description class="font-mono">
         +{file.additions} {file.deletions}
        </Trace.Description>
        <Trace.Icon>
         <ChevronRightIcon />
        </Trace.Icon>
       </Trace.Line>
      </Sheet.Trigger>
      <Sheet.Content>
       <Sheet.Header>
        <Sheet.Title class="font-mono">{file.path}</Sheet.Title>
        <Sheet.Description>
         {file.additions} additions, {file.deletions} deletions
        </Sheet.Description>
       </Sheet.Header>
       <CodeBlock.Root class="mx-6 mb-6 w-auto">
        <CodeBlock.Content>
         {@render diffLines(file.diff)}
        </CodeBlock.Content>
       </CodeBlock.Root>
      </Sheet.Content>
     </Sheet.Root>
    {/each}
   </Trace.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</Trace.Root>
```

View Code

## [Whole Turn](#whole-turn)

Three levels: the turn, a summary, and the rows. Text between steps sits between two `Trace.Root` lists.

```svelte
<script lang="ts">
 import BrainIcon from "@lucide/svelte/icons/brain";
 import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
 import FileTextIcon from "@lucide/svelte/icons/file-text";
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<div class="w-full max-w-sm">
 <Trace.Collapsible open>
  <Trace.CollapsibleTrigger>
   <Trace.Line status="error">
    <Trace.Title>Worked for 2m 4s, 1 command failed</Trace.Title>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent class="flex flex-col gap-2">
   <Trace.Root>
    <Trace.Collapsible>
     <Trace.CollapsibleTrigger>
      <Trace.Line>
       <Trace.Icon>
        <BrainIcon />
       </Trace.Icon>
       <Trace.Title>Thought</Trace.Title>
       <Trace.Description>12s</Trace.Description>
      </Trace.Line>
     </Trace.CollapsibleTrigger>
     <Trace.CollapsibleContent class="whitespace-pre-wrap">
      I should check which package managers are installed before I scaffold anything.
     </Trace.CollapsibleContent>
    </Trace.Collapsible>
    <Trace.Collapsible open>
     <Trace.CollapsibleTrigger>
      <Trace.Line status="error">
       <Trace.Icon>
        <TerminalIcon />
       </Trace.Icon>
       <Trace.Title>Ran 2 commands, 1 failed</Trace.Title>
      </Trace.Line>
     </Trace.CollapsibleTrigger>
     <Trace.CollapsibleContent>
      <Trace.Root>
       <Trace.Line>
        <Trace.Icon>
         <TerminalIcon />
        </Trace.Icon>
        <Trace.Title>Ran node --version</Trace.Title>
       </Trace.Line>
       <Trace.Collapsible>
        <Trace.CollapsibleTrigger>
         <Trace.Line status="error">
          <Trace.Icon>
           <TerminalIcon />
          </Trace.Icon>
          <Trace.Title>Failed to run pnpm --version</Trace.Title>
         </Trace.Line>
        </Trace.CollapsibleTrigger>
        <Trace.CollapsibleContent>
         <CodeBlock.Root size="sm" variant="destructive">
          <CodeBlock.Content wrap class="max-h-64" code="command not found: pnpm" />
         </CodeBlock.Root>
        </Trace.CollapsibleContent>
       </Trace.Collapsible>
      </Trace.Root>
     </Trace.CollapsibleContent>
    </Trace.Collapsible>
   </Trace.Root>
   <p>Node is installed and pnpm is not. Reading the docs config.</p>
   <Trace.Root>
    <a href="#turn">
     <Trace.Line>
      <Trace.Icon>
       <FileTextIcon />
      </Trace.Icon>
      <Trace.Title>Read apps/v4/lib/docs.ts</Trace.Title>
      <Trace.Icon>
       <ChevronRightIcon />
      </Trace.Icon>
     </Trace.Line>
    </a>
   </Trace.Root>
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</div>
```

View Code

## [Reasoning](#reasoning)

Render a `reasoning` part from the AI SDK. The row is a `Trace.Line` until the first text arrives. See [Open State](#open-state).

```svelte
<script lang="ts">
 import BrainIcon from "@lucide/svelte/icons/brain";
 import { Chat } from "@ai-sdk/svelte";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import type { UIMessage } from "ai";
 const script = createChat()
  .user("Why is the checkout deploy so slow?")
  .assistant(({ writer }) => {
   writer.reasoning(
    "The build log shows install and compile finish in under a minute. Image optimization takes almost four, and it reruns on every deploy because the cache key includes the commit hash.",
    { delayMs: 60 }
   );
   writer.sleep(400);
   writer.text(
    "Image optimization is the bottleneck. Key its cache on the lockfile and the image directory instead of the commit hash."
   );
  });
 const initialMessages = script.get(0);
 const transport = script.transport({ delayMs: 20 });
 const chat = new Chat({ messages: initialMessages, transport });
 const nextMessage = $derived(script.next(chat.messages));
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
 // The reader's choice for each thinking row. Until they click, it follows `running`.
 let thinkingOpen = $state<Record<string, boolean>>({});
 function groupParts(parts: UIMessage["parts"]) {
  const runs: { trace: boolean; parts: UIMessage["parts"] }[] = [];
  for (const part of parts) {
   const trace = part.type === "reasoning";
   if (!trace && part.type !== "text") {
    continue;
   }
   const last = runs.at(-1);
   if (last?.trace === trace) {
    last.parts.push(part);
   } else {
    runs.push({ trace, parts: [part] });
   }
  }
  return runs;
 }
</script>
{#snippet thinkingLine(running: boolean)}
 <Trace.Line status={running ? "running" : undefined}>
  <Trace.Icon>
   <BrainIcon />
  </Trace.Icon>
  <Trace.Title>{running ? "Thinking" : "Thought"}</Trace.Title>
 </Trace.Line>
{/snippet}
{#snippet thinkingTrace(id: string, text: string, running: boolean)}
 {#if text.length === 0}
  {@render thinkingLine(running)}
 {:else}
  <Trace.Collapsible
   open={thinkingOpen[id] ?? running}
   onOpenChange={(open) => (thinkingOpen[id] = open)}
  >
   <Trace.CollapsibleTrigger>{@render thinkingLine(running)}</Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent class="whitespace-pre-wrap">
    {text}
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
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
   {@const live = chat.status === "streaming" && message === chat.messages.at(-1)}
   <Message.Root>
    <Message.Content class="gap-4">
     {#each groupParts(message.parts) as run, runIndex (runIndex)}
      {#if run.trace}
       <Trace.Root>
        {#each run.parts as part, index (index)}
         {#if part.type === "reasoning"}
          {@render thinkingTrace( `${message.id}-${runIndex}-${index}`,
           part.text,
           live && part.state === "streaming"
          )}
         {/if}
        {/each}
       </Trace.Root>
      {:else}
       {#each run.parts as part, index (`${runIndex}-${index}`)}
        {#if part.type === "text"}
         <p>{part.text}</p>
        {/if}
       {/each}
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
     thinkingOpen = {};
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

See [Reasoning](https://shadcn-svelte.com/docs/ai-elements/reasoning) for more examples.

## [Tool](#tool)

Render tool parts from the AI SDK. Map the tool part as in [Tool](https://shadcn-svelte.com/docs/ai-elements/tool#states).

```svelte
<script lang="ts">
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import { Chat } from "@ai-sdk/svelte";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import type { DynamicToolUIPart, UIMessage } from "ai";
 const script = createChat()
  .user("Which package managers are installed?")
  .assistant(({ writer }) => {
   writer
    .tool("runCommand", {
     dynamic: true,
     input: { command: "node --version" },
    })
    .sleep(900)
    .output({ stdout: "v24.18.0" });
   writer
    .tool("runCommand", {
     dynamic: true,
     input: { command: "npm --version" },
    })
    .sleep(900)
    .output({ stdout: "11.6.2" });
   writer
    .tool("runCommand", {
     dynamic: true,
     input: { command: "pnpm --version" },
    })
    .sleep(900)
    .error("command not found: pnpm");
   writer.text("Node 24 and npm 11 are installed. pnpm is not.");
  });
 const initialMessages = script.get(0);
 const transport = script.transport({ delayMs: 20 });
 const chat = new Chat({ messages: initialMessages, transport });
 const nextMessage = $derived(script.next(chat.messages));
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
 function groupParts(parts: UIMessage["parts"]) {
  const runs: { trace: boolean; parts: UIMessage["parts"] }[] = [];
  for (const part of parts) {
   const trace = part.type === "dynamic-tool";
   if (!trace && part.type !== "text") {
    continue;
   }
   const last = runs.at(-1);
   if (last?.trace === trace) {
    last.parts.push(part);
   } else {
    runs.push({ trace, parts: [part] });
   }
  }
  return runs;
 }
</script>
{#snippet toolTrace(part: DynamicToolUIPart, live: boolean)}
 {@const command = (part.input as { command?: string } | undefined)?.command}
 {#if part.state === "output-available" || part.state === "output-error"}
  {@const failed = part.state === "output-error"}
  <Trace.Collapsible>
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
      code={failed ? part.errorText : (part.output as { stdout: string }).stdout}
     />
    </CodeBlock.Root>
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
 {:else if part.state === "output-denied"}
  <Trace.Line>
   <Trace.Icon>
    <TerminalIcon />
   </Trace.Icon>
   <Trace.Title>Denied {command}</Trace.Title>
  </Trace.Line>
 {:else}
  <Trace.Line status={live ? "running" : "error"}>
   <Trace.Icon>
    <TerminalIcon />
   </Trace.Icon>
   <Trace.Title>
    {live ? "Running" : "Failed to run"}
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
   {@const live = chat.status === "streaming" && message === chat.messages.at(-1)}
   <Message.Root>
    <Message.Content class="gap-4">
     {#each groupParts(message.parts) as run, runIndex (runIndex)}
      {#if run.trace}
       <Trace.Root>
        {#each run.parts as part, index (part.type === "dynamic-tool" ? part.toolCallId : index)}
         {#if part.type === "dynamic-tool"}
          {@render toolTrace(part, live)}
         {/if}
        {/each}
       </Trace.Root>
      {:else}
       {#each run.parts as part, index (`${runIndex}-${index}`)}
        {#if part.type === "text"}
         <p>{part.text}</p>
        {/if}
       {/each}
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

See [Tool](https://shadcn-svelte.com/docs/ai-elements/tool) for more examples.

## [Accessibility](#accessibility) `Trace` adds no roles of its own. Each line gets its semantics from the element that wraps it.

- A `Trace.Line` on its own is a `span` . It is read as text and is not a tab stop.
- Wrap it in a `Trace.CollapsibleTrigger` and it becomes a button with `aria-expanded` . Wrap it in a link, or in the trigger for a dialog or sheet, and it takes the keyboard and focus behavior of that element.
- `Trace.Icon` is hidden from assistive tech, so `Trace.Title` is the accessible name. Write it as a sentence that says what happened, like "Edited trace.svelte", not just "trace.svelte".
- When a link opens a new tab, add "(opens in a new tab)" to the title with `sr-only` .
- Status is shown with color and motion, so put it in the title too. Write "Running pnpm build" while it runs and "Failed to run pnpm build" when it errors.  
- The shimmer on a running title stops when the reader prefers reduced motion. The title still says what is happening.  
- Inside a [Message Scroller](https://shadcn-svelte.com/docs/components/message-scroller)
  , each line is announced once when it is added.
- `Trace.CollapsibleContent` mutes its text. If you put a block with a muted background inside it, give the block `text-foreground` so it keeps its contrast.
  [Code Block](https://shadcn-svelte.com/docs/components/code-block)
  sets its own text color.

## [API Reference](#api-reference)

### [Trace.Root](#traceroot)

A list of rows. It also styles any trigger or link that wraps a `Trace.Line`.

| Prop                   | Type            | Default | Description                                             |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the list. | ### [Trace.Line](#traceline)

One line: an icon and a title. It is a span, so it is not a button or a tab stop. Wrap it in a trigger or a link to make it do something.

| Prop                    | Type                                       | Default | Description                                             |
| ----------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `status` | `"running" \| "error" \| "pending"` | -       | The state of the work the line reports.                 |
| `class`  | `string`                            | -       | Additional classes to apply to the line. | ### [Trace.Icon](#traceicon)

A decorative icon slot, hidden from assistive tech. Before the title it names the action; after it, it is the indicator.

| Prop                   | Type            | Default | Description                                                  |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the icon slot. | ### [Trace.Title](#tracetitle)

One sentence on one line. It truncates and shimmers while the line is running.

| Prop                   | Type            | Default | Description                                              |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the title. | ### [Trace.Description](#tracedescription)

Secondary text after the title, such as a count or a duration. It does not truncate.

| Prop                   | Type            | Default | Description                                                    |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the description. | ### [Trace.Collapsible](#tracecollapsible)

A row that expands. It accepts the props of [`Collapsible`](https://shadcn-svelte.com/docs/components/collapsible).

| Prop                          | Type                             | Default        | Description                                            |
| ----------------------------------------------------------- | -------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| `open`         | `boolean`                 | `false` | The open state. Bindable.                              |
| `onOpenChange` | `(open: boolean) => void` | -              | Called when the open state changes.                    |
| `class`        | `string`                  | -              | Additional classes to apply to the row. | ### [Trace.CollapsibleTrigger](#tracecollapsibletrigger)

The button that opens and closes the row. Put a `Trace.Line` inside it. It adds a chevron after the line.

| Prop                   | Type            | Default | Description                                                |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the trigger. | ### [Trace.CollapsibleContent](#tracecollapsiblecontent)

The detail of a row that expands.

| Prop                   | Type            | Default | Description                                                |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the content. |