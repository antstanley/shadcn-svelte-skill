# Inline Citation

A source in the sentence that opens on hover.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as HoverCard from "$lib/components/ui/hover-card/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 type Source = {
  url: string;
  title: string;
  description: string;
 };
 const sources = {
  streaming: {
   url: "https://nextjs.org/docs/app/getting-started/linking-and-navigating#streaming",
   title: "Linking and Navigating",
   description: "How the App Router streams a route to the browser.",
  },
  suspense: {
   url: "https://react.dev/reference/react/Suspense",
   title: "<Suspense>",
   description: "Display a fallback until its children have finished loading.",
  },
  serverComponents: {
   url: "https://react.dev/reference/rsc/server-components",
   title: "Server Components",
   description: "Components that render ahead of time, on the server.",
  },
  loading: {
   url: "https://nextjs.org/docs/app/api-reference/file-conventions/loading",
   title: "loading.js",
   description: "Show an instant loading state for a route segment.",
  },
  chunked: {
   url: "https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Headers/Transfer-Encoding",
   title: "Transfer-Encoding",
   description: "Send a response as a series of chunks.",
  },
 } satisfies Record<string, Source>;
 function hostname(url: string) {
  return new URL(url).hostname.replace(/^www./, "");
 }
</script>
{#snippet citation(source: Source)}
 {@const host = hostname(source.url)}
 <HoverCard.Root openDelay={10} closeDelay={100}>
  <HoverCard.Trigger>
   {#snippet child({ props })}
    <Button {...props} variant="secondary" size="xs">
     {host}
    </Button>
   {/snippet}
  </HoverCard.Trigger>
  <HoverCard.Content class="flex w-64 flex-col gap-1">
   <div class="font-medium">{source.title}</div>
   <p class="text-muted-foreground">{source.description}</p>
   <a
    href={source.url}
    target="_blank"
    rel="noreferrer"
    class="text-xs text-muted-foreground underline-offset-4 hover:underline"
   >
    {host}
    <span class="sr-only"> (opens in a new tab)</span>
   </a>
  </HoverCard.Content>
 </HoverCard.Root>
{/snippet}
<div class="mx-auto flex max-w-sm flex-col gap-3 py-6 text-sm leading-relaxed">
 <p>
  Next.js streams a route in chunks, so the page shows up before every request finishes.
  {@render citation(sources.streaming)}
 </p>
 <p>
  Wrap a slow part of the page in a Suspense boundary and React sends the fallback first. When the
  data resolves, the finished HTML streams into the same response and replaces the fallback, with
  no extra request from the browser.
  {@render citation(sources.suspense)}
  Server Components help here, because their code never ships to the browser.
  {@render citation(sources.serverComponents)}
 </p>
 <p>
  A loading.tsx file does the same for a whole route segment.
  {@render citation(sources.loading)}
  It all runs over chunked transfer encoding, so there is nothing extra to set up.
  {@render citation(sources.chunked)}
 </p>
</div>
```

View Code

Inline Citation is a source that sits in the sentence it supports. It is a [Hover Card](https://shadcn-svelte.com/docs/components/hover-card) on a [Button](https://shadcn-svelte.com/docs/components/button).

To show a list of sources after the reply, use [Sources](https://shadcn-svelte.com/docs/ai-elements/sources).

## [Installation](#installation)

Inline Citation is built with the [Hover Card](https://shadcn-svelte.com/docs/components/hover-card) and [Button](https://shadcn-svelte.com/docs/components/button) components.

```bash
pnpm dlx shadcn-svelte@latest add hover-card button
```

```bash
npx shadcn-svelte@latest add hover-card button
```

```bash
bun x shadcn-svelte@latest add hover-card button
```

## [Usage](#usage)

```svelte
<HoverCard.Root openDelay={10} closeDelay={100}>
  <HoverCard.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="secondary" size="xs">
        {hostname}
      </Button>
    {/snippet}
  </HoverCard.Trigger>
  <HoverCard.Content class="flex w-64 flex-col gap-1">
    <div class="font-medium">{title}</div>
    <a href={url} target="_blank" rel="noreferrer">
      {hostname}
      <span class="sr-only"> (opens in a new tab)</span>
    </a>
  </HoverCard.Content>
</HoverCard.Root>
```

## [AI SDK](#ai-sdk)

A `source-url` part is the citation. Set `sendSources: true` on `toUIMessageStreamResponse()`, or write the part yourself.

src/routes/api/chat/+server.ts

```ts
writer.write({
  type: "source-url",
  sourceId: "shadcn",
  url: "https://ui.shadcn.com",
  title: "shadcn/ui",
});
```

```ts
const sources = $derived(
  message.parts.filter((part) => part.type === "source-url")
);
``` `title` is optional. Fall back to the URL's hostname.