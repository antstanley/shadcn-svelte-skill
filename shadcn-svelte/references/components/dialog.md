# Dialog

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add dialog
```

```bash
npx shadcn-svelte@latest add dialog
```

```bash
bun x shadcn-svelte@latest add dialog
```

## Usage

```svelte
<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog/index.js";
</script>

<Dialog.Root>
  <Dialog.Trigger>Open</Dialog.Trigger>
  <Dialog.Content>
    <Dialog.Header>
      <Dialog.Title>Are you sure absolutely sure?</Dialog.Title>
      <Dialog.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </Dialog.Description>
    </Dialog.Header>
  </Dialog.Content>
</Dialog.Root>
```

## Examples

### With Form

```svelte
<script lang="ts">
  import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<Dialog.Root>
  <Dialog.Trigger class={buttonVariants({ variant: "outline" })}>
    Edit Profile
  </Dialog.Trigger>
  <Dialog.Content class="sm:max-w-[425px]">
    <Dialog.Header>
      <Dialog.Title>Edit profile</Dialog.Title>
      <Dialog.Description>
        Make changes to your profile here. Click save when you're done.
      </Dialog.Description>
    </Dialog.Header>
    <div class="grid gap-4">
      <div class="grid gap-3">
        <Label for="name">Name</Label>
        <Input id="name" value="Pedro Duarte" />
      </div>
      <div class="grid gap-3">
        <Label for="username">Username</Label>
        <Input id="username" value="@peduarte" />
      </div>
    </div>
    <Dialog.Footer>
      <Dialog.Close class={buttonVariants({ variant: "outline" })}>
        Cancel
      </Dialog.Close>
      <Button type="submit">Save changes</Button>
    </Dialog.Footer>
  </Dialog.Content>
</Dialog.Root>
```

### Custom Close Button

```svelte
<Dialog.Footer class="sm:justify-start">
  <Dialog.Close class={buttonVariants({ variant: "secondary" })}>
    Close
  </Dialog.Close>
</Dialog.Footer>
```

## Components

- **Dialog.Root** - Root container
- **Dialog.Trigger** - Button that opens the dialog
- **Dialog.Content** - Dialog content container
- **Dialog.Header** - Header section
- **Dialog.Title** - Dialog title
- **Dialog.Description** - Dialog description
- **Dialog.Footer** - Footer section
- **Dialog.Close** - Close button

## API

Built on [Bits UI Dialog](https://bits-ui.com/docs/components/dialog).
