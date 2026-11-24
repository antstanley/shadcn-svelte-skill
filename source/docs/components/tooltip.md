# Tooltip

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

[Docs](https://bits-ui.com/docs/components/tooltip)

[API Reference](https://bits-ui.com/docs/components/tooltip#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as Tooltip from "$lib/components/ui/tooltip/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Tooltip.Provider>
 <Tooltip.Root>
  <Tooltip.Trigger class={buttonVariants({ variant: "outline" })}>Hover</Tooltip.Trigger>
  <Tooltip.Content>
   <p>Add to library</p>
  </Tooltip.Content>
 </Tooltip.Root>
</Tooltip.Provider>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add tooltip
```

```bash
npx shadcn-svelte@latest add tooltip
```

```bash
bun x shadcn-svelte@latest add tooltip
```

## [Usage](#usage)

The `Tooltip.Provider` component should be placed once in your root layout, wrapping all content that will contain tooltips. This ensures that only one tooltip within the provider can be open at a time.

src/routes/+layout.svelte

```svelte
<script lang="ts">
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
  let { children } = $props();
</script>
```

```svelte
<Tooltip.Provider>
  {@render children()}
</Tooltip.Provider>
```

Then use tooltips anywhere in your app:

```svelte
<script lang="ts">
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
</script>
<Tooltip.Root>
  <Tooltip.Trigger>Hover</Tooltip.Trigger>
  <Tooltip.Content>
    <p>Add to library</p>
  </Tooltip.Content>
</Tooltip.Root>
```

### [Nested Providers](#nested-providers)

You can nest providers to create groups with different settings. Tooltips use the closest ancestor provider. This is useful when you want instant tooltips in specific areas:

```svelte
<Tooltip.Provider delayDuration={0}>
</Tooltip.Provider>
```

## [Side](#side)

Use the `side` prop to change the position of the tooltip.

```svelte
<script lang="ts">
 import * as Tooltip from "$lib/components/ui/tooltip/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
 const sides = ["left", "top", "bottom", "right"] as const;
</script>
<div class="flex flex-wrap gap-2">
 {#each sides as side (side)}
  <Tooltip.Root>
   <Tooltip.Trigger class={buttonVariants({ variant: "outline", class: "w-fit capitalize" })}>
    {side}
   </Tooltip.Trigger>
   <Tooltip.Content {side}>
    <p>Add to library</p>
   </Tooltip.Content>
  </Tooltip.Root>
 {/each}
</div>
```

View Code

## [With Keyboard Shortcut](#with-keyboard-shortcut)

```svelte
<script lang="ts">
 import SaveIcon from "@lucide/svelte/icons/save";
 import * as Tooltip from "$lib/components/ui/tooltip/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
 import { Kbd } from "$lib/components/ui/kbd/index.js";
</script>
<Tooltip.Root>
 <Tooltip.Trigger class={buttonVariants({ variant: "outline", size: "icon-sm" })}>
  <SaveIcon />
 </Tooltip.Trigger>
 <Tooltip.Content>
  Save Changes <Kbd>S</Kbd>
 </Tooltip.Content>
</Tooltip.Root>
```

View Code

## [Disabled Button](#disabled-button)

Show a tooltip on a disabled button by wrapping it with a span.

```svelte
<script lang="ts">
 import * as Tooltip from "$lib/components/ui/tooltip/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
<Tooltip.Root>
 <Tooltip.Trigger>
  {#snippet child({ props })}
   <span {...props} class="inline-block w-fit">
    <Button variant="outline" disabled>Disabled</Button>
   </span>
  {/snippet}
 </Tooltip.Trigger>
 <Tooltip.Content>
  <p>This feature is currently unavailable</p>
 </Tooltip.Content>
</Tooltip.Root>
```

View Code

## [Changelog](#changelog)

### [2025-12 Update tooltip colors](#2025-12-update-tooltip-colors)

We've updated the tooltip colors to use the foreground color for the background and the background color for the foreground.

Replace `bg-primary text-primary-foreground` with `bg-foreground text-background` for `<Tooltip.Content />`.