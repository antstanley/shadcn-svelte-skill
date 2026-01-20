# Menubar

A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add menubar
```

```bash
npx shadcn-svelte@latest add menubar
```

```bash
bun x shadcn-svelte@latest add menubar
```

## Usage

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";
</script>

<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>File</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Item>
        New Tab
        <Menubar.Shortcut>⌘T</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item>New Window</Menubar.Item>
      <Menubar.Separator />
      <Menubar.Item>Share</Menubar.Item>
      <Menubar.Separator />
      <Menubar.Item>Print</Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

## Examples

### Complete Menubar

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";

  let bookmarks = $state(false);
  let fullUrls = $state(true);
  let profileRadioValue = $state("benoit");
</script>

<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>File</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Item>New Tab <Menubar.Shortcut>⌘T</Menubar.Shortcut></Menubar.Item>
      <Menubar.Item>New Window <Menubar.Shortcut>⌘N</Menubar.Shortcut></Menubar.Item>
      <Menubar.Separator />
      <Menubar.Sub>
        <Menubar.SubTrigger>Share</Menubar.SubTrigger>
        <Menubar.SubContent>
          <Menubar.Item>Email link</Menubar.Item>
          <Menubar.Item>Messages</Menubar.Item>
        </Menubar.SubContent>
      </Menubar.Sub>
    </Menubar.Content>
  </Menubar.Menu>

  <Menubar.Menu>
    <Menubar.Trigger>View</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.CheckboxItem bind:checked={bookmarks}>
        Always Show Bookmarks Bar
      </Menubar.CheckboxItem>
      <Menubar.CheckboxItem bind:checked={fullUrls}>
        Always Show Full URLs
      </Menubar.CheckboxItem>
    </Menubar.Content>
  </Menubar.Menu>

  <Menubar.Menu>
    <Menubar.Trigger>Profiles</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.RadioGroup bind:value={profileRadioValue}>
        <Menubar.RadioItem value="andy">Andy</Menubar.RadioItem>
        <Menubar.RadioItem value="benoit">Benoit</Menubar.RadioItem>
        <Menubar.RadioItem value="luis">Luis</Menubar.RadioItem>
      </Menubar.RadioGroup>
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

## Components

- **Menubar.Root** - Root container
- **Menubar.Menu** - Individual menu
- **Menubar.Trigger** - Menu trigger button
- **Menubar.Content** - Menu content
- **Menubar.Item** - Menu item
- **Menubar.CheckboxItem** - Checkbox menu item
- **Menubar.RadioGroup** - Radio group container
- **Menubar.RadioItem** - Radio menu item
- **Menubar.Sub** - Submenu container
- **Menubar.SubTrigger** - Submenu trigger
- **Menubar.SubContent** - Submenu content
- **Menubar.Separator** - Visual separator
- **Menubar.Shortcut** - Keyboard shortcut display

## API

Built on [Bits UI Menubar](https://bits-ui.com/docs/components/menubar).
