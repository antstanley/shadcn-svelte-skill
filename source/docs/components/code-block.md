# Code Block

Displays code, terminal output and diffs with an optional header, line numbers and a copy button.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

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

View Code `CodeBlock` displays code, terminal output, logs and diffs. It has a header with a title and actions, line numbers, wrapping, diff and highlighted lines, and a small size for tool output in a [Trace](https://shadcn-svelte.com/docs/components/trace).

Syntax highlighting is optional and lives in a separate hook, so a block that only shows plain output stays small.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add code-block
```

```bash
npx shadcn-svelte@latest add code-block
```

```bash
bun x shadcn-svelte@latest add code-block
``` `code-block` also installs `useHighlightedCode` for [syntax highlighting](#syntax-highlighting).

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
</script>
```

```svelte
<CodeBlock.Root>
  <CodeBlock.Header>
    <CodeBlock.Title>Terminal</CodeBlock.Title>
    <CodeBlock.Actions>
      <CodeBlock.CopyButton value={output} />
    </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content code={output} />
</CodeBlock.Root>
```

## [Composition](#composition)

```text
CodeBlock.Root
 CodeBlock.Header
    CodeBlock.Title
    CodeBlock.Actions
        CodeBlock.CopyButton
 CodeBlock.Actions (floating, when there is no header)
 CodeBlock.Content
    CodeBlock.Line
 CodeBlock.Footer
``` `CodeBlock.Content` takes a `code` string or a list of `CodeBlock.Line` children. Use lines when you need line variants or highlighted tokens. Each `CodeBlock.Line` takes its own `code`: a string, or the tokens of a highlighted line.

## [Features](#features)

- **It streams cheaply.** A `code` string renders as one text node, and the highlighter tokenizes only the new lines as code arrives.
- **It copies cleanly.** Line numbers and diff markers are left out of a selection, and blank lines survive the copy.
- **It reads left to right.** The content is always `dir="ltr"` . The header follows the page direction.
- **It highlights without WASM.** `useHighlightedCode` uses Shiki's JavaScript engine, loads each language on first use and renders ANSI colors in terminal output.
- **It fits where code shows up.** Use it in a message, a Trace line, Tabs or a Dialog.
- **It scrolls by keyboard.** The content is focusable, and floating actions show on focus as well as on hover.

## [Basic](#basic)

Pass a string to the `code` prop of `CodeBlock.Content`. It renders as one text node, so it stays cheap while output streams.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const output = `$ pnpm build
> next build
  Compiled successfully in 4.2s
  Generating static pages (12/12)
Route (app)                Size  First Load JS
  /                    1.9 kB         112 kB
  /_not-found           993 B         103 kB
  /api/chat             141 B         102 kB`;
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Content code={output} />
 </CodeBlock.Root>
</div>
```

View Code

## [Header](#header) `CodeBlock.Header` holds a `CodeBlock.Title` and `CodeBlock.Actions`. `CodeBlock.CopyButton` copies its `value`.

```svelte
<script lang="ts">
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const command = "pnpm add ai @ai-sdk/react zod";
 const output = `$ ${command}
Packages: +14
Progress: resolved 412, reused 398, downloaded 14, added 14, done
Done in 2.8s using pnpm v10.18.0`;
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>
    <TerminalIcon />
    Terminal
   </CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={command} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content code={output} />
 </CodeBlock.Root>
</div>
```

View Code

A long title truncates. To link the title to a file, wrap `CodeBlock.Title` in an anchor.

```svelte
<CodeBlock.Header>
  <a href="/files/route.ts">
    <CodeBlock.Title>app/api/chat/route.ts</CodeBlock.Title>
  </a>
</CodeBlock.Header>
```

## [Actions](#actions) `CodeBlock.Actions` holds any number of buttons. For a wrap toggle, keep the state yourself and pass it to `wrap`.

```svelte
<script lang="ts">
 import DownloadIcon from "@lucide/svelte/icons/download";
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import WrapTextIcon from "@lucide/svelte/icons/text-wrap";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 const output = `$ pnpm lint
apps/web/components/message-list.tsx
  18:22  error  'messages' is possibly 'undefined'. Add a guard before calling map  @typescript-eslint/no-unsafe-call
  42:7   warning  React Hook React.useEffect has a missing dependency: 'scrollToBottom'  react-hooks/exhaustive-deps
 2 problems (1 error, 1 warning)`;
 function download(value: string, filename: string) {
  const url = URL.createObjectURL(new Blob([value], { type: "text/plain" }));
  const link = document.createElement("a");
  link.href = url;
  link.download = filename;
  link.click();
  URL.revokeObjectURL(url);
 }
 let wrap = $state(true);
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>
    <TerminalIcon />
    Terminal
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
     onclick={() => download(output, "lint.log")}
    >
     <DownloadIcon />
    </Button>
    <CodeBlock.CopyButton value={output} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content {wrap} code={output} />
 </CodeBlock.Root>
</div>
```

View Code

```svelte
<script lang="ts">
  let wrap = $state(false);
</script>
<CodeBlock.Actions>
  <Button
    variant="ghost"
    size="icon-xs"
    aria-label="Wrap lines"
    aria-pressed={wrap}
    onclick={() => (wrap = !wrap)}
  >
    <WrapTextIcon />
  </Button>
  <CodeBlock.CopyButton value={output} />
</CodeBlock.Actions>
<CodeBlock.Content {wrap} code={output} />
```

## [Floating Actions](#floating-actions)

Without a header, put `CodeBlock.Actions` directly inside `CodeBlock.Root`. The actions float at the top end and stay hidden until the block is hovered or focused. They always show on touch screens.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const output = `$ pnpm add ai @ai-sdk/react zod
Progress: resolved 412, reused 398, downloaded 14, added 14, done
dependencies:
+ @ai-sdk/react 3.0.12
+ ai 6.0.12
+ zod 4.1.12
Done in 2.8s using pnpm v10.18.0`;
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Actions>
   <CodeBlock.CopyButton value={output} />
  </CodeBlock.Actions>
  <CodeBlock.Content code={output} />
 </CodeBlock.Root>
</div>
```

View Code

## [Line Numbers](#line-numbers)

Add `lineNumbers` to `CodeBlock.Content`. A `code` string is split into lines, and the numbers are not copied with a selection.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const code = `{
  "name": "chat",
  "private": true,
  "scripts": {
    "dev": "next dev",
    "build": "next build"
  }
}`;
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Content lineNumbers {code} />
 </CodeBlock.Root>
</div>
```

View Code

## [Start Line](#start-line)

Set `startLine` to number lines from a given line, for a snippet from the middle of a file. The gutter grows to fit the widest number.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 const code = `  if (!session) {
    redirect("/login")
  }
  const projects = await db.project.findMany({
    where: { ownerId: session.user.id },
    orderBy: { updatedAt: "desc" },
  })
  return <ProjectList projects={projects} />
}`;
 const lines = useHighlightedCode(
  () => code,
  () => "tsx"
 );
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>app/dashboard/page.tsx</CodeBlock.Title>
  </CodeBlock.Header>
  <CodeBlock.Content lineNumbers startLine={995}>
   {#each lines.current as line, index (index)}
    <CodeBlock.Line code={line} />
   {/each}
  </CodeBlock.Content>
 </CodeBlock.Root>
</div>
```

View Code

## [Wrap](#wrap)

Long lines scroll by default. Add `wrap` to wrap them, which suits tool output and error messages. To let the reader toggle it, see [Actions](#actions).

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const output = `Error: The model "anthropic/claude-sonnet-4.5" returned an error: Request too large. The prompt is 212,431 tokens and the context window is 200,000 tokens. Remove some messages or summarize the conversation and try again.`;
</script>
<div class="flex w-full max-w-md flex-col gap-4">
 <CodeBlock.Root>
  <CodeBlock.Content code={output} />
 </CodeBlock.Root>
 <CodeBlock.Root>
  <CodeBlock.Content wrap code={output} />
 </CodeBlock.Root>
</div>
```

View Code

## [Highlighted Lines](#highlighted-lines)

Render each line as a `CodeBlock.Line` and set `variant="highlighted"` on the lines to call out.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const code = `export default {
  experimental: {
    reactCompiler: true,
    viewTransition: true,
  },
  images: {
    remotePatterns: [{ hostname: "avatars.githubusercontent.com" }],
  },
}`;
 const highlighted = [2, 3];
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Content lineNumbers>
   {#each code.split("\n") as line, index (index)}
    <CodeBlock.Line variant={highlighted.includes(index) ? "highlighted" : "default"}
     >{line}</CodeBlock.Line
    >
   {/each}
  </CodeBlock.Content>
 </CodeBlock.Root>
</div>
```

View Code

## [Diff](#diff)

Set `variant="added"` or `variant="removed"` on a `CodeBlock.Line`. Each one adds a `+` or `` marker.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const patch = ` export function Greeting({ name }: { name: string }) {
-  return <p>Hello, {name}</p>
+  return <p className="text-sm text-muted-foreground">
+    Hello, {name}!
+  </p>
 }`;
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
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>components/greeting.tsx</CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={patch} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content>
   {#each patch.split("\n") as line, index (index)}
    <CodeBlock.Line variant={getVariant(line)}>{line.slice(1)}</CodeBlock.Line>
   {/each}
  </CodeBlock.Content>
 </CodeBlock.Root>
</div>
```

View Code

## [Height](#height)

Cap the height with a `max-h-*` class on `CodeBlock.Content`. The content scrolls inside the block.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const logs = Array.from(
  { length: 40 },
  (_, index) => `[${String(index + 1).padStart(2, "0")}] GET /api/chat 200 in ${12 + ((index * 7) % 40)}ms` ).join("\n");
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>Logs</CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={logs} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content class="max-h-48 scroll-fade-y" code={logs} />
 </CodeBlock.Root>
</div>
```

View Code `CodeBlock.Content` fades its edges with [`scroll-fade`](https://shadcn-svelte.com/docs/utils/scroll-fade) as it scrolls: left and right by default, top and bottom when it wraps. Add `scroll-fade-y` to a capped block that does not wrap.

## [Show More](#show-more) `CodeBlock.Footer` is a slot below the content. For Show More, cap the content while it is collapsed and put a ghost `xs` `Button` in the footer.

```svelte
<script lang="ts">
 import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 import { Button } from "$lib/components/ui/button/index.js";
 const code = `"use client"
import * as React from "react"
import { useChat } from "@ai-sdk/react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
export function Chat() {
  const [input, setInput] = React.useState("")
  const { messages, sendMessage, status } = useChat()
  return (
    <div className="flex flex-col gap-4">
      {messages.map((message) => (
        <div key={message.id}>
          {message.parts.map((part, index) =>
            part.type === "text" ? <p key={index}>{part.text}</p> : null
          )}
        </div>
      ))}
      <form
        onSubmit={(event) => {
          event.preventDefault()
          sendMessage({ text: input })
          setInput("")
        }}
      >
        <Input value={input} onChange={(event) => setInput(event.target.value)} />
        <Button disabled={status !== "ready"}>Send</Button>
      </form>
    </div>
  )
}`;
 const id = $props.id();
 let expanded = $state(false);
 const lines = useHighlightedCode(
  () => code,
  () => "tsx"
 );
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>components/chat.tsx</CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={code} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content
   {id}
   lineNumbers
   class={expanded ? undefined : "max-h-64 scroll-fade-y overflow-y-hidden"}
  >
   {#each lines.current as line, index (index)}
    <CodeBlock.Line code={line} />
   {/each}
  </CodeBlock.Content>
  <CodeBlock.Footer class="justify-center">
   <Button
    variant="ghost"
    size="xs"
    aria-expanded={expanded}
    aria-controls={id}
    onclick={() => (expanded = !expanded)}
   >
    <ChevronDownIcon class="transition-transform in-aria-expanded:rotate-180" />
    {expanded ? "Show less" : "Show more"}
   </Button>
  </CodeBlock.Footer>
 </CodeBlock.Root>
</div>
```

View Code

```svelte
<script lang="ts">
  let expanded = $state(false);
  const id = $props.id();
</script>
<CodeBlock.Content
  {id}
  class={expanded ? undefined : "max-h-64 overflow-y-hidden scroll-fade-y"}
  {code}
/>
<CodeBlock.Footer class="justify-center">
  <Button
    variant="ghost"
    size="xs"
    aria-expanded={expanded}
    aria-controls={id}
    onclick={() => (expanded = !expanded)}
  >
    {expanded ? "Show less" : "Show more"}
  </Button>
</CodeBlock.Footer>
```

### [Max Height](#max-height)

To keep a long block from taking over the page, raise the cap instead of removing it. The expanded content scrolls, and the edges fade as you scroll.

```svelte
<script lang="ts">
 import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 import { Button } from "$lib/components/ui/button/index.js";
 const code = `"use client"
import * as React from "react"
import { useChat } from "@ai-sdk/react"
import { Button } from "@/components/ui/button"
import { Input } from "@/components/ui/input"
export function Chat() {
  const [input, setInput] = React.useState("")
  const { messages, sendMessage, status } = useChat()
  return (
    <div className="flex flex-col gap-4">
      {messages.map((message) => (
        <div key={message.id}>
          {message.parts.map((part, index) =>
            part.type === "text" ? <p key={index}>{part.text}</p> : null
          )}
        </div>
      ))}
      <form
        onSubmit={(event) => {
          event.preventDefault()
          sendMessage({ text: input })
          setInput("")
        }}
      >
        <Input value={input} onChange={(event) => setInput(event.target.value)} />
        <Button disabled={status !== "ready"}>Send</Button>
      </form>
    </div>
  )
}`;
 const id = $props.id();
 let expanded = $state(false);
 const lines = useHighlightedCode(
  () => code,
  () => "tsx"
 );
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>components/chat.tsx</CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={code} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content
   {id}
   lineNumbers
   class={expanded ? "max-h-96 scroll-fade-y" : "max-h-64 scroll-fade-y overflow-y-hidden"}
  >
   {#each lines.current as line, index (index)}
    <CodeBlock.Line code={line} />
   {/each}
  </CodeBlock.Content>
  <CodeBlock.Footer class="justify-center">
   <Button
    variant="ghost"
    size="xs"
    aria-expanded={expanded}
    aria-controls={id}
    onclick={() => (expanded = !expanded)}
   >
    <ChevronDownIcon class="transition-transform in-aria-expanded:rotate-180" />
    {expanded ? "Show less" : "Show more"}
   </Button>
  </CodeBlock.Footer>
 </CodeBlock.Root>
</div>
```

View Code

## [Size](#size)

Use `size="sm"` for tool and [Trace](#trace) output. It has tighter padding and `text-xs` text.

```svelte
<script lang="ts">
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const output = `$ pnpm add ai @ai-sdk/react zod
Progress: resolved 412, reused 398, downloaded 14, added 14, done
Done in 2.8s using pnpm v10.18.0`;
</script>
<div class="flex w-full max-w-md flex-col gap-4">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>
    <TerminalIcon />
    Terminal
   </CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={output} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content wrap code={output} />
 </CodeBlock.Root>
 <CodeBlock.Root size="sm">
  <CodeBlock.Header>
   <CodeBlock.Title>
    <TerminalIcon />
    Terminal
   </CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={output} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content wrap code={output} />
 </CodeBlock.Root>
</div>
```

View Code

## [Destructive](#destructive)

Use `variant="destructive"` for errors and failed output.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 const error = `TypeError: Cannot read properties of undefined (reading 'map')
    at MessageList (components/message-list.tsx:18:22)
    at renderWithHooks (react-dom.development.js:16305:18)`;
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root variant="destructive">
  <CodeBlock.Header>
   <CodeBlock.Title>Error</CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={error} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content wrap code={error} />
 </CodeBlock.Root>
</div>
```

View Code

## [Trace](#trace)

Put a `CodeBlock.Root` with `size="sm"` in `Trace.CollapsibleContent` for tool and terminal output. Add `wrap` and a `max-h-64` class to `CodeBlock.Content` so long output wraps and scrolls inside the trace. The block sets its own text color, so `Trace.CollapsibleContent` does not mute it.

```svelte
<script lang="ts">
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 const output = `$ node --version
v24.18.0`;
 const error = `$ pnpm dev
Error: listen EADDRINUSE: address already in use :::3000
    at Server.setupListenHandle [as _listen2] (node:net:1908:16)`;
</script>
<div class="w-full max-w-md">
 <Trace.Root>
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
     <CodeBlock.Content wrap class="max-h-64" code={output} />
    </CodeBlock.Root>
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
  <Trace.Collapsible open>
   <Trace.CollapsibleTrigger>
    <Trace.Line status="error">
     <Trace.Icon>
      <TerminalIcon />
     </Trace.Icon>
     <Trace.Title>Failed to run pnpm dev</Trace.Title>
    </Trace.Line>
   </Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent>
    <CodeBlock.Root size="sm" variant="destructive">
     <CodeBlock.Content wrap class="max-h-64" code={error} />
    </CodeBlock.Root>
   </Trace.CollapsibleContent>
  </Trace.Collapsible>
 </Trace.Root>
</div>
```

View Code

See [Tool](https://shadcn-svelte.com/docs/ai-elements/tool), [Terminal](https://shadcn-svelte.com/docs/ai-elements/terminal) and [Stack Trace](https://shadcn-svelte.com/docs/ai-elements/stack-trace) for more examples.

## [Tabs](#tabs)

Show several files with [Tabs](https://shadcn-svelte.com/docs/components/tabs), one `CodeBlock.Root` in each `Tabs.Content`.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Tabs from "$lib/components/ui/tabs/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 const files = [
  {
   id: "route",
   title: "app/api/chat/route.ts",
   language: "ts",
   code: `import { streamText } from "ai"
export async function POST(request: Request) {
  const { messages } = await request.json()
  const result = streamText({ model: "anthropic/claude-sonnet-4.5", messages })
  return result.toUIMessageStreamResponse()
}`,
  },
  {
   id: "chat",
   title: "components/chat.tsx",
   language: "tsx",
   code: `"use client"
import { useChat } from "@ai-sdk/react"
export function Chat() {
  const { messages } = useChat()
  return <MessageList messages={messages} />
}`,
  },
  {
   id: "env",
   title: ".env.local",
   language: "bash",
   code: "AI_GATEWAY_API_KEY=your-api-key",
  },
];
 const lines = files.map((file) =>
  useHighlightedCode(
   () => file.code,
   () => file.language
  )
 );
</script>
<Tabs.Root value="route" class="w-full max-w-md">
 <Tabs.List>
  {#each files as file (file.id)}
   <Tabs.Trigger value={file.id}>{file.title.split("/").at(-1)}</Tabs.Trigger>
  {/each}
 </Tabs.List>
 {#each files as file, fileIndex (file.id)}
  <Tabs.Content value={file.id}>
   <CodeBlock.Root>
    <CodeBlock.Header>
     <CodeBlock.Title>{file.title}</CodeBlock.Title>
     <CodeBlock.Actions>
      <CodeBlock.CopyButton value={file.code} />
     </CodeBlock.Actions>
    </CodeBlock.Header>
    <CodeBlock.Content lineNumbers>
     {#each lines[fileIndex].current as line, index (index)}
      <CodeBlock.Line code={line} />
     {/each}
    </CodeBlock.Content>
   </CodeBlock.Root>
  </Tabs.Content>
 {/each}
</Tabs.Root>
```

View Code

## [Message](#message)

Put a `CodeBlock.Root` between paragraphs inside a [Message](https://shadcn-svelte.com/docs/components/message).

```svelte
<script lang="ts">
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 const code = `import { streamText } from "ai"
export async function POST(request: Request) {
  const { messages } = await request.json()
  const result = streamText({
    model: "anthropic/claude-sonnet-4.5",
    messages,
  })
  return result.toUIMessageStreamResponse()
}`;
 const lines = useHighlightedCode(
  () => code,
  () => "ts"
 );
</script>
<div class="flex w-full max-w-md flex-col gap-4 text-sm">
 <Message.Root align="end">
  <Message.Content>
   <Bubble.Root variant="muted">
    <Bubble.Content>How do I stream a response?</Bubble.Content>
   </Bubble.Root>
  </Message.Content>
 </Message.Root>
 <Message.Root>
  <Message.Content class="gap-3">
   <p>Create a route handler that returns the stream:</p>
   <CodeBlock.Root>
    <CodeBlock.Header>
     <CodeBlock.Title>app/api/chat/route.ts</CodeBlock.Title>
     <CodeBlock.Actions>
      <CodeBlock.CopyButton value={code} />
     </CodeBlock.Actions>
    </CodeBlock.Header>
    <CodeBlock.Content>
     {#each lines.current as line, index (index)}
      <CodeBlock.Line code={line} />
     {/each}
    </CodeBlock.Content>
   </CodeBlock.Root>
   <p>The client reads it with useChat.</p>
  </Message.Content>
 </Message.Root>
</div>
```

View Code

## [Syntax Highlighting](#syntax-highlighting) `useHighlightedCode` highlights with [Shiki](https://shiki.style). Its `current` property has one entry per line. Pass each one to the `code` prop of a `CodeBlock.Line`.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 const code = `{
  "location": "San Francisco",
  "temperature": 18,
  "unit": "celsius",
  "conditions": ["fog", "wind"]
}`;
 const lines = useHighlightedCode(
  () => code,
  () => "json"
 );
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>getWeather output</CodeBlock.Title>
  </CodeBlock.Header>
  <CodeBlock.Content>
   {#each lines.current as line, index (index)}
    <CodeBlock.Line code={line} />
   {/each}
  </CodeBlock.Content>
 </CodeBlock.Root>
</div>
```

View Code

```svelte
<script lang="ts">
  import { useHighlightedCode } from "$lib/hooks/use-highlighted-code.svelte.js";
  const lines = useHighlightedCode(
    () => code,
    () => "json"
  );
</script>
<CodeBlock.Root>
  <CodeBlock.Content>
    {#each lines.current as line, index (index)}
      <CodeBlock.Line code={line} />
    {/each}
  </CodeBlock.Content>
</CodeBlock.Root>
```

Shiki uses its JavaScript regex engine, so there is no WASM to load.

### [Languages](#languages)

Each language loads the first time it is used. Edit the list in `lib/highlighter.ts`. A language that is not in the list renders as plain text.

```svelte
<script lang="ts">
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 const samples = [
  {
   language: "css",
   title: "app/globals.css",
   code: `@import "tailwindcss";
:root {
  --radius: 0.625rem;
}`,
  },
  {
   language: "python",
   title: "main.py",
   code: `def greet(name: str) -> str:
    return f"Hello, {name}!"`,
  },
  {
   language: "text",
   title: "notes.txt",
   code: "A language that is not in the list renders as plain text.",
  },
];
 const lines = samples.map((sample) =>
  useHighlightedCode(
   () => sample.code,
   () => sample.language
  )
 );
</script>
<div class="flex w-full max-w-md flex-col gap-4">
 {#each samples as sample, sampleIndex (sample.language)}
  <CodeBlock.Root>
   <CodeBlock.Header>
    <CodeBlock.Title>{sample.title}</CodeBlock.Title>
   </CodeBlock.Header>
   <CodeBlock.Content>
    {#each lines[sampleIndex].current as line, index (index)}
     <CodeBlock.Line code={line} />
    {/each}
   </CodeBlock.Content>
  </CodeBlock.Root>
 {/each}
</div>
```

View Code

The list ships with `bash`, `css`, `diff`, `html`, `javascript`, `json`, `jsx`, `markdown`, `python`, `sql`, `svelte`, `tsx`, `typescript` and `yaml`, plus aliases such as `ts`, `js`, `sh` and `yml`.

### [Terminal Output](#terminal-output)

Pass `"ansi"` as the language to render the colors in terminal output. Without it, escape codes show as text.

```svelte
<script lang="ts">
 import TerminalIcon from "@lucide/svelte/icons/terminal";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 const output = `$ pnpm test
[32m[39m src/format.test.ts [2m(4 tests)[22m
[32m[39m src/parse.test.ts [2m(7 tests)[22m
[31m[39m src/stream.test.ts [2m(3 tests | 1 failed)[22m
[31mAssertionError: expected 'hello' to be 'hello world'[39m
Tests  [31m1 failed[39m | [32m13 passed[39m (14)`;
 // eslint-disable-next-line no-control-regex
 const plain = output.replace(/[[d;]*m/g, "");
 const lines = useHighlightedCode(
  () => output,
  () => "ansi"
 );
</script>
<div class="w-full max-w-md">
 <CodeBlock.Root>
  <CodeBlock.Header>
   <CodeBlock.Title>
    <TerminalIcon />
    Terminal
   </CodeBlock.Title>
   <CodeBlock.Actions>
    <CodeBlock.CopyButton value={plain} />
   </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content wrap>
   {#each lines.current as line, index (index)}
    <CodeBlock.Line code={line} />
   {/each}
  </CodeBlock.Content>
 </CodeBlock.Root>
</div>
```

View Code

ANSI colors do not carry from one line to the next.

### [Server Rendering](#server-rendering) `highlightCode` is async and returns plain data, so you can call it in a `load` function. Shiki then stays out of the client bundle.

src/routes/+page.server.ts

```ts
import { highlightCode } from "$lib/highlighter.js";
const code = `export function add(a: number, b: number) {
  return a + b;
}`;
export async function load() {
  return {
    lines: (await highlightCode(code, "ts")) ?? code.split("\n"),
  };
}
```

src/routes/+page.svelte

```svelte
<script lang="ts">
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  let { data } = $props();
</script>
<CodeBlock.Root>
  <CodeBlock.Content lineNumbers>
    {#each data.lines as line, index (index)}
      <CodeBlock.Line code={line} />
    {/each}
  </CodeBlock.Content>
</CodeBlock.Root>
```

### [Streaming](#streaming)

While the code streams, the hook tokenizes only the new lines, starting where the last line left off. Lines that did not change keep the same tokens, so Svelte skips them.

```svelte
<script lang="ts">
 import RotateCcwIcon from "@lucide/svelte/icons/rotate-ccw";
 import { onDestroy } from "svelte";
 import * as CodeBlock from "$lib/components/ui/code-block/index.js";
 import { useHighlightedCode } from "$lib/components/hooks/use-highlighted-code.svelte.js";
 import { Button } from "$lib/components/ui/button/index.js";
 const blocks: {
  title?: string;
  language: string;
  code: string;
  lineNumbers?: boolean;
  highlight?: number[];
  diff?: boolean;
 }[] = [
  {
   title: "hooks/use-debounce.ts",
   language: "ts",
   lineNumbers: true,
   code: `export function useDebounce<T>(value: T, delay = 300) {
  const [debounced, setDebounced] = React.useState(value)
  React.useEffect(() => {
    const timeout = setTimeout(() => setDebounced(value), delay)
    return () => clearTimeout(timeout)
  }, [value, delay])
  return debounced
}`,
  },
  {
   language: "bash",
   code: "pnpm dlx shadcn@latest add code-block",
  },
  {
   title: "components/search.tsx",
   language: "tsx",
   lineNumbers: true,
   diff: true,
   code: ` export function Search() {
   const [query, setQuery] = React.useState("")
-  const results = useSearch(query)
+  const debounced = useDebounce(query, 300)
+  const results = useSearch(debounced)
   return <SearchResults results={results} />
 }`,
  },
  {
   title: "app/api/chat/route.ts",
   language: "ts",
   lineNumbers: true,
   highlight: [5, 6, 7, 8],
   code: `import { streamText } from "ai"
export async function POST(request: Request) {
  const { messages } = await request.json()
  const result = streamText({
    model: "anthropic/claude-sonnet-4.5",
    messages,
  })
  return result.toUIMessageStreamResponse()
}`,
  },
  {
   title: ".env.local",
   language: "bash",
   code: "AI_GATEWAY_API_KEY=your-api-key",
  },
 ];
 // Where each block starts in the stream.
 const offsets = blocks.map((_, index) =>
  blocks.slice(0, index).reduce((total, block) => total + block.code.length, 0)
 );
 const total = blocks.reduce((sum, block) => sum + block.code.length, 0);
 let length = $state(total);
 let interval: ReturnType<typeof setInterval> | undefined;
 function replay() {
  clearInterval(interval);
  length = 0;
  interval = setInterval(() => {
   length = Math.min(length + 3, total);
   if (length >= total) {
    clearInterval(interval);
   }
  }, 16);
 }
 onDestroy(() => clearInterval(interval));
 const streamed = blocks.map((block, index) => {
  const code = () => block.code.slice(0, Math.max(0, length - offsets[index])); const rows = () => code().split("\n");
  // A diff row starts with +, - or a space. The marker is not part of the code. const source = () =>
   block.diff
    ? rows()
      .map((row) => row.slice(1))
      .join("\n")
    : code();
  const lines = useHighlightedCode(source, () => block.language);
  return {
   get rows() {
    return rows();
   },
   get source() {
    return source();
   },
   get lines() {
    return lines.current;
   },
  };
 });
 function getVariant(block: (typeof blocks)[number], rows: string[], index: number) {
  if (block.diff) {
   if (rows[index]?.startsWith("+")) {
    return "added";
   }
   if (rows[index]?.startsWith("-")) {
    return "removed";
   }
   return "default";
  }
  return block.highlight?.includes(index) ? "highlighted" : "default";
 }
</script>
<div class="flex w-full max-w-md flex-col gap-4">
 {#each blocks as block, blockIndex (block.code)}
  {#if length > offsets[blockIndex]}
   {@const stream = streamed[blockIndex]}
   <CodeBlock.Root>
    {#if block.title}
     <CodeBlock.Header>
      <CodeBlock.Title>{block.title}</CodeBlock.Title>
      <CodeBlock.Actions>
       <CodeBlock.CopyButton
        value={stream.source}
        disabled={length - offsets[blockIndex] < block.code.length} />
      </CodeBlock.Actions>
     </CodeBlock.Header>
    {/if}
    <CodeBlock.Content lineNumbers={block.lineNumbers}>
     {#each stream.lines as line, index (index)}
      <CodeBlock.Line variant={getVariant(block, stream.rows, index)} code={line} />
     {/each}
    </CodeBlock.Content>
   </CodeBlock.Root>
  {/if}
 {/each}
 <Button variant="outline" size="sm" class="self-start" disabled={length < total} onclick={replay}>
  <RotateCcwIcon />
  Replay
 </Button>
</div>
```

View Code

### [Markdown](#markdown)

Render the message with [svelte-streamdown](https://github.com/beynar/svelte-streamdown) and route fenced code to a `CodeBlock` with `components.code`. Inline code goes through the `codespan` snippet, so it stays inline.

````svelte
<script lang="ts">
 import { Chat } from "@ai-sdk/svelte";
 import { Streamdown } from "svelte-streamdown";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import MarkdownCodeBlock from "$lib/components/code-block/markdown-code-block.svelte";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { Button } from "$lib/components/ui/button/index.js";
 const response = `Wrap the value in a `useDebounce` hook. It returns the latest value once it stops changing for `delay` milliseconds.
```tsx
export function useDebounce<T>(value: T, delay = 300) {
  const [debounced, setDebounced] = React.useState(value)
  React.useEffect(() => {
    const timeout = setTimeout(() => setDebounced(value), delay)
    return () => clearTimeout(timeout)
  }, [value, delay])
  return debounced
}
```
Pass the debounced value to your fetch instead of the raw input.`;
 const script = createChat()
  .user("How do I debounce a search input in React?")
  .assistant(({ writer }) => {
   writer.text(response);
  });
 const transcript = script.get();
 const [question] = script.get(1);
 const transport = script.transport({ delayMs: 30 });
 const chat = new Chat({ messages: transcript, transport });
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
</script>
<div class="flex min-h-112 w-full max-w-md flex-col gap-4 py-6 text-sm">
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
    <Message.Content>
     <Streamdown
      content={getMessageText(message)}
      controls={false}
      components={{ code: MarkdownCodeBlock }}
      class="space-y-4 whitespace-normal [&>*:first-child]:mt-0 [&>*:last-child]:mb-0"
     >
      {#snippet codespan({ children })}
       <code class="rounded-sm bg-muted px-1 py-0.5 font-mono text-[0.9em]"
        >{@render children()}</code
       >
      {/snippet}
     </Streamdown>
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
````

View Code

The `code` component gets `incomplete`, which is `true` until the closing fence arrives. Use it to disable the copy button while the code is incomplete.

markdown-code-block.svelte

```svelte
<script lang="ts">
  import { useHighlightedCode } from "$lib/hooks/use-highlighted-code.svelte.js";
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  let {
    token,
    incomplete,
  }: { token: { text: string; lang?: string }; incomplete: boolean } =
    $props();
  const language = $derived(token.lang?.split(/s/)[0] ?? "");
  const lines = useHighlightedCode(
    () => token.text,
    () => language
  );
</script>
<CodeBlock.Root>
  <CodeBlock.Header>
    <CodeBlock.Title>{language || "text"}</CodeBlock.Title>
    <CodeBlock.Actions>
      <CodeBlock.CopyButton value={token.text} disabled={incomplete} />
    </CodeBlock.Actions>
  </CodeBlock.Header>
  <CodeBlock.Content>
    {#each lines.current as line, index (index)}
      <CodeBlock.Line code={line} />
    {/each}
  </CodeBlock.Content>
</CodeBlock.Root>
```

```svelte
<Streamdown
  {content}
  controls={false}
  components={{ code: MarkdownCodeBlock }}
/>
```

## [Accessibility](#accessibility)

- `CodeBlock.Content` is a `pre` with a `code` element and always sets `dir="ltr"` , so code reads left to right on an RTL page.
- `CodeBlock.Content` has `tabindex={0}` , so keyboard users can focus it and scroll it. Pass `tabindex={-1}` to remove the tab stop.
- Floating actions show when focus is inside the block, not only on hover, so keyboard users can reach them.  
- Line numbers are hidden from screen readers.  
- Diff lines carry a `+` or `` marker as well as a tint, so the change does not rely on color.
- `CodeBlock.CopyButton` is labelled "Copy", and a polite live region announces "Copied" after a successful copy.
- Give a wrap toggle `aria-pressed` so its state is announced.
- Give a Show More button `aria-expanded` and point `aria-controls` at the `id` of `CodeBlock.Content` .

## [API Reference](#api-reference)

### [CodeBlock.Root](#codeblockroot)

The surface that holds the header, the content and the footer.

| Prop                     | Type                                | Default            | Description                                                                          |
| ------------------------------------------------------ | ----------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- |
| `variant` | `"default" \| "destructive"` | `"default"` | The tone of the block.                                                               |
| `size`    | `"default" \| "sm"`          | `"default"` | `"sm"` has tighter padding and `text-xs` code, for tool output. |
| `class`   | `string`                     | -                  | Additional classes to apply to the block.                             | ### [CodeBlock.Header](#codeblockheader)

A row above the content for a title and actions.

| Prop                   | Type            | Default | Description                                               |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `class` | `string` | -       | Additional classes to apply to the header. | ### [CodeBlock.Title](#codeblocktitle)

A filename or a label, with an optional icon. It truncates.

| Prop                   | Type            | Default | Description                                              |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the title. | ### [CodeBlock.Actions](#codeblockactions)

Holds buttons at the end of the header. As a direct child of `CodeBlock.Root`, it floats.

| Prop                   | Type            | Default | Description                                                |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `class` | `string` | -       | Additional classes to apply to the actions. | ### [CodeBlock.CopyButton](#codeblockcopybutton)

A ghost icon button that copies `value` to the clipboard. It accepts the props of [`Button`](https://shadcn-svelte.com/docs/components/button).

| Prop                   | Type            | Default | Description                                               |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `value` | `string` | -       | Required. The text to copy.                               |
| `class` | `string` | -       | Additional classes to apply to the button. | ### [CodeBlock.Content](#codeblockcontent)

The `pre` that scrolls or wraps.

| Prop                         | Type             | Default        | Description                                                                                  |
| ---------------------------------------------------------- | ---------------------------------------------- | -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| `code`        | `string`  | -              | Plain text to render. When it is set, `children` is ignored.                   |
| `children`    | `Snippet` | -              | A list of `CodeBlock.Line`.                                                    |
| `wrap`        | `boolean` | `false` | Wrap long lines instead of scrolling.                                                        |
| `lineNumbers` | `boolean` | `false` | Number each line. A `code` string is split into lines.                         |
| `startLine`   | `number`  | `1`     | The number of the first line, when `lineNumbers` is set.                       |
| `tabindex`    | `number`  | `0`     | Makes the content focusable so it can be scrolled by keyboard.                               |
| `class`       | `string`  | -              | Additional classes to apply to the content, such as `max-h-72`. | ### [CodeBlock.Line](#codeblockline)

One line of code.

| Prop                     | Type                                                        | Default            | Description                                                                                            |
| ------------------------------------------------------ | ----------------------------------------------------------------------------------------- | ------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `variant` | `"default" \| "added" \| "removed" \| "highlighted"` | `"default"` | The state of the line.                                                                                 |
| `code`    | `string \| CodeBlockLineToken[]`                     | -                  | The line as plain text, or as highlighted tokens. When it is set, `children` is ignored. |
| `class`   | `string`                                             | -                  | Additional classes to apply to the line.                                                | ### [CodeBlock.Footer](#codeblockfooter)

A row below the content, such as for a Show More button.

| Prop                   | Type            | Default | Description                                               |
| ---------------------------------------------------- | --------------------------------------------- | ------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| `class` | `string` | -       | Additional classes to apply to the footer. | ### [useHighlightedCode](#usehighlightedcode)

```ts
const lines = useHighlightedCode(
  () => code,
  () => language
);
```

Returns an object whose `current` property has one entry per line, for the `code` prop of `CodeBlock.Line`. Each entry is the line's tokens once highlighting finishes. It is a plain string until then, and for a language that is not in the list.

| Argument                  | Type                  | Description                                                                                            |
| ------------------------------------------------------- | --------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| `code`     | `() => string` | The code to highlight. A trailing newline is ignored.                                                  |
| `language` | `() => string` | A language or alias from `lib/highlighter.ts`, or `"ansi"`. |