# Toggle Group

A set of two-state buttons that can be toggled on or off.

[Docs](https://bits-ui.com/docs/components/toggle-group)

[API Reference](https://bits-ui.com/docs/components/toggle-group#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add toggle-group
```

```bash
npx shadcn-svelte@latest add toggle-group
```

```bash
bun x shadcn-svelte@latest add toggle-group
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
```

```svelte
<ToggleGroup.Root type="single">
  <ToggleGroup.Item value="a">A</ToggleGroup.Item>
  <ToggleGroup.Item value="b">B</ToggleGroup.Item>
  <ToggleGroup.Item value="c">C</ToggleGroup.Item>
</ToggleGroup.Root>
```

## [Examples](#examples)

### [Outline](#outline)

View Code

### [Single](#single)

View Code

### [Small](#small)

View Code

### [Large](#large)

View Code

### [Disabled](#disabled)

View Code

### [Spacing](#spacing)

Use `spacing={2}` to add spacing between toggle group items.

View Code