# Switch

A control that allows the user to toggle between checked and not checked.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add switch
```

```bash
npx shadcn-svelte@latest add switch
```

```bash
bun x shadcn-svelte@latest add switch
```

## Usage

```svelte
<script lang="ts">
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>

<Switch />
```

## Examples

### With Label

```svelte
<script lang="ts">
  import { Switch } from "$lib/components/ui/switch/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<div class="flex items-center space-x-2">
  <Switch id="airplane-mode" />
  <Label for="airplane-mode">Airplane Mode</Label>
</div>
```

### Controlled

```svelte
<script lang="ts">
  import { Switch } from "$lib/components/ui/switch/index.js";

  let checked = $state(false);
</script>

<Switch bind:checked />
<p>Switch is {checked ? "on" : "off"}</p>
```

### Disabled

```svelte
<Switch disabled />
```

## API

Built on [Bits UI Switch](https://bits-ui.com/docs/components/switch).

### Props

- `checked` - Whether the switch is checked (bindable)
- `disabled` - Whether the switch is disabled
- `required` - Whether the switch is required
- `name` - The name for form submission
- `value` - The value for form submission
