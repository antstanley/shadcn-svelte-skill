# Terminal

Displays a command the agent runs, with its output as it streams.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

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
  import type { UIMessage } from "ai";
  type ChatMessage = UIMessage<
    unknown,
    {
      terminal: { output: string };
    },
    {
      runCommand: {
        input: { command: string };
        output: { exitCode: number };
      };
    }
  >;
  type ToolPart = Extract<
    ChatMessage["parts"][number],
    { type: "tool-runCommand" }
  >;
  const COMMANDS = [
    {
      id: "lint",
      command: "pnpm lint",
      output: ["> acme-chat@0.1.0 lint", "> eslint ."]
    },
    {
      id: "test",
      command: "pnpm test",
      output: [
        "> acme-chat@0.1.0 test",
        "> vitest run",
        "",
        "  lib/ai.test.ts (6 tests) 41ms",
        "  components/chat.test.tsx (9 tests) 212ms",
        "",
        " Test Files  2 passed (2)",
        "      Tests  15 passed (15)"
     ]
    },
    {
      id: "build",
      command: "pnpm build",
      output: [
        "> acme-chat@0.1.0 build",
        "> next build",
        "",
        "    Next.js 16.3.0",
        "   Creating an optimized production build ...",
        "  Compiled successfully in 4.2s",
        "  Generating static pages (12/12)",
        "",
        "Route (app)                Size  First Load JS",
        "  /                     1.9 kB       112 kB",
        "  /api/chat              141 B       102 kB"
     ]
    }
  ];
  const script = createChat<ChatMessage>()
    .user("Run the checks, then build the app.")
    .assistant(({ writer }) => {
      for (const { id, command, output } of COMMANDS) {
        const tool = writer.tool("runCommand", {
          toolCallId: id,
          input: { command }
        });
        // The tool streams its output as a data part with the tool call's id.
        output.forEach((_, index) => {
          writer
            .data({
              type: "data-terminal",
              id,
              data: { output: output.slice(0, index + 1).join("\n") }
            })
            .sleep(200);
        });
        tool.output({ exitCode: 0 });
      }
      writer.text("Lint and tests pass, and the build compiled both routes.");
    });
  const transcript = script.get();
  const [question] = script.get(1);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat<ChatMessage>({ messages: transcript, transport });
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  // The reader's choice for each command. Until they click, it follows `running`.
  // Like `defaultOpen`, the last command of the initial transcript starts open.
  const lastCommand = transcript
    .at(-1)
    ?.parts.findLast(
      (part): part is ToolPart => part.type === "tool-runCommand"
    );
  let commandOpen = $state<Record<string, boolean>>(
    lastCommand ? { [lastCommand.toolCallId]: true } : {}
  );
  function getTitle(part: ToolPart, running: boolean) {
    const command = part.input?.command;
    if (part.state === "output-available") {
      return part.output.exitCode === 0
        ? `Ran ${command}` : `${command} exited with code ${part.output.exitCode}`;
    }
    return running ? `Running ${command}` : `Failed to run ${command}`;
  }
  function getOutput(message: ChatMessage, toolCallId: string) {
    for (const part of message.parts) {
      if (part.type === "data-terminal" && part.id === toolCallId) {
        return part.data.output;
      }
    }
    return "";
  }
</script>
{#snippet commandRow(part: ToolPart, output: string, streaming: boolean)}
  {@const running =
    streaming &&
    (part.state === "input-streaming" || part.state === "input-available")}
  {@const failed =
    !running &&
    (part.state !== "output-available" || part.output.exitCode !== 0)}
  <Trace.Collapsible
    open={commandOpen[part.toolCallId] ?? (running && output.length > 0)}
    onOpenChange={(open) => (commandOpen[part.toolCallId] = open)}
  >
    <Trace.CollapsibleTrigger>
      <Trace.Line status={running ? "running" : failed ? "error" : undefined}>
        <Trace.Icon>
          <TerminalIcon />
        </Trace.Icon>
        <Trace.Title>{getTitle(part, running)}</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <CodeBlock.Root size="sm">
        <CodeBlock.Content
          wrap
          class="max-h-64"
          code={part.state === "output-error" ? part.errorText : output}
        />
      </CodeBlock.Root>
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
      {@const tools = message.parts.filter(
        (part) => part.type === "tool-runCommand"
      )}
      {@const text = getMessageText(message)}
      <Message.Root>
        <Message.Content class="gap-4">
          {#if tools.length > 0}
            <Trace.Root>
              {#each tools as part (part.toolCallId)}
                {@render commandRow(
                  part,
                  getOutput(message, part.toolCallId),
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
        commandOpen = {};
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

Terminal is a shell command the agent runs, such as a lint, a test run or a build. The line shows the command, and its output streams in underneath while it runs.

Terminal is built with `Trace` with a `Trace.Collapsible` for each command.

## [Installation](#installation)

Terminal is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) and [Code Block](https://shadcn-svelte.com/docs/components/code-block) components.

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
        <Trace.Title>Ran pnpm build</Trace.Title>
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

## [Exit Code](#exit-code)

A command that exits with any code other than `0` failed. Set `status="error"`.

```svelte
<script lang="ts">
  import TerminalIcon from "@lucide/svelte/icons/terminal";
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  const LINT_OUTPUT = `> acme-chat@0.1.0 lint
> eslint .
app/api/chat/route.ts
  14:7  error  'model' is assigned a value but never used  no-unused-vars
components/chat.tsx
  42:5  error  React Hook useEffect has a missing dependency: 'messages'  react-hooks/exhaustive-deps
 2 problems (2 errors, 0 warnings)
 ELIFECYCLE  Command failed with exit code 1.`;
</script>
<Trace.Root class="max-w-sm">
  <Trace.Line>
    <Trace.Icon>
      <TerminalIcon />
    </Trace.Icon>
    <Trace.Title>Ran pnpm install</Trace.Title>
  </Trace.Line>
  <Trace.Collapsible open>
    <Trace.CollapsibleTrigger>
      <Trace.Line status="error">
        <Trace.Icon>
          <TerminalIcon />
        </Trace.Icon>
        <Trace.Title>pnpm lint exited with code 1</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <CodeBlock.Root size="sm">
        <CodeBlock.Content wrap class="max-h-64" code={LINT_OUTPUT} />
      </CodeBlock.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

View Code

| Command                              | `status`    | Title                                      |
| -------------------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------------- |
| Running                       | `"running"` | Running pnpm build                         |
| Exited with `0` | none               | Ran pnpm build                             |
| Exited with another code      | `"error"`   | pnpm lint exited with code 1 |

The command is a tool call, so its states map the same way as in [Tool](https://shadcn-svelte.com/docs/ai-elements/tool#states).

## [Open While Running](#open-while-running)

Open the line once the first output arrives, so the output is visible while the command runs. Leave it open or closed after that, as in [Trace](https://shadcn-svelte.com/docs/components/trace#open-state).

## [AI SDK](#ai-sdk)

A tool result arrives only once the command exits. To stream the output while it runs, write it from the tool as a data part with the tool call's id. The AI SDK replaces a data part that has the same id, so the output grows in place.

```ts
writer.write({
  type: "data-terminal",
  id: toolCallId,
  data: { output },
});
```

On the client, find the data part that matches each tool part.

```ts
function getOutput(message: ChatMessage, toolCallId: string) {
  for (const part of message.parts) {
    if (part.type === "data-terminal" && part.id === toolCallId) {
      return part.data.output;
    }
  }
  return "";
}
```

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).