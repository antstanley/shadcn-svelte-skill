# Slider

An input where the user selects a value from within a given range.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add slider
```

```bash
npx shadcn-svelte@latest add slider
```

```bash
bun x shadcn-svelte@latest add slider
```

## Usage

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state(50);
</script>

<Slider type="single" bind:value max={100} step={1} class="max-w-[70%]" />
```

## Examples

### Basic

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state(33);
</script>

<Slider type="single" bind:value max={100} step={1} />
```

### With Min/Max

```svelte
<Slider type="single" bind:value min={0} max={100} step={1} />
```

### Custom Step

```svelte
<Slider type="single" bind:value min={0} max={100} step={10} />
```

## API

Built on [Bits UI Slider](https://bits-ui.com/docs/components/slider).

### Props

- `type` - "single" for single value slider
- `value` - The current value (bindable)
- `min` - Minimum value (default: 0)
- `max` - Maximum value (default: 100)
- `step` - Step increment (default: 1)
- `disabled` - Whether the slider is disabled
- `orientation` - "horizontal" or "vertical"
