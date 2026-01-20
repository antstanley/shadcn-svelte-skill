# Alert Dialog

A modal dialog that interrupts the user with important content and expects a response.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add alert-dialog
```

```bash
npx shadcn-svelte@latest add alert-dialog
```

```bash
bun x shadcn-svelte@latest add alert-dialog
```

## Usage

```svelte
<script lang="ts">
  import * as AlertDialog from "$lib/components/ui/alert-dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>

<AlertDialog.Root>
  <AlertDialog.Trigger class={buttonVariants({ variant: "outline" })}>
    Open
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

## Components

- **AlertDialog.Root** - Root container
- **AlertDialog.Trigger** - Button that opens the dialog
- **AlertDialog.Content** - Dialog content container
- **AlertDialog.Header** - Header section
- **AlertDialog.Title** - Dialog title
- **AlertDialog.Description** - Dialog description
- **AlertDialog.Footer** - Footer with action buttons
- **AlertDialog.Cancel** - Cancel button
- **AlertDialog.Action** - Confirm action button

## API

Built on [Bits UI Alert Dialog](https://bits-ui.com/docs/components/alert-dialog).
