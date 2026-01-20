# Input

Displays a form input field or a component that looks like an input field.

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Input type="email" placeholder="Email" class="max-w-xs" />
```

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
```

```svelte
<Input />
```

## Examples

### Default

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
</script>
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
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Input disabled type="email" placeholder="Email" class="max-w-sm" />
```

### With Label

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  const id = $props.id();
</script>
<div class="flex w-full max-w-sm flex-col gap-1.5">
  <Label for="email-{id}">Email</Label>
  <Input type="email" id="email-{id}" placeholder="Email" />
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