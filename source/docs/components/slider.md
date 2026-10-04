# Slider

An input where the user selects a value from within a given range.

[Docs](https://bits-ui.com/docs/components/slider)

[API Reference](https://bits-ui.com/docs/components/slider#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state(75);
</script>
<Slider
  type="single"
  bind:value
  max={100}
  step={1}
  class="mx-auto w-full max-w-xs"
/>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add slider
```

```bash
npx shadcn-svelte@latest add slider
```

```bash
bun x shadcn-svelte@latest add slider
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state(33);
</script>
```

```svelte
<Slider type="single" bind:value max={100} step={1} />
```

## [Range](#range)

Use `type="multiple"` with an array of two values for a range slider.

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state([25, 50]);
</script>
<Slider
  type="multiple"
  bind:value
  max={100}
  step={5}
  class="mx-auto w-full max-w-xs"
/>
```

View Code

## [Multiple Thumbs](#multiple-thumbs)

Use an array with multiple values for multiple thumbs.

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state([10, 20, 70]);
</script>
<Slider
  type="multiple"
  bind:value
  max={100}
  step={10}
  class="mx-auto w-full max-w-xs"
/>
```

View Code

## [Vertical](#vertical)

Use `orientation="vertical"` for a vertical slider.

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let first = $state(50);
  let second = $state(25);
</script>
<div class="mx-auto flex w-full max-w-xs items-center justify-center gap-6">
  <Slider
    type="single"
    bind:value={first}
    max={100}
    step={1}
    orientation="vertical"
    class="h-40"
  />
  <Slider
    type="single"
    bind:value={second}
    max={100}
    step={1}
    orientation="vertical"
    class="h-40"
  />
</div>
```

View Code

## [Controlled](#controlled)

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state([0.3, 0.7]);
</script>
<div class="mx-auto grid w-full max-w-xs gap-3">
  <div class="flex items-center justify-between gap-2">
    <Label for="slider-demo-temperature">Temperature</Label>
    <span class="text-sm text-muted-foreground">{value.join(", ")}</span>
  </div>
  <Slider
    type="multiple"
    id="slider-demo-temperature"
    bind:value
    min={0}
    max={1}
    step={0.1}
  />
</div>
```

View Code

## [Disabled](#disabled)

Use the `disabled` prop to disable the slider.

```svelte
<script lang="ts">
  import { Slider } from "$lib/components/ui/slider/index.js";
  let value = $state(50);
</script>
<Slider
  type="single"
  bind:value
  max={100}
  step={1}
  disabled
  class="mx-auto w-full max-w-xs"
/>
```

View Code