# Select

Displays a list of options for the user to pick fromtriggered by a button.

[Docs](https://bits-ui.com/docs/components/select)

[API Reference](https://bits-ui.com/docs/components/select#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add select
```

```bash
npx shadcn-svelte@latest add select
```

```bash
bun x shadcn-svelte@latest add select
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
</script>
```

```svelte
<Select.Root type="single">
  <Select.Trigger class="w-[180px]"></Select.Trigger>
  <Select.Content>
    <Select.Item value="light">Light</Select.Item>
    <Select.Item value="dark">Dark</Select.Item>
    <Select.Item value="system">System</Select.Item>
  </Select.Content>
</Select.Root>
```

## [Examples](#examples)

### [Scrollable](#scrollable)

View Code