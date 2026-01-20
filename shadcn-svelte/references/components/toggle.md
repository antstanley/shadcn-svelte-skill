# Toggle

A two-state button that can be either on or off.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add toggle
```

```bash
npx shadcn-svelte@latest add toggle
```

```bash
bun x shadcn-svelte@latest add toggle
```

## Usage

```svelte
<script lang="ts">
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>

<Toggle>Toggle</Toggle>
```

## Examples

### Default

```svelte
<Toggle aria-label="Toggle italic">
  <Italic class="h-4 w-4" />
</Toggle>
```

### Outline

```svelte
<Toggle variant="outline" aria-label="Toggle italic">
  <Italic class="h-4 w-4" />
</Toggle>
```

### With Text

```svelte
<Toggle aria-label="Toggle italic">
  <Italic class="mr-2 h-4 w-4" />
  Italic
</Toggle>
```

### Small

```svelte
<Toggle size="sm" aria-label="Toggle italic">
  <Italic class="h-4 w-4" />
</Toggle>
```

### Large

```svelte
<Toggle size="lg" aria-label="Toggle italic">
  <Italic class="h-4 w-4" />
</Toggle>
```

### Disabled

```svelte
<Toggle disabled aria-label="Toggle italic">
  <Italic class="h-4 w-4" />
</Toggle>
```

## Props

- `variant` - Visual style: `"default"` | `"outline"`
- `size` - Size: `"default"` | `"sm"` | `"lg"`
- `disabled` - Disable the toggle
- `pressed` - Controlled pressed state (bindable)

## Styling Active State

Use data attributes to style the pressed state:

```svelte
<Toggle class="data-[state=on]:bg-primary data-[state=on]:text-primary-foreground">
  Toggle
</Toggle>
```
