# Skeleton

Use to show a placeholder while content is loading.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add skeleton
```

```bash
npx shadcn-svelte@latest add skeleton
```

```bash
bun x shadcn-svelte@latest add skeleton
```

## Usage

```svelte
<script lang="ts">
  import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>

<Skeleton class="h-[20px] w-[100px] rounded-full" />
```

## Examples

### Avatar with Text

```svelte
<div class="flex items-center space-x-4">
  <Skeleton class="size-12 rounded-full" />
  <div class="space-y-2">
    <Skeleton class="h-4 w-[250px]" />
    <Skeleton class="h-4 w-[200px]" />
  </div>
</div>
```

### Card

```svelte
<div class="flex flex-col space-y-3">
  <Skeleton class="h-[125px] w-[250px] rounded-xl" />
  <div class="space-y-2">
    <Skeleton class="h-4 w-[250px]" />
    <Skeleton class="h-4 w-[200px]" />
  </div>
</div>
```

### Table Rows

```svelte
<div class="space-y-2">
  {#each Array(5) as _, i}
    <Skeleton class="h-10 w-full" />
  {/each}
</div>
```

## Props

- `class` - CSS classes for sizing and shape customization

## Styling

The Skeleton component uses CSS classes for all customization:

- Use `h-*` and `w-*` for dimensions
- Use `rounded-*` for border radius
- The animation is built-in via the component styles
