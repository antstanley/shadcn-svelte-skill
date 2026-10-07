# Dropdown Menu

Displays a menu to the user  such as a set of actions or functions  triggered by a button.

[Docs](https://bits-ui.com/docs/components/dropdown-menu)

[API Reference](https://bits-ui.com/docs/components/dropdown-menu#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}
    >Open</DropdownMenu.Trigger
  >
  <DropdownMenu.Content class="w-40" align="start">
    <DropdownMenu.Group>
      <DropdownMenu.Label>My Account</DropdownMenu.Label>
      <DropdownMenu.Item>
        Profile
        <DropdownMenu.Shortcut>P</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        Billing
        <DropdownMenu.Shortcut>B</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        Settings
        <DropdownMenu.Shortcut>S</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Item>Team</DropdownMenu.Item>
      <DropdownMenu.Sub>
        <DropdownMenu.SubTrigger>Invite users</DropdownMenu.SubTrigger>
        <DropdownMenu.SubContent>
          <DropdownMenu.Item>Email</DropdownMenu.Item>
          <DropdownMenu.Item>Message</DropdownMenu.Item>
          <DropdownMenu.Separator />
          <DropdownMenu.Item>More...</DropdownMenu.Item>
        </DropdownMenu.SubContent>
      </DropdownMenu.Sub>
      <DropdownMenu.Item>
        New Team
        <DropdownMenu.Shortcut>+T</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Item>GitHub</DropdownMenu.Item>
      <DropdownMenu.Item>Support</DropdownMenu.Item>
      <DropdownMenu.Item disabled>API</DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Item>
        Log out
        <DropdownMenu.Shortcut>Q</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add dropdown-menu
```

```bash
npx shadcn-svelte@latest add dropdown-menu
```

```bash
bun x shadcn-svelte@latest add dropdown-menu
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
</script>
```

```svelte
<DropdownMenu.Root>
  <DropdownMenu.Trigger>Open</DropdownMenu.Trigger>
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Label>My Account</DropdownMenu.Label>
      <DropdownMenu.Item>Profile</DropdownMenu.Item>
      <DropdownMenu.Item>Billing</DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Item>Team</DropdownMenu.Item>
      <DropdownMenu.Item>Subscription</DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

## [Basic](#basic)

A basic dropdown menu with labels and separators.

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}
    >Open</DropdownMenu.Trigger
  >
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Label>My Account</DropdownMenu.Label>
      <DropdownMenu.Item>Profile</DropdownMenu.Item>
      <DropdownMenu.Item>Billing</DropdownMenu.Item>
      <DropdownMenu.Item>Settings</DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Item>GitHub</DropdownMenu.Item>
    <DropdownMenu.Item>Support</DropdownMenu.Item>
    <DropdownMenu.Item disabled>API</DropdownMenu.Item>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Submenu](#submenu)

Use `DropdownMenu.Sub` to nest secondary actions.

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}
    >Open</DropdownMenu.Trigger
  >
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Item>Team</DropdownMenu.Item>
      <DropdownMenu.Sub>
        <DropdownMenu.SubTrigger>Invite users</DropdownMenu.SubTrigger>
        <DropdownMenu.SubContent>
          <DropdownMenu.Item>Email</DropdownMenu.Item>
          <DropdownMenu.Item>Message</DropdownMenu.Item>
          <DropdownMenu.Sub>
            <DropdownMenu.SubTrigger>More options</DropdownMenu.SubTrigger>
            <DropdownMenu.SubContent>
              <DropdownMenu.Item>Calendly</DropdownMenu.Item>
              <DropdownMenu.Item>Slack</DropdownMenu.Item>
              <DropdownMenu.Separator />
              <DropdownMenu.Item>Webhook</DropdownMenu.Item>
            </DropdownMenu.SubContent>
          </DropdownMenu.Sub>
          <DropdownMenu.Separator />
          <DropdownMenu.Item>Advanced...</DropdownMenu.Item>
        </DropdownMenu.SubContent>
      </DropdownMenu.Sub>
      <DropdownMenu.Item>
        New Team
        <DropdownMenu.Shortcut>+T</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Shortcuts](#shortcuts)

Add `DropdownMenu.Shortcut` to show keyboard hints.

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}
    >Open</DropdownMenu.Trigger
  >
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Label>My Account</DropdownMenu.Label>
      <DropdownMenu.Item>
        Profile
        <DropdownMenu.Shortcut>P</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        Billing
        <DropdownMenu.Shortcut>B</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        Settings
        <DropdownMenu.Shortcut>S</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Item>
      Log out
      <DropdownMenu.Shortcut>Q</DropdownMenu.Shortcut>
    </DropdownMenu.Item>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Icons](#icons)

Combine icons with labels for quick scanning.

```svelte
<script lang="ts">
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import LogOutIcon from "@lucide/svelte/icons/log-out";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import UserIcon from "@lucide/svelte/icons/user";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}
    >Open</DropdownMenu.Trigger
  >
  <DropdownMenu.Content>
    <DropdownMenu.Item>
      <UserIcon />
      Profile
    </DropdownMenu.Item>
    <DropdownMenu.Item>
      <CreditCardIcon />
      Billing
    </DropdownMenu.Item>
    <DropdownMenu.Item>
      <SettingsIcon />
      Settings
    </DropdownMenu.Item>
    <DropdownMenu.Separator />
    <DropdownMenu.Item variant="destructive">
      <LogOutIcon />
      Log out
    </DropdownMenu.Item>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Checkboxes](#checkboxes)

Use `DropdownMenu.CheckboxItem` for toggles.

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  let showStatusBar = $state(true);
  let showActivityBar = $state(false);
  let showPanel = $state(false);
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="outline">Open</Button>
    {/snippet}
  </DropdownMenu.Trigger>
  <DropdownMenu.Content class="w-40">
    <DropdownMenu.Group>
      <DropdownMenu.Label>Appearance</DropdownMenu.Label>
      <DropdownMenu.CheckboxItem bind:checked={showStatusBar}
        >Status Bar</DropdownMenu.CheckboxItem
      >
      <DropdownMenu.CheckboxItem bind:checked={showActivityBar} disabled>
        Activity Bar
      </DropdownMenu.CheckboxItem>
      <DropdownMenu.CheckboxItem bind:checked={showPanel}
        >Panel</DropdownMenu.CheckboxItem
      >
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Checkboxes Icons](#checkboxes-icons)

Add icons to checkbox items.

```svelte
<script lang="ts">
  import BellIcon from "@lucide/svelte/icons/bell";
  import MailIcon from "@lucide/svelte/icons/mail";
  import MessageSquareIcon from "@lucide/svelte/icons/message-square";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  let notifications = $state({
    email: true,
    sms: false,
    push: true
  });
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}>
    Notifications
  </DropdownMenu.Trigger>
  <DropdownMenu.Content class="w-48">
    <DropdownMenu.Group>
      <DropdownMenu.Label>Notification Preferences</DropdownMenu.Label>
      <DropdownMenu.CheckboxItem bind:checked={notifications.email}>
        <MailIcon />
        Email notifications
      </DropdownMenu.CheckboxItem>
      <DropdownMenu.CheckboxItem bind:checked={notifications.sms}>
        <MessageSquareIcon />
        SMS notifications
      </DropdownMenu.CheckboxItem>
      <DropdownMenu.CheckboxItem bind:checked={notifications.push}>
        <BellIcon />
        Push notifications
      </DropdownMenu.CheckboxItem>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Radio Group](#radio-group)

Use `DropdownMenu.RadioGroup` for exclusive choices.

```svelte
<script lang="ts">
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  let position = $state("bottom");
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="outline">Open</Button>
    {/snippet}
  </DropdownMenu.Trigger>
  <DropdownMenu.Content class="w-32">
    <DropdownMenu.Group>
      <DropdownMenu.Label>Panel Position</DropdownMenu.Label>
      <DropdownMenu.RadioGroup bind:value={position}>
        <DropdownMenu.RadioItem value="top">Top</DropdownMenu.RadioItem>
        <DropdownMenu.RadioItem value="bottom">Bottom</DropdownMenu.RadioItem>
        <DropdownMenu.RadioItem value="right">Right</DropdownMenu.RadioItem>
      </DropdownMenu.RadioGroup>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Radio Icons](#radio-icons)

Show radio options with icons.

```svelte
<script lang="ts">
  import Building2Icon from "@lucide/svelte/icons/building-2";
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import WalletIcon from "@lucide/svelte/icons/wallet";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  let paymentMethod = $state("card");
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}>
    Payment Method
  </DropdownMenu.Trigger>
  <DropdownMenu.Content class="min-w-56">
    <DropdownMenu.Group>
      <DropdownMenu.Label>Select Payment Method</DropdownMenu.Label>
      <DropdownMenu.RadioGroup bind:value={paymentMethod}>
        <DropdownMenu.RadioItem value="card">
          <CreditCardIcon />
          Credit Card
        </DropdownMenu.RadioItem>
        <DropdownMenu.RadioItem value="paypal">
          <WalletIcon />
          PayPal
        </DropdownMenu.RadioItem>
        <DropdownMenu.RadioItem value="bank">
          <Building2Icon />
          Bank Transfer
        </DropdownMenu.RadioItem>
      </DropdownMenu.RadioGroup>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Destructive](#destructive)

Use `variant="destructive"` for irreversible actions.

```svelte
<script lang="ts">
  import PencilIcon from "@lucide/svelte/icons/pencil";
  import ShareIcon from "@lucide/svelte/icons/share";
  import TrashIcon from "@lucide/svelte/icons/trash";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}
    >Actions</DropdownMenu.Trigger
  >
  <DropdownMenu.Content>
    <DropdownMenu.Group>
      <DropdownMenu.Item>
        <PencilIcon />
        Edit
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        <ShareIcon />
        Share
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Item variant="destructive">
        <TrashIcon />
        Delete
      </DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Avatar](#avatar)

An account switcher dropdown triggered by an avatar.

```svelte
<script lang="ts">
  import BadgeCheckIcon from "@lucide/svelte/icons/badge-check";
  import BellIcon from "@lucide/svelte/icons/bell";
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import LogOutIcon from "@lucide/svelte/icons/log-out";
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="ghost" size="icon" class="rounded-full">
        <Avatar.Root>
          <Avatar.Image src="https://github.com/shadcn.png" alt="shadcn" />
          <Avatar.Fallback>LR</Avatar.Fallback>
        </Avatar.Root>
      </Button>
    {/snippet}
  </DropdownMenu.Trigger>
  <DropdownMenu.Content align="end">
    <DropdownMenu.Group>
      <DropdownMenu.Item>
        <BadgeCheckIcon />
        Account
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        <CreditCardIcon />
        Billing
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        <BellIcon />
        Notifications
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Item>
      <LogOutIcon />
      Sign Out
    </DropdownMenu.Item>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code

## [Complex](#complex)

A richer example combining groups, icons, and submenus.

```svelte
<script lang="ts">
  import BellIcon from "@lucide/svelte/icons/bell";
  import CircleQuestionMarkIcon from "@lucide/svelte/icons/circle-question-mark";
  import CreditCardIcon from "@lucide/svelte/icons/credit-card";
  import DownloadIcon from "@lucide/svelte/icons/download";
  import EllipsisIcon from "@lucide/svelte/icons/ellipsis";
  import EyeIcon from "@lucide/svelte/icons/eye";
  import FileIcon from "@lucide/svelte/icons/file";
  import FileCodeIcon from "@lucide/svelte/icons/file-code";
  import FileTextIcon from "@lucide/svelte/icons/file-text";
  import FolderIcon from "@lucide/svelte/icons/folder";
  import FolderOpenIcon from "@lucide/svelte/icons/folder-open";
  import FolderSearchIcon from "@lucide/svelte/icons/folder-search";
  import KeyboardIcon from "@lucide/svelte/icons/keyboard";
  import LanguagesIcon from "@lucide/svelte/icons/languages";
  import LogOutIcon from "@lucide/svelte/icons/log-out";
  import MailIcon from "@lucide/svelte/icons/mail";
  import MonitorIcon from "@lucide/svelte/icons/monitor";
  import MoonIcon from "@lucide/svelte/icons/moon";
  import PaletteIcon from "@lucide/svelte/icons/palette";
  import LayoutIcon from "@lucide/svelte/icons/panels-top-left";
  import SaveIcon from "@lucide/svelte/icons/save";
  import SettingsIcon from "@lucide/svelte/icons/settings";
  import ShieldIcon from "@lucide/svelte/icons/shield";
  import SunIcon from "@lucide/svelte/icons/sun";
  import UserIcon from "@lucide/svelte/icons/user";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  let notifications = $state({
    email: true,
    sms: false,
    push: true
  });
  let theme = $state("light");
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}>
    Complex Menu
  </DropdownMenu.Trigger>
  <DropdownMenu.Content class="w-44">
    <DropdownMenu.Group>
      <DropdownMenu.Label>File</DropdownMenu.Label>
      <DropdownMenu.Item>
        <FileIcon />
        New File
        <DropdownMenu.Shortcut>N</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        <FolderIcon />
        New Folder
        <DropdownMenu.Shortcut>N</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Sub>
        <DropdownMenu.SubTrigger>
          <FolderOpenIcon />
          Open Recent
        </DropdownMenu.SubTrigger>
        <DropdownMenu.SubContent>
          <DropdownMenu.Group>
            <DropdownMenu.Label>Recent Projects</DropdownMenu.Label>
            <DropdownMenu.Item>
              <FileCodeIcon />
              Project Alpha
            </DropdownMenu.Item>
            <DropdownMenu.Item>
              <FileCodeIcon />
              Project Beta
            </DropdownMenu.Item>
            <DropdownMenu.Sub>
              <DropdownMenu.SubTrigger>
                <EllipsisIcon />
                More Projects
              </DropdownMenu.SubTrigger>
              <DropdownMenu.SubContent>
                <DropdownMenu.Item>
                  <FileCodeIcon />
                  Project Gamma
                </DropdownMenu.Item>
                <DropdownMenu.Item>
                  <FileCodeIcon />
                  Project Delta
                </DropdownMenu.Item>
              </DropdownMenu.SubContent>
            </DropdownMenu.Sub>
          </DropdownMenu.Group>
          <DropdownMenu.Separator />
          <DropdownMenu.Group>
            <DropdownMenu.Item>
              <FolderSearchIcon />
              Browse...
            </DropdownMenu.Item>
          </DropdownMenu.Group>
        </DropdownMenu.SubContent>
      </DropdownMenu.Sub>
      <DropdownMenu.Separator />
      <DropdownMenu.Item>
        <SaveIcon />
        Save
        <DropdownMenu.Shortcut>S</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        <DownloadIcon />
        Export
        <DropdownMenu.Shortcut>E</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Label>View</DropdownMenu.Label>
      <DropdownMenu.CheckboxItem bind:checked={notifications.email}>
        <EyeIcon />
        Show Sidebar
      </DropdownMenu.CheckboxItem>
      <DropdownMenu.CheckboxItem bind:checked={notifications.sms}>
        <LayoutIcon />
        Show Status Bar
      </DropdownMenu.CheckboxItem>
      <DropdownMenu.Sub>
        <DropdownMenu.SubTrigger>
          <PaletteIcon />
          Theme
        </DropdownMenu.SubTrigger>
        <DropdownMenu.SubContent>
          <DropdownMenu.Group>
            <DropdownMenu.Label>Appearance</DropdownMenu.Label>
            <DropdownMenu.RadioGroup bind:value={theme}>
              <DropdownMenu.RadioItem value="light">
                <SunIcon />
                Light
              </DropdownMenu.RadioItem>
              <DropdownMenu.RadioItem value="dark">
                <MoonIcon />
                Dark
              </DropdownMenu.RadioItem>
              <DropdownMenu.RadioItem value="system">
                <MonitorIcon />
                System
              </DropdownMenu.RadioItem>
            </DropdownMenu.RadioGroup>
          </DropdownMenu.Group>
        </DropdownMenu.SubContent>
      </DropdownMenu.Sub>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Label>Account</DropdownMenu.Label>
      <DropdownMenu.Item>
        <UserIcon />
        Profile
        <DropdownMenu.Shortcut>P</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        <CreditCardIcon />
        Billing
      </DropdownMenu.Item>
      <DropdownMenu.Sub>
        <DropdownMenu.SubTrigger>
          <SettingsIcon />
          Settings
        </DropdownMenu.SubTrigger>
        <DropdownMenu.SubContent>
          <DropdownMenu.Group>
            <DropdownMenu.Label>Preferences</DropdownMenu.Label>
            <DropdownMenu.Item>
              <KeyboardIcon />
              Keyboard Shortcuts
            </DropdownMenu.Item>
            <DropdownMenu.Item>
              <LanguagesIcon />
              Language
            </DropdownMenu.Item>
            <DropdownMenu.Sub>
              <DropdownMenu.SubTrigger>
                <BellIcon />
                Notifications
              </DropdownMenu.SubTrigger>
              <DropdownMenu.SubContent>
                <DropdownMenu.Group>
                  <DropdownMenu.Label>Notification Types</DropdownMenu.Label>
                  <DropdownMenu.CheckboxItem bind:checked={notifications.push}>
                    <BellIcon />
                    Push Notifications
                  </DropdownMenu.CheckboxItem>
                  <DropdownMenu.CheckboxItem bind:checked={notifications.email}>
                    <MailIcon />
                    Email Notifications
                  </DropdownMenu.CheckboxItem>
                </DropdownMenu.Group>
              </DropdownMenu.SubContent>
            </DropdownMenu.Sub>
          </DropdownMenu.Group>
          <DropdownMenu.Separator />
          <DropdownMenu.Group>
            <DropdownMenu.Item>
              <ShieldIcon />
              Privacy & Security
            </DropdownMenu.Item>
          </DropdownMenu.Group>
        </DropdownMenu.SubContent>
      </DropdownMenu.Sub>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Item>
        <CircleQuestionMarkIcon />
        Help & Support
      </DropdownMenu.Item>
      <DropdownMenu.Item>
        <FileTextIcon />
        Documentation
      </DropdownMenu.Item>
    </DropdownMenu.Group>
    <DropdownMenu.Separator />
    <DropdownMenu.Group>
      <DropdownMenu.Item variant="destructive">
        <LogOutIcon />
        Sign Out
        <DropdownMenu.Shortcut>Q</DropdownMenu.Shortcut>
      </DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code