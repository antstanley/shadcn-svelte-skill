# Changelog

Latest updates and announcements.

## October 2026 - Trace, Code Block and AI Elements Today, we are releasing two new components, [**Trace**](https://shadcn-svelte.com/docs/components/trace) and [**Code Block**](https://shadcn-svelte.com/docs/components/code-block), and [**AI Elements**](https://shadcn-svelte.com/docs/ai-elements), a set of patterns for agentic interfaces built from shadcn-svelte components.

Trace and Code Block are available for Svelte across all eight styles.

## [Trace](#trace) `Trace` is a list of lines for the steps an agent takes. Each line has an icon, a title, and an optional description and status. A line can expand to show more detail, link to a page, or open a dialog or sheet, so every step looks and behaves the same in your interface.

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

View Code

Reasoning, tool calls, sources, plans and subagent runs all have the same shape: something the agent did, and what happened. Trace gives those steps a shared composition:

- `running` , `error` and `pending` states, with a shimmer while a step runs.
- Lines that expand, link out, or open a dialog, sheet, drawer or popover.  
- Nested lines, so a summary expands into steps and a step into its output.  
- Examples for reasoning, tool and source parts from the AI SDK using `@ai-sdk/svelte` .
- Keyboard and screen reader support from the link or trigger that wraps each line. ```bash
npx shadcn-svelte@latest add trace
```

## [Code Block](#code-block) `CodeBlock` displays code, terminal output, logs and diffs. It has a header with a title and actions, line numbers, wrapping, diff and highlighted lines, and a small size for tool output in a Trace.

```svelte
<script lang="ts">
 import DownloadIcon from "@lucide/svelte/icons/download";
 import FileCodeIcon from "@lucide/svelte/icons/file-code";
 import WrapTextIcon from "@lucide/svelte/icons/text-wrap";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 import { Button } from "$lib/components/ui/button/index.js";
 const code = `import { convertToModelMessages, streamText } from "ai"
import type { RequestHandler } from "./$types"
export const POST: RequestHandler = async ({ request }) => {
  const { messages } = await request.json()
  const result = streamText({
    model: "anthropic/claude-sonnet-4.5",
    system: "You are a helpful assistant. Answer in one short paragraph.",
    messages: await convertToModelMessages(messages),
  })
  return result.toUIMessageStreamResponse()
}`;
 function download(value: string, filename: string) {
  const url = URL.createObjectURL(new Blob([value], { type: "text/plain" }));
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
 }
 let wrap = $state(false);
 const lines = useHighlightedCode(
  () => code,
  () => "ts"
 );
</script>
<div class="w-full max-w-lg">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>
    <FileCodeIcon />
    src/routes/api/chat/+server.ts
   </CodeBlock.Title>
   <CodeBlock.Actions>
    <Button
     variant="ghost"
     size="icon-xs"
     aria-label="Wrap lines"
     aria-pressed={wrap}
     class="aria-pressed:text-foreground"
     onclick={() => (wrap = !wrap)}
    >
     <WrapTextIcon />
    </Button>
    <Button
     variant="ghost"
     size="icon-xs"
     aria-label="Download"
     onclick={() => download(code, "+server.ts")}
    >
     <DownloadIcon />
    </Button>
    <CodeBlock.CopyButton value={code} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content {wrap} lineNumbers>
   {#each lines.current as line, index (index)}
    <CodeBlock.Line
     variant={index >= 6 && index <= 10 ? "highlighted" : "default"}
     code={line}
    />
   {/each}
  </CodeBlock.Content>
 </CodeBlock.Root>
</div>
```

View Code

```bash
npx shadcn-svelte@latest add code-block
```

Syntax highlighting uses the separate `useHighlightedCode` hook, which is installed with `code-block`. Blocks that only show plain output can render it without highlighting.

## [Building agentic interfaces](#building-agentic-interfaces)

Trace and Code Block join the [components for chat interfaces](https://shadcn-svelte.com/docs/changelog/2026-10-chat-components) announced earlier this month. Together, they cover the pieces of an agentic interface:

- [Message Scroller](https://shadcn-svelte.com/docs/components/message-scroller) holds the thread. It anchors each turn, follows the reply while it streams and loads history without jumping.
- [Message](https://shadcn-svelte.com/docs/components/message) is one turn, with an avatar, a header and a footer for actions.
- [Bubble](https://shadcn-svelte.com/docs/components/bubble) holds what the person sends.
- [Trace](https://shadcn-svelte.com/docs/components/trace) shows the steps the agent takes inside a turn.
- [Code Block](https://shadcn-svelte.com/docs/components/code-block) shows the code, commands and output those steps produce.
- [Marker](https://shadcn-svelte.com/docs/components/marker) adds notes and dividers between turns.
- [Attachment](https://shadcn-svelte.com/docs/components/attachment) shows the files that come with a message.
- [Questionnaire](https://shadcn-svelte.com/docs/components/questionnaire) asks the person to clarify before the agent continues.

## [AI Elements](#ai-elements)

[AI Elements](https://shadcn-svelte.com/docs/ai-elements) are patterns for agentic interfaces built from these components. There is no package to install. Each pattern is a Svelte composition you copy into your project, and the code is yours.

````svelte
<script lang="ts">
 import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import GlobeIcon from "@lucide/svelte/icons/globe";
 import LoaderCircleIcon from "@lucide/svelte/icons/loader-circle";
 import MessageCircleDashedIcon from "@lucide/svelte/icons/message-circle-dashed";
 import PaperclipIcon from "@lucide/svelte/icons/paperclip";
 import PlusIcon from "@lucide/svelte/icons/plus";
 import RotateCwIcon from "@lucide/svelte/icons/rotate-cw";
 import TelescopeIcon from "@lucide/svelte/icons/telescope";
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import { Chat } from "@ai-sdk/svelte";
 import { prefersReducedMotion } from "svelte/motion";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import * as Empty from "$lib/components/ui/empty/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
 import * as MessageScroller from "$lib/components/ui/message-scroller/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import * as Tooltip from "$lib/components/ui/tooltip/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import Markdown from "$lib/components/markdown/markdown.svelte";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { MESSAGE_ANIMATIONS, type MessageAnimationPreset } from "$lib/message-animations.js";
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
 type ToolPart = Extract<ChatMessage["parts"][number], { type: "tool-runCommand" }>;
 const script = createChat<ChatMessage>()
  .user("Add a dark mode toggle to the settings page.")
  .sleep(600)
  .assistant(({ writer }) => {
   writer.reasoning(
    "I need to know how themes are set up before I add a toggle. If mode-watcher is already in the layout, the toggle only has to call setMode."
   );
   writer.sleep(400);
   writer
    .tool("runCommand", { input: { command: "rg -l ModeWatcher src/routes" } })
    .sleep(800)
    .output({ stdout: "src/routes/+layout.svelte" });
   writer.sleep(500);
   writer.text(`mode-watcher is already set up in `src/routes/+layout.svelte`, so the toggle only has to call `setMode`.
**Changes**
- Added `src/lib/components/mode-toggle.svelte` with a Light and Dark option.
- Put `<ModeToggle />` next to the Appearance heading in `src/routes/settings/+page.svelte`. ```ts
import { setMode } from "mode-watcher"
setMode("dark")
``` `);
  })
  .user("Make it follow the system setting by default.")
  .sleep(600)
  .assistant(({ writer }) => {
   writer.reasoning(
    "The default theme lives on the ModeWatcher. I should check what it is set to now."
   );
   writer.sleep(400);
   writer
    .tool("runCommand", {
     input: { command: "rg -n defaultMode src/routes/+layout.svelte" },
    })
    .sleep(800)
    .output({
     stdout: '12:  <ModeWatcher defaultMode="light" />',
    });
   writer.sleep(500);
   writer.text(`It was set to `light`. I updated the `ModeWatcher` in `src/routes/+layout.svelte`:
```svelte
<ModeWatcher defaultMode="system" />
```
New visitors now get the theme from their OS. The toggle also has a **System** option, so anyone who picked Light or Dark can switch back. `);
  })
  .user("Run the build before I ship it.")
  .sleep(600)
  .assistant(({ writer }) => {
   writer
    .tool("runCommand", { input: { command: "pnpm build" } })
    .sleep(1600)
    .output({
     stdout:
      "vite v8.1.5 building for production...\n\n Built in 4.2s\n Prerendered 12 pages",
    });
   writer.sleep(500);
   writer.text(`The build passes, so it is ready to ship.
- Compiled in **4.2s**.
- Generated all **12** static pages. `);
  });
 const initialMessages = script.get(0);
 const transport = script.transport({
  delayMs: 16,
  fallback: "This demo only knows the scripted turns. Press reset to start over.",
 });
 const chat = new Chat<ChatMessage>({ messages: initialMessages, transport });
 let draft = $state<string | null>(null);
 let form = $state<HTMLFormElement | null>(null);
 // The reader's choice for each reasoning row. Until they click, it follows `running`.
 let reasoningOpen = $state<Record<string, boolean>>({});
 const nextMessage = $derived(script.next(chat.messages));
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
 const text = $derived(draft ?? (nextMessage ? getMessageText(nextMessage) : ""));
 const canSend = $derived(text.trim().length > 0 && !busy);
 function onSubmit(event: SubmitEvent) {
  event.preventDefault();
  if (!canSend) {
   return;
  }
  if (draft === null && nextMessage) {
   void chat.sendMessage(nextMessage);
  } else {
   void chat.sendMessage({ text: text.trim() });
  }
  draft = null;
 }
 const enterPreset: MessageAnimationPreset = MESSAGE_ANIMATIONS["slide-up"];
 function enterMessage(node: HTMLElement) {
  if (prefersReducedMotion.current) return { duration: 0 };
  return enterPreset.transition(node);
 }
</script>
{#snippet reasoningRow(id: string, text: string, running: boolean)}
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
  <Trace.CollapsibleContent class="whitespace-pre-wrap">{text}</Trace.CollapsibleContent>
 </Trace.Collapsible>
{/snippet}
{#snippet toolRow(part: ToolPart, streaming: boolean)}
 {@const command = part.input?.command}
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
<MessageScroller.Provider>
 <div
  class="relative flex w-full flex-col gap-4 [[data-slot=preview]:has(&)]:bg-background [[data-slot=preview]:has(&)>div]:p-0!"
 >
  <div class="flex h-200 w-full flex-col gap-4">
   <div class="flex items-start justify-between gap-4 p-8 pb-4">
    <div class="flex flex-col gap-1">
     <div class="font-medium">New Thread</div>
     <div class="text-sm text-muted-foreground">Ask the agent to change your code.</div>
    </div>
    <Tooltip.Root>
     <Tooltip.Trigger>
      {#snippet child({ props })}
       <Button
        {...props}
        variant="outline"
        size="icon"
        aria-label="Reset conversation"
        onclick={() => {
         chat.messages = initialMessages;
         draft = null;
         reasoningOpen = {};
        }}
        disabled={busy}
       >
        <RotateCwIcon />
       </Button>
      {/snippet}
     </Tooltip.Trigger>
     <Tooltip.Content>
      <p>Reset</p>
     </Tooltip.Content>
    </Tooltip.Root>
   </div>
   <div class="min-h-0 flex-1">
    {#if chat.messages.length === 0}
     <Empty.Root class="h-full">
      <Empty.Header>
       <Empty.Media variant="icon">
        <MessageCircleDashedIcon />
       </Empty.Media>
       <Empty.Title>What should we build?</Empty.Title>
       <Empty.Description>
        The agent can read your code, run commands and make changes. Press send to start.
       </Empty.Description>
      </Empty.Header>
     </Empty.Root>
    {:else}
     <MessageScroller.Root>
      <MessageScroller.Viewport>
       <MessageScroller.Content aria-busy={busy} class="gap-6 px-8 py-0">
        {#each chat.messages as message (message.id)}
         {#if message.role === "user"}
          <MessageScroller.Item messageId={message.id} scrollAnchor>
           {#snippet child({ props })}
            <div {...props} in:enterMessage|global>
             <Message.Root align="end">
              <Message.Content>
               <Bubble.Root align="end" variant="muted">
                <Bubble.Content>{getMessageText(message)}</Bubble.Content>
               </Bubble.Root>
              </Message.Content>
             </Message.Root>
            </div>
           {/snippet}
          </MessageScroller.Item>
         {:else}
          {@const streaming = busy && message === chat.messages.at(-1)}
          {@const hasSteps = message.parts.some(
           (part) => part.type === "reasoning" || part.type === "tool-runCommand"
          )}
          {@const reply = getMessageText(message)}
          <MessageScroller.Item messageId={message.id}>
           <Message.Root>
            <Message.Content class="gap-3">
             {#if hasSteps}
              <Trace.Root>
               {#each message.parts as part, index (index)}
                {#if part.type === "reasoning"}
                 {@render reasoningRow( `${message.id}-${index}`,
                  part.text,
                  part.state === "streaming"
                 )}
                {:else if part.type === "tool-runCommand"}
                 {@render toolRow(part, streaming)}
                {/if}
               {/each}
              </Trace.Root>
             {/if}
             {#if reply}
              <Markdown content={reply} />
             {/if}
            </Message.Content>
           </Message.Root>
          </MessageScroller.Item>
         {/if}
        {/each}
       </MessageScroller.Content>
      </MessageScroller.Viewport>
      <MessageScroller.Button />
     </MessageScroller.Root>
    {/if}
   </div>
   <div class="p-8 pt-0">
    <form bind:this={form} onsubmit={onSubmit} class="w-full">
     <InputGroup.Root>
      <InputGroup.Textarea
       bind:value={() => text, (value) => (draft = value ?? "")}
       placeholder="Ask the agent..."
       aria-label="Message"
       class="min-h-14"
       onkeydown={(event) => {
        if (event.key === "Enter" && !event.shiftKey) {
         event.preventDefault();
         form?.requestSubmit();
        }
       }}
      />
      <InputGroup.Addon align="block-end" class="pt-1">
       <DropdownMenu.Root>
        <DropdownMenu.Trigger>
         {#snippet child({ props })}
          <InputGroup.Button
           {...props}
           aria-label="Add context"
           type="button"
           size="icon-sm"
           variant="outline"
          >
           <PlusIcon />
          </InputGroup.Button>
         {/snippet}
        </DropdownMenu.Trigger>
        <DropdownMenu.Content align="start" side="top" class="w-44">
         <DropdownMenu.Item>
          <PaperclipIcon />
          Add Photos & Files
         </DropdownMenu.Item>
         <DropdownMenu.Separator />
         <DropdownMenu.Item>
          <TelescopeIcon />
          Deep Research
         </DropdownMenu.Item>
         <DropdownMenu.Item>
          <GlobeIcon />
          Web Search
         </DropdownMenu.Item>
        </DropdownMenu.Content>
       </DropdownMenu.Root>
       <InputGroup.Button
        type="submit"
        variant="default"
        size="icon-sm"
        disabled={!canSend}
        class="ml-auto"
       >
        <ArrowUpIcon />
        <span class="sr-only">Send</span>
       </InputGroup.Button>
      </InputGroup.Addon>
     </InputGroup.Root>
    </form>
   </div>
  </div>
 </div>
</MessageScroller.Provider>
````

View Code

There are 21 patterns, from [Chat](https://shadcn-svelte.com/docs/ai-elements/chat) and [Prompt Input](https://shadcn-svelte.com/docs/ai-elements/prompt-input) to [Reasoning](https://shadcn-svelte.com/docs/ai-elements/reasoning), [Tool](https://shadcn-svelte.com/docs/ai-elements/tool), [Plan](https://shadcn-svelte.com/docs/ai-elements/plan) and [Subagent](https://shadcn-svelte.com/docs/ai-elements/subagent). The AI SDK examples use `@ai-sdk/svelte`. The patterns read message parts, so you can also use them with another source of messages.

Every page is also available as Markdown, so you can point your coding agent at it:

Prompt

```txt
Add the Reasoning pattern from https://shadcn-svelte.com/docs/ai-elements/reasoning.md to my Svelte chat.
```

## [Using existing AI Elements components](#using-existing-ai-elements-components)

If you already use [Svelte AI Elements](https://svelte-ai-elements.vercel.app/), you can keep the components in your project and adopt these patterns one at a time.

Each pattern page lists the shadcn-svelte components it uses and includes Svelte code and AI SDK message-part examples. Copy the pattern you need, then adapt your existing wrappers and message handling to its composition.

[Read the Docs](https://shadcn-svelte.com/docs/ai-elements)

## October 2026 - Questionnaire Today, we're releasing [**Questionnaire**](https://shadcn-svelte.com/docs/components/questionnaire), a new component for multi-step question flows. Use it for agent clarification prompts, onboarding, surveys, intake forms, and configuration.

Questionnaire is available for Svelte across all eight styles.

```svelte
<script lang="ts">
 import { toast } from "svelte-sonner";
 import * as Questionnaire from "$lib/components/ui/questionnaire/index.js";
 const items = [
  {
   choices: [{ value: "tool-calls" }, { value: "approvals" }, { value: "handoffs" }],
   name: "direction",
   required: true,
  },
  {
   choices: [
    { value: "progress" },
    { value: "decisions" },
    { value: "risks" },
    { value: "next-step" },
  ],
   name: "signals",
  },
  {
   choices: [{ value: "now" }, { value: "next-cycle" }, { value: "backlog" }],
   name: "timing",
   required: true,
  },
 ] as const;
 function handleSubmit(event: SubmitEvent) {
  event.preventDefault();
  const formData = new FormData(event.currentTarget as HTMLFormElement);
  const answers = {
   direction: formData.get("direction"),
   signals: formData.getAll("signals"),
   timing: formData.get("timing"),
  };
  toast("Agent plan saved", {
   description: `Direction: ${answers.direction ?? "None"}  Progress signals: ${answers.signals.join(", ") || "None"}  Timing: ${answers.timing ?? "None"}`,
  });
 }
</script>
<Questionnaire.Root
 class="mx-auto max-w-md"
 defaultItem="direction"
 {items}
 shortcuts="letters"
 onSubmit={handleSubmit}
>
 <Questionnaire.Progress />
 <Questionnaire.Item name="direction" required>
  <Questionnaire.Title>What should the agent build next?</Questionnaire.Title>
  <Questionnaire.Description>
   Choose a direction or describe another task.
  </Questionnaire.Description>
  <Questionnaire.Choices>
   <Questionnaire.Choice value="tool-calls">
    <span class="font-medium">Tool call timeline</span>
    <span class="text-muted-foreground">Show what the agent ran and what came back.</span>
   </Questionnaire.Choice>
   <Questionnaire.Choice value="approvals">
    <span class="font-medium">Approval checkpoints</span>
    <span class="text-muted-foreground">Ask before sensitive or destructive actions.</span>
   </Questionnaire.Choice>
   <Questionnaire.Choice value="handoffs">
    <span class="font-medium">Sub-agent handoffs</span>
    <span class="text-muted-foreground">
     Make delegated work and results easier to follow.
    </span>
   </Questionnaire.Choice>
   <Questionnaire.Input
    aria-label="Another agent feature"
    placeholder="Describe another feature"
   />
  </Questionnaire.Choices>
  <Questionnaire.Error />
 </Questionnaire.Item>
 <Questionnaire.Item name="signals" multiple>
  <Questionnaire.Title>What should every progress update include?</Questionnaire.Title>
  <Questionnaire.Description
   >Select all that apply, or skip this question.</Questionnaire.Description
  >
  <Questionnaire.Choices>
   <Questionnaire.Choice value="progress">Progress</Questionnaire.Choice>
   <Questionnaire.Choice value="decisions">Decisions</Questionnaire.Choice>
   <Questionnaire.Choice value="risks">Risks</Questionnaire.Choice>
   <Questionnaire.Choice value="next-step">Next step</Questionnaire.Choice>
  </Questionnaire.Choices>
  <Questionnaire.Error />
 </Questionnaire.Item>
 <Questionnaire.Item name="timing" required>
  <Questionnaire.Title>When should work begin?</Questionnaire.Title>
  <Questionnaire.Description
   >Choose when the agent should begin the work.</Questionnaire.Description
  >
  <Questionnaire.Choices>
   <Questionnaire.Choice value="now">Start now</Questionnaire.Choice>
   <Questionnaire.Choice value="next-cycle">Next development cycle</Questionnaire.Choice>
   <Questionnaire.Choice value="backlog">Add it to the backlog</Questionnaire.Choice>
  </Questionnaire.Choices>
  <Questionnaire.Error />
 </Questionnaire.Item>
 <Questionnaire.Actions>
  <Questionnaire.Previous />
  <Questionnaire.Skip />
  <Questionnaire.Next>Next</Questionnaire.Next>
  <Questionnaire.Submit>Save plan</Questionnaire.Submit>
 </Questionnaire.Actions>
</Questionnaire.Root>
```

View Code

## [Features](#features)

- Single and multiple selection with native radios and checkboxes.  
- Freeform answers alongside fixed choices.  
- Explicit skipping for optional questions.  
- Previous, next, submit, and custom progress controls.  
- Required and custom validation.  
- Controlled navigation, saved defaults, and conditional questions.  
- Keyboard navigation with optional letter or number shortcuts.  
- Native form serialization and server-rendered collection state.  
- Standalone, Card, and Dialog composition. ## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add questionnaire
```

```bash
npx shadcn-svelte@latest add questionnaire
```

```bash
bun x shadcn-svelte@latest add questionnaire
```

## [@shadcn-svelte/primitives](#shadcn-svelteprimitives)

Questionnaire is also available as an unstyled headless primitive in `@shadcn-svelte/primitives/questionnaire`. [Read the docs](https://shadcn-svelte.com/docs/components/questionnaire#unstyled) to learn more.

[View Questionnaire](https://shadcn-svelte.com/docs/components/questionnaire)

## More Updates

[October 2026 Components for Chat Interfaces](https://shadcn-svelte.com/docs/changelog/2026-10-chat-components)[September 2026 cn](https://shadcn-svelte.com/docs/changelog/2026-09-cn)[May 2026 Introducing Rhea](https://shadcn-svelte.com/docs/changelog/2026-05-rhea)[April 2026 Introducing Sera](https://shadcn-svelte.com/docs/changelog/2026-04-sera)[March 2026 Introducing Luma](https://shadcn-svelte.com/docs/changelog/2026-03-luma)[October 2025 New Components](https://shadcn-svelte.com/docs/changelog/2025-10-new-components)[June 2025 Calendar Components](https://shadcn-svelte.com/docs/changelog/2025-06-calendar)[May 2025 Tailwind v4 Support](https://shadcn-svelte.com/docs/changelog/2025-05-tailwind-v4)[March 2024 Introducing Blocks](https://shadcn-svelte.com/docs/changelog/2024-03-blocks)[February 2024 New Component Resizable](https://shadcn-svelte.com/docs/changelog/2024-02-resizable)[January 2024 New Components](https://shadcn-svelte.com/docs/changelog/2024-01-new-components)[December 2023 Calendar Components](https://shadcn-svelte.com/docs/changelog/2023-12-calendar)[November 2023 Toggle Group](https://shadcn-svelte.com/docs/changelog/2023-11-toggle-group)[October 2023 Command and Combobox](https://shadcn-svelte.com/docs/changelog/2023-10-command-combobox)