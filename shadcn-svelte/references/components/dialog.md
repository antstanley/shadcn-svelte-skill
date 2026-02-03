# Dialog

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

[Docs](https://bits-ui.com/docs/components/dialog)

[API Reference](https://bits-ui.com/docs/components/dialog#api-reference)

```svelte
<script lang="ts">
  import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<Dialog.Root>
  <form>
    <Dialog.Trigger class={buttonVariants({ variant: "outline" })}
      >Open Dialog</Dialog.Trigger
    >
    <Dialog.Content class="sm:max-w-[425px]">
      <Dialog.Header>
        <Dialog.Title>Edit profile</Dialog.Title>
        <Dialog.Description>
          Make changes to your profile here. Click save when you&apos;re done.
        </Dialog.Description>
      </Dialog.Header>
      <div class="grid gap-4">
        <div class="grid gap-3">
          <Label for="name-1">Name</Label>
          <Input id="name-1" name="name" defaultValue="Pedro Duarte" />
        </div>
        <div class="grid gap-3">
          <Label for="username-1">Username</Label>
          <Input id="username-1" name="username" defaultValue="@peduarte" />
        </div>
      </div>
      <Dialog.Footer>
        <Dialog.Close class={buttonVariants({ variant: "outline" })}
          >Cancel</Dialog.Close
        >
        <Button type="submit">Save changes</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </form>
</Dialog.Root>
```

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
```

```svelte
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

### Custom close button

```svelte
<script lang="ts">
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<Dialog.Root>
  <Dialog.Trigger class={buttonVariants({ variant: "outline" })}
    >Share</Dialog.Trigger
  >
  <Dialog.Content class="sm:max-w-md">
    <Dialog.Header>
      <Dialog.Title>Share link</Dialog.Title>
      <Dialog.Description>
        Anyone who has this link will be able to view this.
      </Dialog.Description>
    </Dialog.Header>
    <div class="flex items-center gap-2">
      <div class="grid flex-1 gap-2">
        <Label for="link" class="sr-only">Link</Label>
        <Input
          id="link"
          defaultValue="https://shadcn-svelte.com/docs/installation"
        />
      </div>
    </div>
    <Dialog.Footer class="sm:justify-start">
      <Dialog.Close class={buttonVariants({ variant: "secondary" })}
        >Close</Dialog.Close
      >
    </Dialog.Footer>
  </Dialog.Content>
</Dialog.Root>
```