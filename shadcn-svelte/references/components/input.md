# Input

Displays a form input field or a component that looks like an input field.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add input
```

```bash
npx shadcn-svelte@latest add input
```

```bash
bun x shadcn-svelte@latest add input
```

## Usage

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
</script>

<Input />
```

## Examples

### Default

```svelte
<Input type="email" placeholder="Email" class="max-w-xs" />
```

### File

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<div class="grid w-full max-w-sm items-center gap-1.5">
  <Label for="picture">Picture</Label>
  <Input id="picture" type="file" />
</div>
```

### Disabled

```svelte
<Input disabled type="email" placeholder="Email" class="max-w-sm" />
```

### With Label

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<div class="flex w-full max-w-sm flex-col gap-1.5">
  <Label for="email">Email</Label>
  <Input type="email" id="email" placeholder="Email" />
</div>
```

### With Button

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>

<div class="flex w-full max-w-sm items-center gap-2">
  <Input type="email" placeholder="Email" />
  <Button type="submit" variant="outline">Subscribe</Button>
</div>
```

## Props

The Input component accepts all standard HTML input attributes:

- `type` - Input type (text, email, password, file, etc.)
- `placeholder` - Placeholder text
- `disabled` - Whether the input is disabled
- `required` - Whether the input is required
- `name` - Input name for form submission
- `value` - Input value
- `class` - Additional CSS classes
