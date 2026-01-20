# Popover

Displays rich content in a portal, triggered by a button.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add popover
```

```bash
npx shadcn-svelte@latest add popover
```

```bash
bun x shadcn-svelte@latest add popover
```

## Usage

```svelte
<script lang="ts">
  import * as Popover from "$lib/components/ui/popover/index.js";
</script>

<Popover.Root>
  <Popover.Trigger>Open</Popover.Trigger>
  <Popover.Content>Place content for the popover here.</Popover.Content>
</Popover.Root>
```

## Examples

### With Form

```svelte
<script lang="ts">
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
</script>

<Popover.Root>
  <Popover.Trigger class={buttonVariants({ variant: "outline" })}>
    Open popover
  </Popover.Trigger>
  <Popover.Content class="w-80">
    <div class="grid gap-4">
      <div class="space-y-2">
        <h4 class="leading-none font-medium">Dimensions</h4>
        <p class="text-muted-foreground text-sm">
          Set the dimensions for the layer.
        </p>
      </div>
      <div class="grid gap-2">
        <div class="grid grid-cols-3 items-center gap-4">
          <Label for="width">Width</Label>
          <Input id="width" value="100%" class="col-span-2 h-8" />
        </div>
        <div class="grid grid-cols-3 items-center gap-4">
          <Label for="height">Height</Label>
          <Input id="height" value="25px" class="col-span-2 h-8" />
        </div>
      </div>
    </div>
  </Popover.Content>
</Popover.Root>
```

## Components

- **Popover.Root** - Root container
- **Popover.Trigger** - Button that opens the popover
- **Popover.Content** - Popover content

## API

Built on [Bits UI Popover](https://bits-ui.com/docs/components/popover).

### Popover.Content Props

- `align` - Alignment relative to trigger ("start" | "center" | "end")
- `side` - Side to render ("top" | "right" | "bottom" | "left")
- `sideOffset` - Distance from trigger
- `class` - Additional CSS classes
