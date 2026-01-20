# Command

Fast, composable, unstyled command menu for Svelte.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add command
```

```bash
npx shadcn-svelte@latest add command
```

```bash
bun x shadcn-svelte@latest add command
```

## Usage

```svelte
<script lang="ts">
  import * as Command from "$lib/components/ui/command/index.js";
</script>

<Command.Root>
  <Command.Input placeholder="Type a command or search..." />
  <Command.List>
    <Command.Empty>No results found.</Command.Empty>
    <Command.Group heading="Suggestions">
      <Command.Item>Calendar</Command.Item>
      <Command.Item>Search Emoji</Command.Item>
      <Command.Item>Calculator</Command.Item>
    </Command.Group>
    <Command.Separator />
    <Command.Group heading="Settings">
      <Command.Item>Profile</Command.Item>
      <Command.Item>Billing</Command.Item>
      <Command.Item>Settings</Command.Item>
    </Command.Group>
  </Command.List>
</Command.Root>
```

## Examples

### Command Dialog

Use keyboard shortcut to open a command dialog:

```svelte
<script lang="ts">
  import * as Command from "$lib/components/ui/command/index.js";

  let open = $state(false);

  function handleKeydown(e: KeyboardEvent) {
    if (e.key === "k" && (e.metaKey || e.ctrlKey)) {
      e.preventDefault();
      open = !open;
    }
  }
</script>

<svelte:document onkeydown={handleKeydown} />

<Command.Dialog bind:open>
  <Command.Input placeholder="Type a command or search..." />
  <Command.List>
    <Command.Empty>No results found.</Command.Empty>
    <Command.Group heading="Suggestions">
      <Command.Item>Calendar</Command.Item>
      <Command.Item>Search Emoji</Command.Item>
    </Command.Group>
  </Command.List>
</Command.Dialog>
```

### With Shortcuts

```svelte
<Command.Item>
  Profile
  <Command.Shortcut>⌘P</Command.Shortcut>
</Command.Item>
```

## Components

- **Command.Root** - Main container
- **Command.Dialog** - Dialog variant for modal command menu
- **Command.Input** - Search input
- **Command.List** - Scrollable list of items
- **Command.Empty** - Empty state message
- **Command.Group** - Group of related items
- **Command.Item** - Individual command item
- **Command.Separator** - Visual separator
- **Command.Shortcut** - Keyboard shortcut display

## Related

See [Combobox](/docs/components/combobox) for autocomplete functionality.
