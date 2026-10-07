# Command

Command menu for search and quick actions.

[Docs](https://bits-ui.com/docs/components/command)

[API Reference](https://bits-ui.com/docs/components/command#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import CalculatorIcon from "@lucide/svelte/icons/calculator";
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import SmileIcon from "@lucide/svelte/icons/smile";
  import UserIcon from "@lucide/svelte/icons/user";
  import * as Command from "$lib/components/ui/command/index.js";
</script>
<Command.Root class="max-w-sm rounded-lg border">
  <Command.Input placeholder="Type a command or search..." />
  <Command.List>
    <Command.Empty>No results found.</Command.Empty>
    <Command.Group heading="Suggestions">
      <Command.Item>
        <CalendarIcon />
        <span>Calendar</span>
      </Command.Item>
      <Command.Item>
        <SmileIcon />
        <span>Search Emoji</span>
      </Command.Item>
      <Command.Item disabled>
        <CalculatorIcon />
        <span>Calculator</span>
      </Command.Item>
    </Command.Group>
    <Command.Separator />
    <Command.Group heading="Settings">
      <Command.Item>
        <UserIcon />
        <span>Profile</span>
        <Command.Shortcut>P</Command.Shortcut>
      </Command.Item>
      <Command.Item>
        <CreditCardIcon />
        <span>Billing</span>
        <Command.Shortcut>B</Command.Shortcut>
      </Command.Item>
      <Command.Item>
        <SettingsIcon />
        <span>Settings</span>
        <Command.Shortcut>S</Command.Shortcut>
      </Command.Item>
    </Command.Group>
  </Command.List>
</Command.Root>
```

View Code

## [About](#about)

The `<Command />` component uses the [`Command`](https://bits-ui.com/docs/components/command) component from [Bits UI](https://bits-ui.com), which is inspired by [`cmdk`](https://github.com/dip/cmdk).

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add command
```

```bash
npx shadcn-svelte@latest add command
```

```bash
bun x shadcn-svelte@latest add command
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Command from "$lib/components/ui/command/index.js";
</script>
```

```svelte
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

## [Basic](#basic)

A simple command menu in a dialog.

```svelte
<script lang="ts">
  import * as Command from "$lib/components/ui/command/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  let open = $state(false);
</script>
<div class="flex flex-col gap-4">
  <Button onclick={() => (open = true)} variant="outline" class="w-fit"
    >Open Menu</Button
  >
  <Command.Dialog bind:open>
    <Command.Input placeholder="Type a command or search..." />
    <Command.List>
      <Command.Empty>No results found.</Command.Empty>
      <Command.Group heading="Suggestions">
        <Command.Item>Calendar</Command.Item>
        <Command.Item>Search Emoji</Command.Item>
        <Command.Item>Calculator</Command.Item>
      </Command.Group>
    </Command.List>
  </Command.Dialog>
</div>
```

View Code

## [Shortcuts](#shortcuts)

```svelte
<script lang="ts">
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import UserIcon from "@lucide/svelte/icons/user";
  import * as Command from "$lib/components/ui/command/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  let open = $state(false);
</script>
<div class="flex flex-col gap-4">
  <Button onclick={() => (open = true)} variant="outline" class="w-fit"
    >Open Menu</Button
  >
  <Command.Dialog bind:open>
    <Command.Input placeholder="Type a command or search..." />
    <Command.List>
      <Command.Empty>No results found.</Command.Empty>
      <Command.Group heading="Settings">
        <Command.Item>
          <UserIcon />
          <span>Profile</span>
          <Command.Shortcut>P</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <CreditCardIcon />
          <span>Billing</span>
          <Command.Shortcut>B</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <SettingsIcon />
          <span>Settings</span>
          <Command.Shortcut>S</Command.Shortcut>
        </Command.Item>
      </Command.Group>
    </Command.List>
  </Command.Dialog>
</div>
```

View Code

## [Groups](#groups)

A command menu with groups, icons and separators.

```svelte
<script lang="ts">
  import CalculatorIcon from "@lucide/svelte/icons/calculator";
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import SmileIcon from "@lucide/svelte/icons/smile";
  import UserIcon from "@lucide/svelte/icons/user";
  import * as Command from "$lib/components/ui/command/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  let open = $state(false);
</script>
<div class="flex flex-col gap-4">
  <Button onclick={() => (open = true)} variant="outline" class="w-fit"
    >Open Menu</Button
  >
  <Command.Dialog bind:open>
    <Command.Input placeholder="Type a command or search..." />
    <Command.List>
      <Command.Empty>No results found.</Command.Empty>
      <Command.Group heading="Suggestions">
        <Command.Item>
          <CalendarIcon />
          <span>Calendar</span>
        </Command.Item>
        <Command.Item>
          <SmileIcon />
          <span>Search Emoji</span>
        </Command.Item>
        <Command.Item>
          <CalculatorIcon />
          <span>Calculator</span>
        </Command.Item>
      </Command.Group>
      <Command.Separator />
      <Command.Group heading="Settings">
        <Command.Item>
          <UserIcon />
          <span>Profile</span>
          <Command.Shortcut>P</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <CreditCardIcon />
          <span>Billing</span>
          <Command.Shortcut>B</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <SettingsIcon />
          <span>Settings</span>
          <Command.Shortcut>S</Command.Shortcut>
        </Command.Item>
      </Command.Group>
    </Command.List>
  </Command.Dialog>
</div>
```

View Code

## [Scrollable](#scrollable)

Scrollable command menu with multiple items.

```svelte
<script lang="ts">
  import BellIcon from "@lucide/svelte/icons/bell";
  import CalculatorIcon from "@lucide/svelte/icons/calculator";
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import CircleQuestionMarkIcon from "@lucide/svelte/icons/circle-question-mark";
  import ClipboardPasteIcon from "@lucide/svelte/icons/clipboard-paste";
  import CodeIcon from "@lucide/svelte/icons/code";
  import CopyIcon from "@lucide/svelte/icons/copy";
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import FolderIcon from "@lucide/svelte/icons/folder";
  import FolderPlusIcon from "@lucide/svelte/icons/folder-plus";
  import HouseIcon from "@lucide/svelte/icons/house";
  import ImageIcon from "@lucide/svelte/icons/image";
  import InboxIcon from "@lucide/svelte/icons/inbox";
  import LayoutGridIcon from "@lucide/svelte/icons/layout-grid";
  import ListIcon from "@lucide/svelte/icons/list";
  import PlusIcon from "@lucide/svelte/icons/plus";
  import ScissorsIcon from "@lucide/svelte/icons/scissors";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import TrashIcon from "@lucide/svelte/icons/trash";
  import UserIcon from "@lucide/svelte/icons/user";
  import ZoomInIcon from "@lucide/svelte/icons/zoom-in";
  import ZoomOutIcon from "@lucide/svelte/icons/zoom-out";
  import * as Command from "$lib/components/ui/command/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  let open = $state(false);
</script>
<div class="flex flex-col gap-4">
  <Button onclick={() => (open = true)} variant="outline" class="w-fit"
    >Open Menu</Button
  >
  <Command.Dialog bind:open>
    <Command.Input placeholder="Type a command or search..." />
    <Command.List>
      <Command.Empty>No results found.</Command.Empty>
      <Command.Group heading="Navigation">
        <Command.Item>
          <HouseIcon />
          <span>Home</span>
          <Command.Shortcut>H</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <InboxIcon />
          <span>Inbox</span>
          <Command.Shortcut>I</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <FileTextIcon />
          <span>Documents</span>
          <Command.Shortcut>D</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <FolderIcon />
          <span>Folders</span>
          <Command.Shortcut>F</Command.Shortcut>
        </Command.Item>
      </Command.Group>
      <Command.Separator />
      <Command.Group heading="Actions">
        <Command.Item>
          <PlusIcon />
          <span>New File</span>
          <Command.Shortcut>N</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <FolderPlusIcon />
          <span>New Folder</span>
          <Command.Shortcut>N</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <CopyIcon />
          <span>Copy</span>
          <Command.Shortcut>C</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <ScissorsIcon />
          <span>Cut</span>
          <Command.Shortcut>X</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <ClipboardPasteIcon />
          <span>Paste</span>
          <Command.Shortcut>V</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <TrashIcon />
          <span>Delete</span>
          <Command.Shortcut></Command.Shortcut>
        </Command.Item>
      </Command.Group>
      <Command.Separator />
      <Command.Group heading="View">
        <Command.Item>
          <LayoutGridIcon />
          <span>Grid View</span>
        </Command.Item>
        <Command.Item>
          <ListIcon />
          <span>List View</span>
        </Command.Item>
        <Command.Item>
          <ZoomInIcon />
          <span>Zoom In</span>
          <Command.Shortcut>+</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <ZoomOutIcon />
          <span>Zoom Out</span>
          <Command.Shortcut>-</Command.Shortcut>
        </Command.Item>
      </Command.Group>
      <Command.Separator />
      <Command.Group heading="Account">
        <Command.Item>
          <UserIcon />
          <span>Profile</span>
          <Command.Shortcut>P</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <CreditCardIcon />
          <span>Billing</span>
          <Command.Shortcut>B</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <SettingsIcon />
          <span>Settings</span>
          <Command.Shortcut>S</Command.Shortcut>
        </Command.Item>
        <Command.Item>
          <BellIcon />
          <span>Notifications</span>
        </Command.Item>
        <Command.Item>
          <CircleQuestionMarkIcon />
          <span>Help & Support</span>
        </Command.Item>
      </Command.Group>
      <Command.Separator />
      <Command.Group heading="Tools">
        <Command.Item>
          <CalculatorIcon />
          <span>Calculator</span>
        </Command.Item>
        <Command.Item>
          <CalendarIcon />
          <span>Calendar</span>
        </Command.Item>
        <Command.Item>
          <ImageIcon />
          <span>Image Editor</span>
        </Command.Item>
        <Command.Item>
          <CodeIcon />
          <span>Code Editor</span>
        </Command.Item>
      </Command.Group>
    </Command.List>
  </Command.Dialog>
</div>
```

View Code