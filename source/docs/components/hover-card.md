# Hover Card

For sighted users to preview content available behind a link.

[Docs](https://bits-ui.com/docs/components/link-preview)

[API Reference](https://bits-ui.com/docs/components/link-preview#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as HoverCard from "$lib/components/ui/hover-card/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<HoverCard.Root openDelay={10} closeDelay={100}>
 <HoverCard.Trigger class={buttonVariants({ variant: "link" })}>Hover Here</HoverCard.Trigger>
 <HoverCard.Content class="flex w-64 flex-col gap-0.5">
  <div class="font-semibold">@sveltejs</div>
  <div>Cybernetically enhanced web apps  created and maintained by @vercel.</div>
  <div class="mt-1 text-xs text-muted-foreground">Joined December 2021</div>
 </HoverCard.Content>
</HoverCard.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add hover-card
```

```bash
npx shadcn-svelte@latest add hover-card
```

```bash
bun x shadcn-svelte@latest add hover-card
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as HoverCard from "$lib/components/ui/hover-card/index.js";
</script>
```

```svelte
<HoverCard.Root>
  <HoverCard.Trigger>Hover</HoverCard.Trigger>
  <HoverCard.Content>
    SvelteKit - Web development, streamlined </HoverCard.Content>
</HoverCard.Root>
```

## [Trigger Delays](#trigger-delays)

Use `openDelay` and `closeDelay` on `HoverCard.Root` to control when the card opens and closes.

```svelte
<HoverCard.Root openDelay={100} closeDelay={200}>
  <HoverCard.Trigger>Hover</HoverCard.Trigger>
  <HoverCard.Content>Content</HoverCard.Content>
</HoverCard.Root>
```

## [Positioning](#positioning)

Use the `side` and `align` props on `HoverCard.Content` to control placement.

```svelte
<HoverCard.Root>
  <HoverCard.Trigger>Hover</HoverCard.Trigger>
  <HoverCard.Content side="top" align="start">Content</HoverCard.Content>
</HoverCard.Root>
```

## [Basic](#basic)

```svelte
<script lang="ts">
 import * as HoverCard from "$lib/components/ui/hover-card/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<HoverCard.Root openDelay={10} closeDelay={100}>
 <HoverCard.Trigger class={buttonVariants({ variant: "link" })}>Hover Here</HoverCard.Trigger>
 <HoverCard.Content class="flex w-64 flex-col gap-0.5">
  <div class="font-semibold">@sveltejs</div>
  <div>Cybernetically enhanced web apps  created and maintained by @vercel.</div>
  <div class="mt-1 text-xs text-muted-foreground">Joined December 2021</div>
 </HoverCard.Content>
</HoverCard.Root>
```

View Code

## [Sides](#sides)

```svelte
<script lang="ts">
 import * as HoverCard from "$lib/components/ui/hover-card/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
 import { cn } from "$lib/utils.js";
 const HOVER_CARD_SIDES = ["left", "top", "bottom", "right"] as const;
</script>
<div class="flex flex-wrap justify-center gap-2">
 {#each HOVER_CARD_SIDES as side (side)}
  <HoverCard.Root openDelay={100} closeDelay={100}>
   <HoverCard.Trigger class={cn(buttonVariants({ variant: "outline" }), "capitalize")}>
    {side}
   </HoverCard.Trigger>
   <HoverCard.Content {side}>
    <div class="flex flex-col gap-1">
     <h4 class="font-medium">Hover Card</h4>
     <p>This hover card appears on the {side} side of the trigger.</p>
    </div>
   </HoverCard.Content>
  </HoverCard.Root>
 {/each}
</div>
```

View Code