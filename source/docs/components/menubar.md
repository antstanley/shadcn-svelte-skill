# Menubar

A visually persistent menu common in desktop applications that provides quick access to a consistent set of commands.

[Docs](https://bits-ui.com/docs/components/menubar)

[API Reference](https://bits-ui.com/docs/components/menubar#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";
  let bookmarks = $state(false);
  let fullUrls = $state(true);
  let profileRadioValue = $state("benoit");
</script>
<Menubar.Root class="w-72">
  <Menubar.Menu>
    <Menubar.Trigger>File</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Group>
        <Menubar.Item>
          New Tab <Menubar.Shortcut>T</Menubar.Shortcut>
        </Menubar.Item>
        <Menubar.Item>
          New Window <Menubar.Shortcut>N</Menubar.Shortcut>
        </Menubar.Item>
        <Menubar.Item disabled>New Incognito Window</Menubar.Item>
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Sub>
          <Menubar.SubTrigger>Share</Menubar.SubTrigger>
          <Menubar.SubContent>
            <Menubar.Group>
              <Menubar.Item>Email link</Menubar.Item>
              <Menubar.Item>Messages</Menubar.Item>
              <Menubar.Item>Notes</Menubar.Item>
            </Menubar.Group>
          </Menubar.SubContent>
        </Menubar.Sub>
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Item>
          Print... <Menubar.Shortcut>P</Menubar.Shortcut>
        </Menubar.Item>
      </Menubar.Group>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>Edit</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Group>
        <Menubar.Item>
          Undo <Menubar.Shortcut>Z</Menubar.Shortcut>
        </Menubar.Item>
        <Menubar.Item>
          Redo <Menubar.Shortcut>Z</Menubar.Shortcut>
        </Menubar.Item>
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Sub>
          <Menubar.SubTrigger>Find</Menubar.SubTrigger>
          <Menubar.SubContent>
            <Menubar.Group>
              <Menubar.Item>Search the web</Menubar.Item>
            </Menubar.Group>
            <Menubar.Separator />
            <Menubar.Group>
              <Menubar.Item>Find...</Menubar.Item>
              <Menubar.Item>Find Next</Menubar.Item>
              <Menubar.Item>Find Previous</Menubar.Item>
            </Menubar.Group>
          </Menubar.SubContent>
        </Menubar.Sub>
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Item>Cut</Menubar.Item>
        <Menubar.Item>Copy</Menubar.Item>
        <Menubar.Item>Paste</Menubar.Item>
      </Menubar.Group>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>View</Menubar.Trigger>
    <Menubar.Content class="w-44">
      <Menubar.Group>
        <Menubar.CheckboxItem bind:checked={bookmarks}
          >Bookmarks Bar</Menubar.CheckboxItem
        >
        <Menubar.CheckboxItem bind:checked={fullUrls}
          >Full URLs</Menubar.CheckboxItem
        >
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Item inset>
          Reload <Menubar.Shortcut>R</Menubar.Shortcut>
        </Menubar.Item>
        <Menubar.Item disabled inset>
          Force Reload <Menubar.Shortcut>R</Menubar.Shortcut>
        </Menubar.Item>
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Item inset>Toggle Fullscreen</Menubar.Item>
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Item inset>Hide Sidebar</Menubar.Item>
      </Menubar.Group>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>Profiles</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.RadioGroup bind:value={profileRadioValue}>
        <Menubar.RadioItem value="andy">Andy</Menubar.RadioItem>
        <Menubar.RadioItem value="benoit">Benoit</Menubar.RadioItem>
        <Menubar.RadioItem value="Luis">Luis</Menubar.RadioItem>
      </Menubar.RadioGroup>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Item inset>Edit...</Menubar.Item>
      </Menubar.Group>
      <Menubar.Separator />
      <Menubar.Group>
        <Menubar.Item inset>Add Profile...</Menubar.Item>
      </Menubar.Group>
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add menubar
```

```bash
npx shadcn-svelte@latest add menubar
```

```bash
bun x shadcn-svelte@latest add menubar
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";
</script>
```

```svelte
<Menubar.Root>
  <Menubar.Menu>
    <Menubar.Trigger>File</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Item>
        New Tab
        <Menubar.Shortcut>T</Menubar.Shortcut>
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

## [Checkbox](#checkbox)

Use `Menubar.CheckboxItem` for toggleable options.

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";
  let showBookmarksBar = $state(false);
  let showFullURLs = $state(true);
  let strikethrough = $state(true);
  let code = $state(false);
  let superscript = $state(false);
</script>
<Menubar.Root class="w-72">
  <Menubar.Menu>
    <Menubar.Trigger>View</Menubar.Trigger>
    <Menubar.Content class="w-64">
      <Menubar.CheckboxItem bind:checked={showBookmarksBar}>
        Always Show Bookmarks Bar
      </Menubar.CheckboxItem>
      <Menubar.CheckboxItem bind:checked={showFullURLs}
        >Always Show Full URLs</Menubar.CheckboxItem
      >
      <Menubar.Separator />
      <Menubar.Item inset>
        Reload <Menubar.Shortcut>R</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item disabled inset>
        Force Reload <Menubar.Shortcut>R</Menubar.Shortcut>
      </Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>Format</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.CheckboxItem bind:checked={strikethrough}
        >Strikethrough</Menubar.CheckboxItem
      >
      <Menubar.CheckboxItem bind:checked={code}>Code</Menubar.CheckboxItem>
      <Menubar.CheckboxItem bind:checked={superscript}
        >Superscript</Menubar.CheckboxItem
      >
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

View Code

## [Radio](#radio)

Use `Menubar.RadioGroup` and `Menubar.RadioItem` for single-select options.

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";
  let user = $state("benoit");
  let theme = $state("system");
</script>
<Menubar.Root class="w-72">
  <Menubar.Menu>
    <Menubar.Trigger>Profiles</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.RadioGroup bind:value={user}>
        <Menubar.RadioItem value="andy">Andy</Menubar.RadioItem>
        <Menubar.RadioItem value="benoit">Benoit</Menubar.RadioItem>
        <Menubar.RadioItem value="luis">Luis</Menubar.RadioItem>
      </Menubar.RadioGroup>
      <Menubar.Separator />
      <Menubar.Item inset>Edit...</Menubar.Item>
      <Menubar.Item inset>Add Profile...</Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>Theme</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.RadioGroup bind:value={theme}>
        <Menubar.RadioItem value="light">Light</Menubar.RadioItem>
        <Menubar.RadioItem value="dark">Dark</Menubar.RadioItem>
        <Menubar.RadioItem value="system">System</Menubar.RadioItem>
      </Menubar.RadioGroup>
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

View Code

## [Submenu](#submenu)

Use `Menubar.Sub`, `Menubar.SubTrigger`, and `Menubar.SubContent` for nested menus.

```svelte
<script lang="ts">
  import * as Menubar from "$lib/components/ui/menubar/index.js";
</script>
<Menubar.Root class="w-72">
  <Menubar.Menu>
    <Menubar.Trigger>File</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Sub>
        <Menubar.SubTrigger>Share</Menubar.SubTrigger>
        <Menubar.SubContent>
          <Menubar.Item>Email link</Menubar.Item>
          <Menubar.Item>Messages</Menubar.Item>
          <Menubar.Item>Notes</Menubar.Item>
        </Menubar.SubContent>
      </Menubar.Sub>
      <Menubar.Separator />
      <Menubar.Item>
        Print... <Menubar.Shortcut>P</Menubar.Shortcut>
      </Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>Edit</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Item>
        Undo <Menubar.Shortcut>Z</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item>
        Redo <Menubar.Shortcut>Z</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Separator />
      <Menubar.Sub>
        <Menubar.SubTrigger>Find</Menubar.SubTrigger>
        <Menubar.SubContent>
          <Menubar.Item>Find...</Menubar.Item>
          <Menubar.Item>Find Next</Menubar.Item>
          <Menubar.Item>Find Previous</Menubar.Item>
        </Menubar.SubContent>
      </Menubar.Sub>
      <Menubar.Separator />
      <Menubar.Item>Cut</Menubar.Item>
      <Menubar.Item>Copy</Menubar.Item>
      <Menubar.Item>Paste</Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

View Code

## [With Icons](#with-icons)

```svelte
<script lang="ts">
  import CircleQuestionMarkIcon from "@lucide/svelte/icons/circle-question-mark";
  import FileIcon from "@lucide/svelte/icons/file";
  import FolderIcon from "@lucide/svelte/icons/folder";
  import SaveIcon from "@lucide/svelte/icons/save";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import TrashIcon from "@lucide/svelte/icons/trash";
  import * as Menubar from "$lib/components/ui/menubar/index.js";
</script>
<Menubar.Root class="w-72">
  <Menubar.Menu>
    <Menubar.Trigger>File</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Item>
        <FileIcon />
        New File <Menubar.Shortcut>N</Menubar.Shortcut>
      </Menubar.Item>
      <Menubar.Item>
        <FolderIcon />
        Open Folder
      </Menubar.Item>
      <Menubar.Separator />
      <Menubar.Item>
        <SaveIcon />
        Save <Menubar.Shortcut>S</Menubar.Shortcut>
      </Menubar.Item>
    </Menubar.Content>
  </Menubar.Menu>
  <Menubar.Menu>
    <Menubar.Trigger>More</Menubar.Trigger>
    <Menubar.Content>
      <Menubar.Group>
        <Menubar.Item>
          <SettingsIcon />
          Settings
        </Menubar.Item>
        <Menubar.Item>
          <CircleQuestionMarkIcon />
          Help
        </Menubar.Item>
        <Menubar.Separator />
        <Menubar.Item variant="destructive">
          <TrashIcon />
          Delete
        </Menubar.Item>
      </Menubar.Group>
    </Menubar.Content>
  </Menubar.Menu>
</Menubar.Root>
```

View Code