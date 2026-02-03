# Switch

A control that allows the user to toggle between checked and not checked.

[Docs](https://bits-ui.com/docs/components/switch)

[API Reference](https://bits-ui.com/docs/components/switch#api-reference)

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import { Switch } from "$lib/components/ui/switch/index.js";
</script>
<div class="flex items-center space-x-2">
  <Switch id="airplane-mode" />
  <Label for="airplane-mode">Airplane Mode</Label>
</div>
```

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
```

```svelte
<Switch />
```