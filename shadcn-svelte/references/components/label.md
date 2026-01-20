# Label

Renders an accessible label associated with controls.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add label
```

```bash
npx shadcn-svelte@latest add label
```

```bash
bun x shadcn-svelte@latest add label
```

## Usage

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<Label for="email">Your email address</Label>
```

## Examples

### With Checkbox

```svelte
<script lang="ts">
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<div class="flex items-center space-x-2">
  <Checkbox id="terms" />
  <Label for="terms">Accept terms and conditions</Label>
</div>
```

### With Input

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<div class="grid gap-1.5">
  <Label for="email">Email</Label>
  <Input id="email" type="email" placeholder="you@example.com" />
</div>
```

## Accessibility

The `for` attribute on the Label should match the `id` of the form control it describes. This ensures proper accessibility linking between the label and its associated input element.
