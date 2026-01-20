# Radio Group

A set of checkable buttons—known as radio buttons—where no more than one of the buttons can be checked at a time.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add radio-group
```

```bash
npx shadcn-svelte@latest add radio-group
```

```bash
bun x shadcn-svelte@latest add radio-group
```

## Usage

```svelte
<script lang="ts">
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<RadioGroup.Root value="comfortable">
  <div class="flex items-center space-x-2">
    <RadioGroup.Item value="default" id="r1" />
    <Label for="r1">Default</Label>
  </div>
  <div class="flex items-center space-x-2">
    <RadioGroup.Item value="comfortable" id="r2" />
    <Label for="r2">Comfortable</Label>
  </div>
  <div class="flex items-center space-x-2">
    <RadioGroup.Item value="compact" id="r3" />
    <Label for="r3">Compact</Label>
  </div>
</RadioGroup.Root>
```

## Examples

### Basic Usage

```svelte
<script lang="ts">
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<RadioGroup.Root value="option-one">
  <div class="flex items-center space-x-2">
    <RadioGroup.Item value="option-one" id="option-one" />
    <Label for="option-one">Option One</Label>
  </div>
  <div class="flex items-center space-x-2">
    <RadioGroup.Item value="option-two" id="option-two" />
    <Label for="option-two">Option Two</Label>
  </div>
</RadioGroup.Root>
```

### Controlled

```svelte
<script lang="ts">
  import * as RadioGroup from "$lib/components/ui/radio-group/index.js";

  let value = $state("option-one");
</script>

<RadioGroup.Root bind:value>
  <RadioGroup.Item value="option-one" id="o1" />
  <RadioGroup.Item value="option-two" id="o2" />
</RadioGroup.Root>

<p>Selected: {value}</p>
```

## API

Built on [Bits UI Radio Group](https://bits-ui.com/docs/components/radio-group).

### RadioGroup.Root Props

- `value` - The currently selected value
- `disabled` - Whether the radio group is disabled
- `required` - Whether a selection is required
- `orientation` - Layout orientation ("horizontal" | "vertical")

### RadioGroup.Item Props

- `value` - The value of the radio item
- `disabled` - Whether this specific item is disabled
- `id` - ID for label association
