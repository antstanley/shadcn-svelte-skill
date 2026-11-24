# Toggle Group

A set of two-state buttons that can be toggled on or off.

[Docs](https://bits-ui.com/docs/components/toggle-group)

[API Reference](https://bits-ui.com/docs/components/toggle-group#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import BoldIcon from "@lucide/svelte/icons/bold";
 import ItalicIcon from "@lucide/svelte/icons/italic";
 import UnderlineIcon from "@lucide/svelte/icons/underline";
 import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root variant="outline" type="multiple">
 <ToggleGroup.Item value="bold" aria-label="Toggle bold">
  <BoldIcon />
 </ToggleGroup.Item>
 <ToggleGroup.Item value="italic" aria-label="Toggle italic">
  <ItalicIcon />
 </ToggleGroup.Item>
 <ToggleGroup.Item value="strikethrough" aria-label="Toggle strikethrough">
  <UnderlineIcon />
 </ToggleGroup.Item>
</ToggleGroup.Root>
```

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

## [Outline](#outline)

Use `variant="outline"` for an outline style.

```svelte
<script lang="ts">
 import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root variant="outline" type="single" value="all">
 <ToggleGroup.Item value="all" aria-label="Toggle all">All</ToggleGroup.Item>
 <ToggleGroup.Item value="missed" aria-label="Toggle missed">Missed</ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

## [Size](#size)

Use the `size` prop to change the size of the toggle group.

```svelte
<script lang="ts">
 import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
 const sides = ["top", "bottom", "left", "right"] as const;
</script>
<div class="flex flex-col gap-4">
 <ToggleGroup.Root type="single" size="sm" value="top" variant="outline">
  {#each sides as side (side)}
   <ToggleGroup.Item value={side} aria-label="Toggle {side}" class="capitalize">
    {side}
   </ToggleGroup.Item>
  {/each}
 </ToggleGroup.Root>
 <ToggleGroup.Root type="single" value="top" variant="outline">
  {#each sides as side (side)}
   <ToggleGroup.Item value={side} aria-label="Toggle {side}" class="capitalize">
    {side}
   </ToggleGroup.Item>
  {/each}
 </ToggleGroup.Root>
</div>
```

View Code

## [Spacing](#spacing)

Use `spacing` to add spacing between toggle group items.

```svelte
<script lang="ts">
 import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
 const sides = ["top", "bottom", "left", "right"] as const;
</script>
<ToggleGroup.Root type="single" size="sm" value="top" variant="outline" spacing={2}>
 {#each sides as side (side)}
  <ToggleGroup.Item value={side} aria-label="Toggle {side}" class="capitalize">
   {side}
  </ToggleGroup.Item>
 {/each}
</ToggleGroup.Root>
```

View Code

## [Vertical](#vertical)

Use `orientation="vertical"` for vertical toggle groups.

```svelte
<script lang="ts">
 import BoldIcon from "@lucide/svelte/icons/bold";
 import ItalicIcon from "@lucide/svelte/icons/italic";
 import UnderlineIcon from "@lucide/svelte/icons/underline";
 import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root type="multiple" orientation="vertical" spacing={1} value={["bold", "italic"]}>
 <ToggleGroup.Item value="bold" aria-label="Toggle bold">
  <BoldIcon />
 </ToggleGroup.Item>
 <ToggleGroup.Item value="italic" aria-label="Toggle italic">
  <ItalicIcon />
 </ToggleGroup.Item>
 <ToggleGroup.Item value="underline" aria-label="Toggle underline">
  <UnderlineIcon />
 </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

## [Disabled](#disabled)

```svelte
<script lang="ts">
 import BoldIcon from "@lucide/svelte/icons/bold";
 import ItalicIcon from "@lucide/svelte/icons/italic";
 import UnderlineIcon from "@lucide/svelte/icons/underline";
 import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root disabled type="single">
 <ToggleGroup.Item value="bold" aria-label="Toggle bold">
  <BoldIcon />
 </ToggleGroup.Item>
 <ToggleGroup.Item value="italic" aria-label="Toggle italic">
  <ItalicIcon />
 </ToggleGroup.Item>
 <ToggleGroup.Item value="strikethrough" aria-label="Toggle strikethrough">
  <UnderlineIcon />
 </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

## [Custom](#custom)

A custom toggle group example.

```svelte
<script lang="ts">
 import * as Field from "$lib/components/ui/field/index.js";
 import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
 const weights = [
  { value: "light", label: "Light", class: "font-light" },
  { value: "normal", label: "Normal", class: "font-normal" },
  { value: "medium", label: "Medium", class: "font-medium" },
  { value: "bold", label: "Bold", class: "font-bold" },
];
 let fontWeight = $state("normal");
</script>
<Field.Field>
 <Field.Label>Font Weight</Field.Label>
 <ToggleGroup.Root type="single" bind:value={fontWeight} variant="outline" spacing={2} size="lg">
  {#each weights as weight (weight.value)}
   <ToggleGroup.Item
    value={weight.value}
    aria-label={weight.label}
    class="flex size-16 flex-col items-center justify-center rounded-xl"
   >
    <span class="text-2xl leading-none {weight.class}">Aa</span>
    <span class="text-xs text-muted-foreground">{weight.label}</span>
   </ToggleGroup.Item>
  {/each}
 </ToggleGroup.Root>
 <Field.Description>
  Use <code class="rounded-md bg-muted px-1 py-0.5 font-mono">font-{fontWeight}</code> to set the font
  weight.
 </Field.Description>
</Field.Field>
```

View Code