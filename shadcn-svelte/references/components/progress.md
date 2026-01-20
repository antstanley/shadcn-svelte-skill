# Progress

Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add progress
```

```bash
npx shadcn-svelte@latest add progress
```

```bash
bun x shadcn-svelte@latest add progress
```

## Usage

```svelte
<script lang="ts">
  import { Progress } from "$lib/components/ui/progress/index.js";
</script>

<Progress value={33} />
```

## Examples

### Basic

```svelte
<Progress value={33} />
```

### With Dynamic Value

```svelte
<script lang="ts">
  import { Progress } from "$lib/components/ui/progress/index.js";
  import { onMount } from "svelte";

  let value = $state(13);

  onMount(() => {
    const timer = setTimeout(() => {
      value = 66;
    }, 500);
    return () => clearTimeout(timer);
  });
</script>

<Progress {value} />
```

### Custom Max Value

```svelte
<Progress value={5} max={10} />
```

## Props

- `value` - Current progress value
- `max` - Maximum value (default: 100)
- `class` - Additional CSS classes

## API

Built on [Bits UI Progress](https://bits-ui.com/docs/components/progress).
