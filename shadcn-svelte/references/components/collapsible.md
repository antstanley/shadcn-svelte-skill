# Collapsible

An interactive component which expands/collapses a panel.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add collapsible
```

```bash
npx shadcn-svelte@latest add collapsible
```

```bash
bun x shadcn-svelte@latest add collapsible
```

## Usage

```svelte
<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible/index.js";
</script>

<Collapsible.Root>
  <Collapsible.Trigger>Can I use this in my project?</Collapsible.Trigger>
  <Collapsible.Content>
    Yes. Free to use for personal and commercial projects. No attribution required.
  </Collapsible.Content>
</Collapsible.Root>
```

## Examples

### With Button Trigger

```svelte
<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import ChevronsUpDown from "lucide-svelte/icons/chevrons-up-down";

  let open = $state(false);
</script>

<Collapsible.Root bind:open class="w-[350px] space-y-2">
  <div class="flex items-center justify-between space-x-4 px-4">
    <h4 class="text-sm font-semibold">@peduarte starred 3 repositories</h4>
    <Collapsible.Trigger>
      {#snippet child({ props })}
        <Button {...props} variant="ghost" size="sm" class="w-9 p-0">
          <ChevronsUpDown class="h-4 w-4" />
          <span class="sr-only">Toggle</span>
        </Button>
      {/snippet}
    </Collapsible.Trigger>
  </div>
  <div class="rounded-md border px-4 py-3 font-mono text-sm">@radix-ui/primitives</div>
  <Collapsible.Content class="space-y-2">
    <div class="rounded-md border px-4 py-3 font-mono text-sm">@radix-ui/colors</div>
    <div class="rounded-md border px-4 py-3 font-mono text-sm">@stitches/react</div>
  </Collapsible.Content>
</Collapsible.Root>
```

## Components

- **Collapsible.Root** - Main container with open state
- **Collapsible.Trigger** - Element that toggles the content
- **Collapsible.Content** - Collapsible content area
