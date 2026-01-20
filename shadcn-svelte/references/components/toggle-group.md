# Toggle Group

A set of two-state buttons that can be toggled on or off.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add toggle-group
```

```bash
npx shadcn-svelte@latest add toggle-group
```

```bash
bun x shadcn-svelte@latest add toggle-group
```

## Usage

```svelte
<script lang="ts">
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>

<ToggleGroup.Root type="single">
  <ToggleGroup.Item value="a">A</ToggleGroup.Item>
  <ToggleGroup.Item value="b">B</ToggleGroup.Item>
  <ToggleGroup.Item value="c">C</ToggleGroup.Item>
</ToggleGroup.Root>
```

## Examples

### Default

```svelte
<ToggleGroup.Root type="single">
  <ToggleGroup.Item value="bold" aria-label="Toggle bold">
    <Bold class="h-4 w-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="italic" aria-label="Toggle italic">
    <Italic class="h-4 w-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="underline" aria-label="Toggle underline">
    <Underline class="h-4 w-4" />
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

### Outline

```svelte
<ToggleGroup.Root type="multiple" variant="outline">
  <ToggleGroup.Item value="bold" aria-label="Toggle bold">
    <Bold class="h-4 w-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="italic" aria-label="Toggle italic">
    <Italic class="h-4 w-4" />
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

### Single Selection

```svelte
<ToggleGroup.Root type="single" value="center">
  <ToggleGroup.Item value="left">Left</ToggleGroup.Item>
  <ToggleGroup.Item value="center">Center</ToggleGroup.Item>
  <ToggleGroup.Item value="right">Right</ToggleGroup.Item>
</ToggleGroup.Root>
```

### Multiple Selection

```svelte
<ToggleGroup.Root type="multiple">
  <ToggleGroup.Item value="bold">Bold</ToggleGroup.Item>
  <ToggleGroup.Item value="italic">Italic</ToggleGroup.Item>
  <ToggleGroup.Item value="underline">Underline</ToggleGroup.Item>
</ToggleGroup.Root>
```

### Sizes

```svelte
<ToggleGroup.Root type="single" size="sm">...</ToggleGroup.Root>
<ToggleGroup.Root type="single" size="lg">...</ToggleGroup.Root>
```

### Disabled

```svelte
<ToggleGroup.Root type="single" disabled>
  <ToggleGroup.Item value="a">A</ToggleGroup.Item>
  <ToggleGroup.Item value="b">B</ToggleGroup.Item>
</ToggleGroup.Root>
```

## Props

### Root

- `type` - Selection mode: `"single"` | `"multiple"`
- `value` - Selected value(s)
- `variant` - Visual style: `"default"` | `"outline"`
- `size` - Size: `"default"` | `"sm"` | `"lg"`
- `disabled` - Disable all items

### Item

- `value` - Item value
- `disabled` - Disable individual item
