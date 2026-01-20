# Context Menu

Displays a menu to the user — such as a set of actions or functions — triggered by right click.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add context-menu
```

```bash
npx shadcn-svelte@latest add context-menu
```

```bash
bun x shadcn-svelte@latest add context-menu
```

## Usage

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>

<ContextMenu.Root>
  <ContextMenu.Trigger>Right click</ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Item>Profile</ContextMenu.Item>
    <ContextMenu.Item>Billing</ContextMenu.Item>
    <ContextMenu.Item>Team</ContextMenu.Item>
    <ContextMenu.Item>Subscription</ContextMenu.Item>
  </ContextMenu.Content>
</ContextMenu.Root>
```

## Examples

### With Shortcuts

```svelte
<ContextMenu.Item>
  Back
  <ContextMenu.Shortcut>⌘[</ContextMenu.Shortcut>
</ContextMenu.Item>
```

### Submenus

```svelte
<ContextMenu.Sub>
  <ContextMenu.SubTrigger>More Tools</ContextMenu.SubTrigger>
  <ContextMenu.SubContent>
    <ContextMenu.Item>Save Page As...</ContextMenu.Item>
    <ContextMenu.Item>Create Shortcut...</ContextMenu.Item>
    <ContextMenu.Separator />
    <ContextMenu.Item>Developer Tools</ContextMenu.Item>
  </ContextMenu.SubContent>
</ContextMenu.Sub>
```

### Checkbox Items

```svelte
<script lang="ts">
  let showBookmarks = $state(false);
</script>

<ContextMenu.CheckboxItem bind:checked={showBookmarks}>
  Show Bookmarks
</ContextMenu.CheckboxItem>
```

### Radio Groups

```svelte
<script lang="ts">
  let value = $state("pedro");
</script>

<ContextMenu.RadioGroup bind:value>
  <ContextMenu.GroupHeading inset>People</ContextMenu.GroupHeading>
  <ContextMenu.RadioItem value="pedro">Pedro Duarte</ContextMenu.RadioItem>
  <ContextMenu.RadioItem value="colm">Colm Tuite</ContextMenu.RadioItem>
</ContextMenu.RadioGroup>
```

## Components

- **ContextMenu.Root** - Root container
- **ContextMenu.Trigger** - Right-click trigger area
- **ContextMenu.Content** - Menu content
- **ContextMenu.Item** - Menu item
- **ContextMenu.CheckboxItem** - Checkbox menu item
- **ContextMenu.RadioGroup** - Radio group container
- **ContextMenu.RadioItem** - Radio menu item
- **ContextMenu.Sub** - Submenu container
- **ContextMenu.SubTrigger** - Submenu trigger
- **ContextMenu.SubContent** - Submenu content
- **ContextMenu.Separator** - Visual separator
- **ContextMenu.Shortcut** - Keyboard shortcut display

## API

Built on [Bits UI Context Menu](https://bits-ui.com/docs/components/context-menu).
