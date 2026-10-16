# Context

How much of the context window the conversation has used.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as HoverCard from "$lib/components/ui/hover-card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Progress } from "$lib/components/ui/progress/index.js";
  const usage = {
    input: 8420,
    output: 1260,
    reasoning: 980,
    limit: 128000
  };
  const used = usage.input + usage.output + usage.reasoning;
  const percent = Math.round((used / usage.limit) * 100);
  function formatTokens(value: number) {
    if (value < 1000) {
      return String(value);
    }
    return `${(value / 1000).toFixed(1).replace(/.0$/, "")}k`;
  }
  const rows = [
    { label: "Input", value: usage.input },
    { label: "Output", value: usage.output },
    { label: "Reasoning", value: usage.reasoning }
 ];
</script>
<div class="flex justify-center py-12">
  <HoverCard.Root openDelay={10} closeDelay={100}>
    <HoverCard.Trigger>
      {#snippet child({ props })}
        <Button {...props} variant="outline" size="sm">
          {percent}% context
        </Button>
      {/snippet}
    </HoverCard.Trigger>
    <HoverCard.Content class="flex w-64 flex-col gap-3">
      <div class="flex items-center justify-between gap-3 text-sm">
        <span class="font-medium">Context</span>
        <span class="text-muted-foreground">
          {formatTokens(used)} / {formatTokens(usage.limit)}
        </span>
      </div>
      <Progress value={percent} aria-label="Context used" />
      <div class="flex flex-col gap-1 text-sm">
        {#each rows as row (row.label)}
          <div class="flex justify-between gap-3">
            <span class="text-muted-foreground">{row.label}</span>
            <span>{formatTokens(row.value)}</span>
          </div>
        {/each}
      </div>
    </HoverCard.Content>
  </HoverCard.Root>
</div>
```

View Code

Context shows how much of the model's context window the conversation has used. It is a [Hover Card](https://shadcn-svelte.com/docs/components/hover-card) with a [Progress](https://shadcn-svelte.com/docs/components/progress) bar.

## [Installation](#installation)

Context is built with the [Hover Card](https://shadcn-svelte.com/docs/components/hover-card) and [Progress](https://shadcn-svelte.com/docs/components/progress) components.

```bash
pnpm dlx shadcn-svelte@latest add hover-card progress button
```

```bash
npx shadcn-svelte@latest add hover-card progress button
```

```bash
bun x shadcn-svelte@latest add hover-card progress button
```

## [Usage](#usage)

```svelte
<HoverCard.Root openDelay={10} closeDelay={100}>
  <HoverCard.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="outline" size="sm">
        {percent}% context
      </Button>
    {/snippet}
  </HoverCard.Trigger>
  <HoverCard.Content class="flex w-64 flex-col gap-3">
    <div class="flex items-center justify-between gap-3 text-sm">
      <span class="font-medium">Context</span>
      <span class="text-muted-foreground">
        {used} / {limit}
      </span>
    </div>
    <Progress value={percent} aria-label="Context used" />
  </HoverCard.Content>
</HoverCard.Root>
```

## [AI SDK](#ai-sdk)

Read usage from the metadata on the agent's message. `messageMetadata` runs when the stream finishes.

src/routes/api/chat/+server.ts

```ts
return result.toUIMessageStreamResponse({
  messageMetadata: ({ part }) => {
    if (part.type === "finish") {
      return { usage: part.totalUsage };
    }
  },
});
```

```ts
const usage = $derived(message.metadata?.usage);
const used = $derived((usage?.inputTokens ?? 0) + (usage?.outputTokens ?? 0));
const percent = $derived(Math.round((used / limit) * 100));
``` `limit` is the model's context window. The AI SDK does not send it, so set it from the model you use.