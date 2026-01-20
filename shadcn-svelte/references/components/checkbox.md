# Checkbox

A control that allows the user to toggle between checked and not checked.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add checkbox
```

```bash
npx shadcn-svelte@latest add checkbox
```

```bash
bun x shadcn-svelte@latest add checkbox
```

## Usage

```svelte
<script lang="ts">
  import { Checkbox } from "$lib/components/ui/checkbox/index.js";
</script>

<Checkbox />
```

## Examples

### Default

```svelte
<Checkbox />
```

### Checked

```svelte
<Checkbox checked />
```

### Disabled

```svelte
<Checkbox disabled />
```

### With Label

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

### With Description

```svelte
<div class="flex items-start space-x-2">
  <Checkbox id="notifications" />
  <div class="grid gap-1.5 leading-none">
    <Label for="notifications">Enable notifications</Label>
    <p class="text-muted-foreground text-sm">
      You will receive notifications about important updates.
    </p>
  </div>
</div>
```

### Custom Styling

Use data attributes and CSS classes for custom appearance:

```svelte
<Checkbox class="data-[state=checked]:bg-blue-500" />
```

## API

The Checkbox component is built on [Bits UI Checkbox](https://bits-ui.com/docs/components/checkbox).

### Props

- `checked` - Whether the checkbox is checked
- `disabled` - Whether the checkbox is disabled
- `required` - Whether the checkbox is required
- `name` - The name of the checkbox for form submission
- `value` - The value of the checkbox for form submission
