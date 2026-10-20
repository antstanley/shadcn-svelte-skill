# Chain of Thought

Displays a summary that expands into the steps an agent took.

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
  import * as Bubble from "$lib/components/ui/bubble/index.js";
  import * as CodeBlock from "$lib/components/ui/code-block/index.js";
  import * as Message from "$lib/components/ui/message/index.js";
  import * as Trace from "$lib/components/ui/trace/index.js";
  import { createChat, getMessageText } from "$lib/ai-sdk.js";
  import { Badge } from "$lib/components/ui/badge/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import type { UIDataTypes, UIMessage } from "ai";
  import type { Snippet } from "svelte";
  type ChatMessage = UIMessage<
    unknown,
    UIDataTypes,
    {
      searchWeb: {
        input: { query: string };
        output: { results: { title: string; url: string }[] };
      };
      readBuildLog: {
        input: { deployment: string };
        output: { log: string };
      };
      searchCode: {
        input: { query: string };
        output: { files: string[] };
      };
    }
  >;
  type StepPart = Extract<
    ChatMessage["parts"][number],
    { type: "tool-searchWeb" | "tool-readBuildLog" | "tool-searchCode" }
  >;
  type StepStatus = "running" | "error" | undefined;
  const script = createChat<ChatMessage>()
    .user("Why is the checkout deploy so slow?")
    .assistant(({ writer }) => {
      writer
        .tool("readBuildLog", { input: { deployment: "dpl_8Kx2" } })
        .sleep(900)
        .output({
          log: "install    41s\ncompile    38s\nimages   3m 52s"
        });
      writer
        .tool("searchWeb", { input: { query: "next.js image cache key" } })
        .sleep(900)
        .output({
          results: [
            {
              title: "Image component | nextjs.org",
              url: "https://nextjs.org/docs/app/api-reference/components/image"
            },
            {
              title: "Build cache | vercel.com",
              url: "https://vercel.com/docs/deployments/troubleshoot-a-build"
            }
         ]
        });
      writer
        .tool("searchCode", { input: { query: "cacheKey" } })
        .sleep(900)
        .output({ files: ["next.config.ts", "scripts/optimize-images.ts"] });
      writer.text(
        "Image optimization takes almost four minutes because its cache key includes the commit hash. Key it on the image directory instead."
      );
    });
  const transcript = script.get();
  const [question] = script.get(1);
  const transport = script.transport({ delayMs: 20 });
  const chat = new Chat<ChatMessage>({ messages: transcript, transport });
  const busy = $derived(
    chat.status === "submitted" || chat.status === "streaming"
  );
  // The reader's choice for each summary. Until they click, it follows `running`.
  let summaryOpen = $state<Record<string, boolean>>({});
  function isStep(part: ChatMessage["parts"][number]): part is StepPart {
    return (
      part.type === "tool-searchWeb" ||
      part.type === "tool-readBuildLog" ||
      part.type === "tool-searchCode"
    );
  }
  function stepStatus(part: StepPart, streaming: boolean): StepStatus {
    return part.state === "output-available"
      ? undefined
      : part.state === "output-error" || !streaming
        ? "error"
        : "running";
  }
</script>
{#snippet statusIcon(status: StepStatus)}
  {#if status === "running"}
    <LoaderCircleIcon class="animate-spin" />
  {:else if status === "error"}
    <CircleAlertIcon />
  {:else}
    <CircleCheckIcon />
  {/if}
{/snippet}
{#snippet step(
  title: string,
  status: StepStatus,
  defaultOpen: boolean,
  children?: Snippet
)}
  {#snippet line()}
    <Trace.Line {status}>
      <Trace.Icon>
        {@render statusIcon(status)}
      </Trace.Icon>
      <Trace.Title>{title}</Trace.Title>
    </Trace.Line>
  {/snippet}
  {#if !children}
    {@render line()}
  {:else}
    <Trace.Collapsible open={defaultOpen}>
      <Trace.CollapsibleTrigger>{@render line()}</Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent>{@render children()}</Trace.CollapsibleContent>
    </Trace.Collapsible>
  {/if}
{/snippet}
{#snippet stepRow(part: StepPart, streaming: boolean)}
  {@const status = stepStatus(part, streaming)}
  {@const verb = (running: string, done: string, failed: string) =>
    status === "running" ? running : status === "error" ? failed : done}
  {@const hasContent =
    part.state === "output-error" || part.state === "output-available"}
  {#snippet error()}
    {#if part.state === "output-error"}
      <CodeBlock.Root size="sm" variant="destructive">
        <CodeBlock.Content wrap class="max-h-64" code={part.errorText} />
      </CodeBlock.Root>
    {/if}
  {/snippet}
  {#if part.type === "tool-searchWeb"}
    {#snippet results()}
      {#if part.state === "output-available"}
        <Trace.Root>
          {#each part.output.results as result, index (index)}
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
      {:else}
        {@render error()}
      {/if}
    {/snippet}
    {@render step( `${verb("Searching", "Searched", "Failed to search")} the web for ${part.input?.query}`,
      status,
      false,
      hasContent ? results : undefined
    )}
  {:else if part.type === "tool-readBuildLog"}
    {#snippet log()}
      {#if part.state === "output-available"}
        <CodeBlock.Root size="sm">
          <CodeBlock.Content wrap class="max-h-64" code={part.output.log} />
        </CodeBlock.Root>
      {:else}
        {@render error()}
      {/if}
    {/snippet}
    {@render step( `${verb("Reading", "Read", "Failed to read")} the build log for ${part.input?.deployment}`,
      status,
      true,
      hasContent ? log : undefined
    )}
  {:else}
    {#snippet files()}
      {#if part.state === "output-available"}
        <div class="flex flex-wrap gap-1.5">
          {#each part.output.files as file, index (index)}
            <Badge variant="secondary" class="font-mono">{file}</Badge>
          {/each}
        </div>
      {:else}
        {@render error()}
      {/if}
    {/snippet}
    {@render step( `${verb("Searching", "Searched", "Failed to search")} the code for ${part.input?.query}`,
      status,
      false,
      hasContent ? files : undefined
    )}
  {/if}
{/snippet}
{#snippet chainOfThought(
  id: string,
  steps: StepPart[],
  streaming: boolean,
  answering: boolean
)}
  {@const running = streaming && !answering}
  {@const failed = steps.filter((part) => part.state === "output-error").length}
  {@const status = running ? "running" : failed > 0 ? "error" : undefined}
  <Trace.Root>
    <Trace.Collapsible
      open={summaryOpen[id] ?? running}
      onOpenChange={(open) => (summaryOpen[id] = open)}
    >
      <Trace.CollapsibleTrigger>
        <Trace.Line {status}>
          <Trace.Icon>
            {@render statusIcon(status)}
          </Trace.Icon>
          <Trace.Title>
            {running
              ? "Researching"
              : `Researched in ${steps.length} steps${failed > 0 ? `, ${failed} failed` : ""}`}
          </Trace.Title>
        </Trace.Line>
      </Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent>
        <Trace.Root>
          {#each steps as part (part.toolCallId)}
            {@render stepRow(part, streaming)}
          {/each}
        </Trace.Root>
      </Trace.CollapsibleContent>
    </Trace.Collapsible>
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
      {@const steps = message.parts.filter(isStep)}
      {@const text = getMessageText(message)}
      <Message.Root>
        <Message.Content class="gap-4">
          {#if steps.length > 0}
            {@render chainOfThought(
              message.id,
              steps,
              streaming,
              text.length > 0
            )}
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
        summaryOpen = {};
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

Chain of Thought is a summary line that expands into the steps an agent took. The summary says what happened, like "Researched in 3 steps". The steps sit inside it, each one a line of its own.

Chain of Thought is built with `Trace` with a `Trace.Collapsible` for the summary.

## [Installation](#installation)

Chain of Thought is built with the [Trace](https://shadcn-svelte.com/docs/components/trace), [Code Block](https://shadcn-svelte.com/docs/components/code-block) and [Badge](https://shadcn-svelte.com/docs/components/badge) components.

```bash
pnpm dlx shadcn-svelte@latest add trace code-block badge
```

```bash
npx shadcn-svelte@latest add trace code-block badge
```

```bash
bun x shadcn-svelte@latest add trace code-block badge
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
          <CircleCheckIcon />
        </Trace.Icon>
        <Trace.Title>Researched in 3 steps</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent>
      <Trace.Root>
        <Trace.Line>
          <Trace.Icon>
            <CircleCheckIcon />
          </Trace.Icon>
          <Trace.Title>Read the build log for dpl_8Kx2</Trace.Title>
        </Trace.Line>
        <Trace.Line>
          <Trace.Icon>
            <CircleCheckIcon />
          </Trace.Icon>
          <Trace.Title
            >Searched the web for next.js image cache key</Trace.Title
          >
        </Trace.Line>
        <Trace.Line>
          <Trace.Icon>
            <CircleCheckIcon />
          </Trace.Icon>
          <Trace.Title>Searched the code for cacheKey</Trace.Title>
        </Trace.Line>
      </Trace.Root>
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [Steps](#steps)

Each step is a `Trace.Line`. Set its `status` and write the title in the matching tense.

| Step                     | `status`    | Title                                |
| -------------------------------------- | --------------------------------------- | ----------------------------------------------------------------------- |
| Running           | `"running"` | Searching for                       |
| Done, with detail | none               | Searched for                        |
| Done, links out   | none               | Read the Image component docs        |
| Failed            | `"error"`   | Failed to search for  |

## [Search Results](#search-results)

When a step runs a web search, show the results as a `Badge` for each hostname in the step's content.

```svelte
<Trace.CollapsibleContent class="flex flex-wrap gap-1.5">
  {#each results as result, index (index)}
    <Badge variant="secondary">
      {new URL(result.url).hostname}
    </Badge>
  {/each}
</Trace.CollapsibleContent>
```

## [AI SDK](#ai-sdk)

Render each tool part as a step. `running` is true while tool parts stream and before the reply starts. Set the summary's status and title from the steps. The summary opens while the steps run, as in [Trace](https://shadcn-svelte.com/docs/components/trace#open-state).

```svelte
<script lang="ts">
  let open = $state<boolean>();
  const running = $derived(streaming && !answering);
  const failed = $derived(
    steps.filter((part) => part.state === "output-error").length
  );
</script>
<Trace.Collapsible
  open={open ?? running}
  onOpenChange={(value) => (open = value)}
>
  <Trace.CollapsibleTrigger>
    <Trace.Line
      status={running ? "running" : failed > 0 ? "error" : undefined}
    >
      <Trace.Title>
        {running ? "Researching" : `Researched in ${steps.length} steps`}
      </Trace.Title>
    </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent>
    <Trace.Root>
      {#each steps as part (part.toolCallId)}
        {@render stepLine(part, streaming)}
      {/each}
    </Trace.Root>
  </Trace.CollapsibleContent>
</Trace.Collapsible>
``` `stepLine` renders one tool part as a `Trace.Line`, as in [Tool](https://shadcn-svelte.com/docs/ai-elements/tool#states).

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).