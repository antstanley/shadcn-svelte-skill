# Tooltip

A popup that displays information related to an element when the element receives keyboard focus or the mouse hovers over it.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add tooltip
```

```bash
npx shadcn-svelte@latest add tooltip
```

```bash
bun x shadcn-svelte@latest add tooltip
```

## Setup

The `Tooltip.Provider` should be placed once in your root layout, wrapping all content that will contain tooltips. This ensures only one tooltip within the provider can be open at a time.

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";

  let { children } = $props();
</script>

<Tooltip.Provider>
  {@render children()}
</Tooltip.Provider>
```

## Usage

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

## Examples

### With Button

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  import * as Tooltip from "$lib/components/ui/tooltip/index.js";
</script>

<Tooltip.Root>
  <Tooltip.Trigger>
    {#snippet child({ props })}
      <Button variant="outline" {...props}>Hover me</Button>
    {/snippet}
  </Tooltip.Trigger>
  <Tooltip.Content>
    <p>This is a tooltip</p>
  </Tooltip.Content>
</Tooltip.Root>
```

### Instant Tooltips

Create zones with `delayDuration={0}` for instant tooltips:

```svelte
<Tooltip.Provider delayDuration={0}>
  <!-- Tooltips in this area appear instantly -->
</Tooltip.Provider>
```

## Components

- **Tooltip.Provider** - Context provider (place in root layout)
- **Tooltip.Root** - Root container for individual tooltip
- **Tooltip.Trigger** - Element that triggers the tooltip
- **Tooltip.Content** - Tooltip content

## API

Built on [Bits UI Tooltip](https://bits-ui.com/docs/components/tooltip).

### Tooltip.Provider Props

- `delayDuration` - Delay before tooltip appears (default: 700ms)
- `skipDelayDuration` - Time before delay resets after leaving a tooltip

### Tooltip.Content Props

- `side` - Side to render ("top" | "right" | "bottom" | "left")
- `align` - Alignment ("start" | "center" | "end")
- `sideOffset` - Distance from trigger
