# Select

Displays a list of options for the user to pick from—triggered by a button.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add select
```

```bash
npx shadcn-svelte@latest add select
```

```bash
bun x shadcn-svelte@latest add select
```

## Usage

```svelte
<script lang="ts">
  import * as Select from "$lib/components/ui/select/index.js";
</script>

<Select.Root type="single">
  <Select.Trigger class="w-[180px]">
    <Select.Value placeholder="Select a fruit" />
  </Select.Trigger>
  <Select.Content>
    <Select.Group>
      <Select.Label>Fruits</Select.Label>
      <Select.Item value="apple">Apple</Select.Item>
      <Select.Item value="banana">Banana</Select.Item>
      <Select.Item value="orange">Orange</Select.Item>
    </Select.Group>
  </Select.Content>
</Select.Root>
```

## Examples

### Theme Selector

```svelte
<Select.Root type="single">
  <Select.Trigger class="w-[180px]">
    <Select.Value placeholder="Select theme" />
  </Select.Trigger>
  <Select.Content>
    <Select.Item value="light">Light</Select.Item>
    <Select.Item value="dark">Dark</Select.Item>
    <Select.Item value="system">System</Select.Item>
  </Select.Content>
</Select.Root>
```

### Grouped Options

```svelte
<Select.Root type="single">
  <Select.Trigger class="w-[280px]">
    <Select.Value placeholder="Select a timezone" />
  </Select.Trigger>
  <Select.Content>
    <Select.Group>
      <Select.Label>North America</Select.Label>
      <Select.Item value="est">Eastern Standard Time (EST)</Select.Item>
      <Select.Item value="cst">Central Standard Time (CST)</Select.Item>
      <Select.Item value="pst">Pacific Standard Time (PST)</Select.Item>
    </Select.Group>
    <Select.Group>
      <Select.Label>Europe</Select.Label>
      <Select.Item value="gmt">Greenwich Mean Time (GMT)</Select.Item>
      <Select.Item value="cet">Central European Time (CET)</Select.Item>
    </Select.Group>
  </Select.Content>
</Select.Root>
```

### Disabled Item

```svelte
<Select.Item value="unavailable" disabled>Unavailable</Select.Item>
```

### Scrollable Content

For large lists, the Select.Content automatically handles scrolling:

```svelte
<Select.Content>
  <Select.Group>
    <Select.Label>Timezones</Select.Label>
    {#each timezones as tz}
      <Select.Item value={tz.value}>{tz.label}</Select.Item>
    {/each}
  </Select.Group>
</Select.Content>
```

## Components

- **Select.Root** - The root container
- **Select.Trigger** - The button that opens the select
- **Select.Value** - Displays the selected value or placeholder
- **Select.Content** - The dropdown content container
- **Select.Group** - Groups related items together
- **Select.Label** - Label for a group of items
- **Select.Item** - An individual selectable option
- **Select.Separator** - Visual separator between groups
