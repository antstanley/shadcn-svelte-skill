# Aspect Ratio

Displays content within a desired ratio.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add aspect-ratio
```

```bash
npx shadcn-svelte@latest add aspect-ratio
```

```bash
bun x shadcn-svelte@latest add aspect-ratio
```

## Usage

```svelte
<script lang="ts">
  import { AspectRatio } from "$lib/components/ui/aspect-ratio/index.js";
</script>

<div class="w-[450px]">
  <AspectRatio ratio={16 / 9} class="bg-muted">
    <img src="..." alt="..." class="rounded-md object-cover" />
  </AspectRatio>
</div>
```

## Examples

### 16:9 Ratio

```svelte
<AspectRatio ratio={16 / 9} class="bg-muted rounded-lg">
  <img
    src="https://images.unsplash.com/photo-1588345921523-c2dcdb7f1dcd?w=800"
    alt="Image"
    class="h-full w-full rounded-lg object-cover"
  />
</AspectRatio>
```

### Square (1:1)

```svelte
<AspectRatio ratio={1} class="bg-muted rounded-lg">
  <img src="..." alt="..." class="h-full w-full rounded-lg object-cover" />
</AspectRatio>
```

### 4:3 Ratio

```svelte
<AspectRatio ratio={4 / 3} class="bg-muted rounded-lg">
  <img src="..." alt="..." class="h-full w-full rounded-lg object-cover" />
</AspectRatio>
```

## Props

- `ratio` - The desired aspect ratio (default: 1)
- `class` - Additional CSS classes

## API

Built on [Bits UI Aspect Ratio](https://bits-ui.com/docs/components/aspect-ratio).
