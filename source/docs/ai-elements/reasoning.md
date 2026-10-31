# Reasoning

Displays the agent's thinking as it streams.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { Chat } from "@ai-sdk/svelte";
 import * as Bubble from "$lib/components/ui/bubble/index.js";
 import * as Message from "$lib/components/ui/message/index.js";
 import * as Trace from "$lib/components/ui/trace/index.js";
 import { createChat, getMessageText } from "$lib/ai-sdk.js";
 import { Button } from "$lib/components/ui/button/index.js";
 const script = createChat()
  .user("Why is the checkout deploy so slow?")
  .assistant(({ writer }) => {
   writer.reasoning(
    "The deploy log has three phases. Install takes 38s and next build takes 52s, both normal for this repo.\n\nImage optimization takes 3m 50s. It reruns on every deploy because its cache key includes the commit hash, so the cache never hits.",
    { delayMs: 40 }
   );
   writer.sleep(400);
   writer.text(
    "Image optimization is the bottleneck. Key its cache on the lockfile and the image directory instead of the commit hash, and the deploy should take under two minutes."
   );
  });
 const transcript = script.get();
 const [question] = script.get(1);
 const transport = script.transport({ delayMs: 20 });
 const chat = new Chat({ messages: transcript, transport });
 const busy = $derived(chat.status === "submitted" || chat.status === "streaming");
 // The reader's choice for each reasoning row. Until they click, it follows `running`.
 // The transcript's rows start open, like `defaultOpen` when the chat is idle.
 function transcriptOpen() {
  const open: Record<string, boolean> = {};
  for (const message of transcript) {
   message.parts
    .filter((part) => part.type === "reasoning")
    .forEach((_, index) => (open[`${message.id}-${index}`] = true));
  }
  return open;
 }
 let reasoningOpen = $state<Record<string, boolean>>(transcriptOpen());
</script>
{#snippet reasoningRow(id: string, text: string, running: boolean)}
 {#snippet line()}
  <Trace.Line status={running ? "running" : undefined}>
   <Trace.Title>{running ? "Thinking" : "Thought for 5s"}</Trace.Title>
  </Trace.Line>
 {/snippet}
 {#if text.length === 0}
  {@render line()}
 {:else}
  <Trace.Collapsible
   open={reasoningOpen[id] ?? running}
   onOpenChange={(open) => (reasoningOpen[id] = open)}
  >
   <Trace.CollapsibleTrigger>{@render line()}</Trace.CollapsibleTrigger>
   <Trace.CollapsibleContent class="whitespace-pre-wrap">{text}</Trace.CollapsibleContent>
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
   {@const streaming = busy && message === chat.messages.at(-1)}
   {@const reasoning = message.parts.filter((part) => part.type === "reasoning")}
   {@const text = getMessageText(message)}
   <Message.Root>
    <Message.Content class="gap-4">
     {#if reasoning.length > 0}
      <Trace.Root>
       {#each reasoning as part, index (index)}
        {@render reasoningRow( `${message.id}-${index}`,
         part.text,
         streaming && part.state === "streaming"
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
    reasoningOpen = {};
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

Reasoning is a line for the agent's thinking. It reads "Thinking" and opens while the model thinks, then reads "Thought" and closes when it is done. The thinking itself sits inside, and the line can show how long it took.

Reasoning is built with `Trace` with a `Trace.Collapsible` for the thinking.

## [Installation](#installation)

Reasoning is built with the [Trace](https://shadcn-svelte.com/docs/components/trace) component.

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
  <Trace.Collapsible>
    <Trace.CollapsibleTrigger>
      <Trace.Line>
        <Trace.Icon>
          <CircleCheckIcon />
        </Trace.Icon>
        <Trace.Title>Thought</Trace.Title>
      </Trace.Line>
    </Trace.CollapsibleTrigger>
    <Trace.CollapsibleContent class="whitespace-pre-wrap">
      {text}
    </Trace.CollapsibleContent>
  </Trace.Collapsible>
</Trace.Root>
```

## [Duration](#duration)

The AI SDK does not time reasoning. Measure it on the server, send it as message metadata, and show it in a `Trace.Description` after the title.

```svelte
<script lang="ts">
 import CircleCheckIcon from "@lucide/svelte/icons/circle-check";
 import * as Trace from "$lib/components/ui/trace/index.js";
</script>
<Trace.Root class="max-w-sm">
 <Trace.Collapsible>
  <Trace.CollapsibleTrigger>
   <Trace.Line>
    <Trace.Icon>
     <CircleCheckIcon />
    </Trace.Icon>
    <Trace.Title>Thought</Trace.Title>
    <Trace.Description>12s</Trace.Description>
   </Trace.Line>
  </Trace.CollapsibleTrigger>
  <Trace.CollapsibleContent class="whitespace-pre-wrap">
   The build log shows install and compile finish in under a minute. Image optimization takes
   almost four, and it reruns on every deploy because the cache key includes the commit hash.
  </Trace.CollapsibleContent>
 </Trace.Collapsible>
</Trace.Root>
```

View Code

```svelte
<Trace.Line>
  <Trace.Icon>
    <CircleCheckIcon />
  </Trace.Icon>
  <Trace.Title>Thought</Trace.Title>
  <Trace.Description>{seconds}s</Trace.Description>
</Trace.Line>
```

## [AI SDK](#ai-sdk)

Render each `reasoning` part as a line. It starts as a plain `Trace.Line` and becomes a `Trace.Collapsible` once text arrives, so there is nothing to open before the model has written anything. It opens while the model thinks and closes when it finishes. If the person opens or closes it, their choice wins. See [Open State](https://shadcn-svelte.com/docs/components/trace#open-state).

```svelte
<script lang="ts">
  // The person's choice for each line. Until they click, it follows `running`.
  let reasoningOpen = $state<Record<string, boolean>>({});
</script>
{#snippet reasoningLine(id: string, text: string, running: boolean)}
  {#snippet line()}
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
  {/snippet}
  {#if text.length === 0}
    {@render line()}
  {:else}
    <Trace.Collapsible
      open={reasoningOpen[id] ?? running}
      onOpenChange={(open) => (reasoningOpen[id] = open)}
    >
      <Trace.CollapsibleTrigger>{@render line()}</Trace.CollapsibleTrigger>
      <Trace.CollapsibleContent class="whitespace-pre-wrap">
        {text}
      </Trace.CollapsibleContent>
    </Trace.Collapsible>
  {/if}
{/snippet}
```

```svelte
<Trace.Root>
  {#each message.parts.filter((part) => part.type === "reasoning") as part, index (index)}
    {@render reasoningLine( `${message.id}-${index}`,
      part.text,
      streaming && part.state === "streaming"
    )}
  {/each}
</Trace.Root>
```

Some models send several reasoning parts in one message. Each one is a line in the same `Trace`.

## [API Reference](#api-reference)

See [Trace](https://shadcn-svelte.com/docs/components/trace#api-reference).