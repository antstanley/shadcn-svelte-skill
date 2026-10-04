# Alert Dialog

A modal dialog that interrupts the user with important content and expects a response.

[Docs](https://bits-ui.com/docs/components/alert-dialog)

[API Reference](https://bits-ui.com/docs/components/alert-dialog#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "outline" })}>
    Show Dialog
  </AlertDialog.Trigger>
  <AlertDialog.Content>
    <AlertDialog.Header>
      <AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
      <AlertDialog.Description>
        This action cannot be undone. This will permanently delete your account
        from our servers.
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
      <AlertDialog.Action>Continue</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add alert-dialog
```

```bash
npx shadcn-svelte@latest add alert-dialog
```

```bash
bun x shadcn-svelte@latest add alert-dialog
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
```

```svelte
<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "outline" })}>
    Show Dialog
  </AlertDialog.Trigger>
  <AlertDialog.Content>
    <AlertDialog.Header>
      <AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
      <AlertDialog.Description>
        This action cannot be undone. This will permanently delete your account
        from our servers.
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
      <AlertDialog.Action>Continue</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

## [Basic](#basic)

A basic alert dialog with a title, description, and cancel and continue buttons.

```svelte
<script lang="ts">
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "outline" })}>
    Show Dialog
  </AlertDialog.Trigger>
  <AlertDialog.Content>
    <AlertDialog.Header>
      <AlertDialog.Title>Are you absolutely sure?</AlertDialog.Title>
      <AlertDialog.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
      <AlertDialog.Action>Continue</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

View Code

## [Small](#small)

Use the `size="sm"` prop to make the alert dialog smaller.

```svelte
<script lang="ts">
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "outline" })}
    >Show Dialog</AlertDialog.Trigger
  >
  <AlertDialog.Content size="sm">
    <AlertDialog.Header>
      <AlertDialog.Title>Allow accessory to connect?</AlertDialog.Title>
      <AlertDialog.Description>
        Do you want to allow the USB accessory to connect to this device?
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel>Don't allow</AlertDialog.Cancel>
      <AlertDialog.Action>Allow</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

View Code

## [Media](#media)

Use the `AlertDialog.Media` component to add a media element such as an icon or image to the alert dialog.

```svelte
<script lang="ts">
  import CircleFadingPlusIcon from "@lucide/svelte/icons/circle-fading-plus";
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "outline" })}
    >Share Project</AlertDialog.Trigger
  >
  <AlertDialog.Content>
    <AlertDialog.Header>
      <AlertDialog.Media>
        <CircleFadingPlusIcon />
      </AlertDialog.Media>
      <AlertDialog.Title>Share this project?</AlertDialog.Title>
      <AlertDialog.Description>
        Anyone with the link will be able to view and edit this project.
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel>Cancel</AlertDialog.Cancel>
      <AlertDialog.Action>Share</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

View Code

## [Small with Media](#small-with-media)

Use the `size="sm"` prop to make the alert dialog smaller and the `AlertDialog.Media` component to add a media element such as an icon or image to the alert dialog.

```svelte
<script lang="ts">
  import BluetoothIcon from "@lucide/svelte/icons/bluetooth";
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "outline" })}
    >Show Dialog</AlertDialog.Trigger
  >
  <AlertDialog.Content size="sm">
    <AlertDialog.Header>
      <AlertDialog.Media>
        <BluetoothIcon />
      </AlertDialog.Media>
      <AlertDialog.Title>Allow accessory to connect?</AlertDialog.Title>
      <AlertDialog.Description>
        Do you want to allow the USB accessory to connect to this device?
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel>Don't allow</AlertDialog.Cancel>
      <AlertDialog.Action>Allow</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

View Code

## [Destructive](#destructive)

Use the `AlertDialog.Action` component to add a destructive action button to the alert dialog.

```svelte
<script lang="ts">
  import Trash2Icon from "@lucide/svelte/icons/trash-2";
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "destructive" })}>
    Delete Chat
  </AlertDialog.Trigger>
  <AlertDialog.Content size="sm">
    <AlertDialog.Header>
      <AlertDialog.Media
        class="bg-destructive/10 text-destructive dark:bg-destructive/20 dark:text-destructive"
      >
        <Trash2Icon />
      </AlertDialog.Media>
      <AlertDialog.Title>Delete chat?</AlertDialog.Title>
      <AlertDialog.Description>
        This will permanently delete this chat conversation. View <a href="##"
          >Settings</a
        > delete any memories saved during this chat.
      </AlertDialog.Description>
    </AlertDialog.Header>
    <AlertDialog.Footer>
      <AlertDialog.Cancel variant="outline">Cancel</AlertDialog.Cancel>
      <AlertDialog.Action variant="destructive">Delete</AlertDialog.Action>
    </AlertDialog.Footer>
  </AlertDialog.Content>
</AlertDialog.Root>
```

View Code