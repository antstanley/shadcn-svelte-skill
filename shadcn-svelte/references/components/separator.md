# Separator

Visually or semantically separates content.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add separator
```

```bash
npx shadcn-svelte@latest add separator
```

```bash
bun x shadcn-svelte@latest add separator
```

## Usage

```svelte
<script lang="ts">
  import { Separator } from "$lib/components/ui/separator/index.js";
</script>

<Separator />
```

## Examples

### Horizontal (Default)

```svelte
<div>
  <div class="space-y-1">
    <h4 class="text-sm font-medium leading-none">Radix Primitives</h4>
    <p class="text-sm text-muted-foreground">
      An open-source UI component library.
    </p>
  </div>
  <Separator class="my-4" />
  <div class="flex h-5 items-center space-x-4 text-sm">
    <div>Blog</div>
    <Separator orientation="vertical" />
    <div>Docs</div>
    <Separator orientation="vertical" />
    <div>Source</div>
  </div>
</div>
```

### Vertical

```svelte
<div class="flex h-5 items-center space-x-4 text-sm">
  <div>Blog</div>
  <Separator orientation="vertical" />
  <div>Docs</div>
  <Separator orientation="vertical" />
  <div>Source</div>
</div>
```

## API

Built on [Bits UI Separator](https://bits-ui.com/docs/components/separator).

### Props

- `orientation` - "horizontal" (default) or "vertical"
- `decorative` - Whether the separator is purely decorative
- `class` - Additional CSS classes
