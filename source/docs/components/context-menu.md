# Context Menu

Displays a menu of actions triggered by a right click.

[Docs](https://bits-ui.com/docs/components/context-menu)

[API Reference](https://bits-ui.com/docs/components/context-menu#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
  let showBookmarks = $state(true);
  let showFullURLs = $state(false);
  let value = $state("pedro");
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content class="w-48">
    <ContextMenu.Group>
      <ContextMenu.Item>
        Back
        <ContextMenu.Shortcut>[</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item disabled>
        Forward
        <ContextMenu.Shortcut>]</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Reload
        <ContextMenu.Shortcut>R</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Sub>
        <ContextMenu.SubTrigger>More Tools</ContextMenu.SubTrigger>
        <ContextMenu.SubContent class="w-44">
          <ContextMenu.Group>
            <ContextMenu.Item>Save Page...</ContextMenu.Item>
            <ContextMenu.Item>Create Shortcut...</ContextMenu.Item>
            <ContextMenu.Item>Name Window...</ContextMenu.Item>
          </ContextMenu.Group>
          <ContextMenu.Separator />
          <ContextMenu.Group>
            <ContextMenu.Item>Developer Tools</ContextMenu.Item>
          </ContextMenu.Group>
          <ContextMenu.Separator />
          <ContextMenu.Group>
            <ContextMenu.Item variant="destructive">Delete</ContextMenu.Item>
          </ContextMenu.Group>
        </ContextMenu.SubContent>
      </ContextMenu.Sub>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.CheckboxItem bind:checked={showBookmarks}
        >Show Bookmarks</ContextMenu.CheckboxItem
      >
      <ContextMenu.CheckboxItem bind:checked={showFullURLs}
        >Show Full URLs</ContextMenu.CheckboxItem
      >
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.RadioGroup bind:value>
        <ContextMenu.Label>People</ContextMenu.Label>
        <ContextMenu.RadioItem value="pedro">Pedro Duarte</ContextMenu.RadioItem
        >
        <ContextMenu.RadioItem value="colm">Colm Tuite</ContextMenu.RadioItem>
      </ContextMenu.RadioGroup>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add context-menu
```

```bash
npx shadcn-svelte@latest add context-menu
```

```bash
bun x shadcn-svelte@latest add context-menu
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
```

```svelte
<ContextMenu.Root>
  <ContextMenu.Trigger>Right click here</ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Item>Profile</ContextMenu.Item>
    <ContextMenu.Item>Billing</ContextMenu.Item>
    <ContextMenu.Item>Team</ContextMenu.Item>
    <ContextMenu.Item>Subscription</ContextMenu.Item>
  </ContextMenu.Content>
</ContextMenu.Root>
```

## [Basic](#basic)

A simple context menu with a few actions.

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.Item>Back</ContextMenu.Item>
      <ContextMenu.Item disabled>Forward</ContextMenu.Item>
      <ContextMenu.Item>Reload</ContextMenu.Item>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Submenu](#submenu)

Use `ContextMenu.Sub` to nest secondary actions.

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.Item>
        Copy
        <ContextMenu.Shortcut>C</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Cut
        <ContextMenu.Shortcut>X</ContextMenu.Shortcut>
      </ContextMenu.Item>
    </ContextMenu.Group>
    <ContextMenu.Sub>
      <ContextMenu.SubTrigger>More Tools</ContextMenu.SubTrigger>
      <ContextMenu.SubContent>
        <ContextMenu.Group>
          <ContextMenu.Item>Save Page...</ContextMenu.Item>
          <ContextMenu.Item>Create Shortcut...</ContextMenu.Item>
          <ContextMenu.Item>Name Window...</ContextMenu.Item>
        </ContextMenu.Group>
        <ContextMenu.Separator />
        <ContextMenu.Group>
          <ContextMenu.Item>Developer Tools</ContextMenu.Item>
        </ContextMenu.Group>
        <ContextMenu.Separator />
        <ContextMenu.Group>
          <ContextMenu.Item variant="destructive">Delete</ContextMenu.Item>
        </ContextMenu.Group>
      </ContextMenu.SubContent>
    </ContextMenu.Sub>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Shortcuts](#shortcuts)

Add `ContextMenu.Shortcut` to show keyboard hints.

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.Item>
        Back
        <ContextMenu.Shortcut>[</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item disabled>
        Forward
        <ContextMenu.Shortcut>]</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Reload
        <ContextMenu.Shortcut>R</ContextMenu.Shortcut>
      </ContextMenu.Item>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.Item>
        Save
        <ContextMenu.Shortcut>S</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Save As...
        <ContextMenu.Shortcut>S</ContextMenu.Shortcut>
      </ContextMenu.Item>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Groups](#groups)

Group related actions and separate them with dividers.

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.Label>File</ContextMenu.Label>
      <ContextMenu.Item>
        New File
        <ContextMenu.Shortcut>N</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Open File
        <ContextMenu.Shortcut>O</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Save
        <ContextMenu.Shortcut>S</ContextMenu.Shortcut>
      </ContextMenu.Item>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.Label>Edit</ContextMenu.Label>
      <ContextMenu.Item>
        Undo
        <ContextMenu.Shortcut>Z</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Redo
        <ContextMenu.Shortcut>Z</ContextMenu.Shortcut>
      </ContextMenu.Item>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.Item>
        Cut
        <ContextMenu.Shortcut>X</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Copy
        <ContextMenu.Shortcut>C</ContextMenu.Shortcut>
      </ContextMenu.Item>
      <ContextMenu.Item>
        Paste
        <ContextMenu.Shortcut>V</ContextMenu.Shortcut>
      </ContextMenu.Item>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.Item variant="destructive">
        Delete
        <ContextMenu.Shortcut></ContextMenu.Shortcut>
      </ContextMenu.Item>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Icons](#icons)

Combine icons with labels for quick scanning.

```svelte
<script lang="ts">
  import ClipboardPasteIcon from "@lucide/svelte/icons/clipboard-paste";
  import CopyIcon from "@lucide/svelte/icons/copy";
  import ScissorsIcon from "@lucide/svelte/icons/scissors";
  import TrashIcon from "@lucide/svelte/icons/trash";
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.Item>
        <CopyIcon />
        Copy
      </ContextMenu.Item>
      <ContextMenu.Item>
        <ScissorsIcon />
        Cut
      </ContextMenu.Item>
      <ContextMenu.Item>
        <ClipboardPasteIcon />
        Paste
      </ContextMenu.Item>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.Item variant="destructive">
        <TrashIcon />
        Delete
      </ContextMenu.Item>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Checkboxes](#checkboxes)

Use `ContextMenu.CheckboxItem` for toggles.

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
  let showBookmarksBar = $state(true);
  let showFullURLs = $state(false);
  let showDeveloperTools = $state(true);
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.CheckboxItem bind:checked={showBookmarksBar}>
        Show Bookmarks Bar
      </ContextMenu.CheckboxItem>
      <ContextMenu.CheckboxItem bind:checked={showFullURLs}
        >Show Full URLs</ContextMenu.CheckboxItem
      >
      <ContextMenu.CheckboxItem bind:checked={showDeveloperTools}>
        Show Developer Tools
      </ContextMenu.CheckboxItem>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Radio](#radio)

Use `ContextMenu.RadioItem` for exclusive choices.

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
  let user = $state("pedro");
  let theme = $state("light");
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.Label>People</ContextMenu.Label>
      <ContextMenu.RadioGroup bind:value={user}>
        <ContextMenu.RadioItem value="pedro">Pedro Duarte</ContextMenu.RadioItem
        >
        <ContextMenu.RadioItem value="colm">Colm Tuite</ContextMenu.RadioItem>
      </ContextMenu.RadioGroup>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.Label>Theme</ContextMenu.Label>
      <ContextMenu.RadioGroup bind:value={theme}>
        <ContextMenu.RadioItem value="light">Light</ContextMenu.RadioItem>
        <ContextMenu.RadioItem value="dark">Dark</ContextMenu.RadioItem>
        <ContextMenu.RadioItem value="system">System</ContextMenu.RadioItem>
      </ContextMenu.RadioGroup>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Destructive](#destructive)

Use `variant="destructive"` to style the menu item as destructive.

```svelte
<script lang="ts">
  import PencilIcon from "@lucide/svelte/icons/pencil";
  import ShareIcon from "@lucide/svelte/icons/share";
  import TrashIcon from "@lucide/svelte/icons/trash";
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
<ContextMenu.Root>
  <ContextMenu.Trigger
    class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
  >
    <span class="hidden pointer-fine:inline-block">Right click here</span>
    <span class="hidden pointer-coarse:inline-block">Long press here</span>
  </ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Group>
      <ContextMenu.Item>
        <PencilIcon />
        Edit
      </ContextMenu.Item>
      <ContextMenu.Item>
        <ShareIcon />
        Share
      </ContextMenu.Item>
    </ContextMenu.Group>
    <ContextMenu.Separator />
    <ContextMenu.Group>
      <ContextMenu.Item variant="destructive">
        <TrashIcon />
        Delete
      </ContextMenu.Item>
    </ContextMenu.Group>
  </ContextMenu.Content>
</ContextMenu.Root>
```

View Code

## [Sides](#sides)

Control submenu placement with `side` and `align` props.

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
  const sides = ["top", "right", "bottom", "left"] as const;
</script>
<div class="grid w-full max-w-sm grid-cols-2 gap-4">
  {#each sides as side (side)}
    <ContextMenu.Root>
      <ContextMenu.Trigger
        class="flex aspect-video w-full max-w-xs items-center justify-center rounded-xl border border-dashed text-sm"
      >
        <span class="hidden pointer-fine:inline-block"
          >Right click ({side})</span
        >
        <span class="hidden pointer-coarse:inline-block"
          >Long press ({side})</span
        >
      </ContextMenu.Trigger>
      <ContextMenu.Content {side}>
        <ContextMenu.Group>
          <ContextMenu.Item>Back</ContextMenu.Item>
          <ContextMenu.Item>Forward</ContextMenu.Item>
          <ContextMenu.Item>Reload</ContextMenu.Item>
        </ContextMenu.Group>
      </ContextMenu.Content>
    </ContextMenu.Root>
  {/each}
</div>
```

View Code