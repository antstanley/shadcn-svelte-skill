# Dropdown Menu

Displays a menu to the user — such as a set of actions or functions — triggered by a button.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add dropdown-menu
```

```bash
npx shadcn-svelte@latest add dropdown-menu
```

```bash
bun x shadcn-svelte@latest add dropdown-menu
```

## Usage

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
</script>

<DropdownMenu.Root>
  <DropdownMenu.Trigger>Open</DropdownMenu.Trigger>
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Label>My Account</DropdownMenu.Label>
      <DropdownMenu.Separator />
      <DropdownMenu.Item>Profile</DropdownMenu.Item>
      <DropdownMenu.Item>Billing</DropdownMenu.Item>
      <DropdownMenu.Item>Settings</DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

## Examples

### Checkbox Items

```svelte
<script lang="ts">
  let showStatusBar = $state(true);
  let showActivityBar = $state(false);
</script>

<DropdownMenu.CheckboxItem bind:checked={showStatusBar}>
  Status Bar
</DropdownMenu.CheckboxItem>
<DropdownMenu.CheckboxItem bind:checked={showActivityBar}>
  Activity Bar
</DropdownMenu.CheckboxItem>
```

### Radio Groups

```svelte
<script lang="ts">
  let position = $state("bottom");
</script>

<DropdownMenu.RadioGroup bind:value={position}>
  <DropdownMenu.RadioItem value="top">Top</DropdownMenu.RadioItem>
  <DropdownMenu.RadioItem value="bottom">Bottom</DropdownMenu.RadioItem>
  <DropdownMenu.RadioItem value="right">Right</DropdownMenu.RadioItem>
</DropdownMenu.RadioGroup>
```

### Submenus

```svelte
<DropdownMenu.Sub>
  <DropdownMenu.SubTrigger>Invite users</DropdownMenu.SubTrigger>
  <DropdownMenu.SubContent>
    <DropdownMenu.Item>Email</DropdownMenu.Item>
    <DropdownMenu.Item>Message</DropdownMenu.Item>
  </DropdownMenu.SubContent>
</DropdownMenu.Sub>
```

## Components

- **DropdownMenu.Root** - Root container
- **DropdownMenu.Trigger** - Button that opens the menu
- **DropdownMenu.Content** - Menu content
- **DropdownMenu.Group** - Group of items
- **DropdownMenu.Label** - Group label
- **DropdownMenu.Item** - Menu item
- **DropdownMenu.CheckboxItem** - Checkbox menu item
- **DropdownMenu.RadioGroup** - Radio group container
- **DropdownMenu.RadioItem** - Radio menu item
- **DropdownMenu.Sub** - Submenu container
- **DropdownMenu.SubTrigger** - Submenu trigger
- **DropdownMenu.SubContent** - Submenu content
- **DropdownMenu.Separator** - Visual separator
- **DropdownMenu.Shortcut** - Keyboard shortcut display
