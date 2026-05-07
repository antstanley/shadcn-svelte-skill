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
  let value = $state(50);
</script>
<Slider type="single" bind:value max={100} step={1} class="max-w-[70%]" />
```

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
  let value = $state(33);
</script>
```

```svelte
<Slider type="single" bind:value max={100} step={1} />
```