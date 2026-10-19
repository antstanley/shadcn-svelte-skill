# Dialog

A window overlaid on either the primary window or another dialog window, rendering the content underneath inert.

[Docs](https://bits-ui.com/docs/components/dialog)

[API Reference](https://bits-ui.com/docs/components/dialog#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import * as Field from "$lib/components/ui/field/index.js";
  import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<Dialog.Root>
  <form>
    <Dialog.Trigger
      type="button"
      class={buttonVariants({ variant: "outline" })}
    >
      Open Dialog
    </Dialog.Trigger>
    <Dialog.Content class="sm:max-w-sm">
      <Dialog.Header>
        <Dialog.Title>Edit profile</Dialog.Title>
        <Dialog.Description>
          Make changes to your profile here. Click save when you&apos;re done.
        </Dialog.Description>
      </Dialog.Header>
      <Field.Group>
        <Field.Field>
          <Label for="name-1">Name</Label>
          <Input id="name-1" name="name" defaultValue="Pedro Duarte" />
        </Field.Field>
        <Field.Field>
          <Label for="username-1">Username</Label>
          <Input id="username-1" name="username" defaultValue="@peduarte" />
        </Field.Field>
      </Field.Group>
      <Dialog.Footer>
        <Dialog.Close
          type="button"
          class={buttonVariants({ variant: "outline" })}
        >
          Cancel
        </Dialog.Close>
        <Button type="submit">Save changes</Button>
      </Dialog.Footer>
    </Dialog.Content>
  </form>
</Dialog.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add dialog
```

```bash
npx shadcn-svelte@latest add dialog
```

```bash
bun x shadcn-svelte@latest add dialog
```

## [Usage](#usage)

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
      <Dialog.Title>Are you absolutely sure?</Dialog.Title>
      <Dialog.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </Dialog.Description>
    </Dialog.Header>
  </Dialog.Content>
</Dialog.Root>
```

## [Custom Close Button](#custom-close-button)

Replace the default close control with your own button.

```svelte
<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
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
      <Dialog.Description
        >Anyone who has this link will be able to view this.</Dialog.Description
      >
    </Dialog.Header>
    <div class="flex items-center gap-2">
      <div class="grid flex-1 gap-2">
        <Label for="link" class="sr-only">Link</Label>
        <Input
          id="link"
          defaultValue="https://shadcn-svelte.com/docs/installation"
          readonly
        />
      </div>
    </div>
    <Dialog.Footer class="sm:justify-start">
      <Dialog.Close type="button" class={buttonVariants()}>Close</Dialog.Close>
    </Dialog.Footer>
  </Dialog.Content>
</Dialog.Root>
```

View Code

## [No Close Button](#no-close-button)

Use `showCloseButton={false}` to hide the close button.

```svelte
<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Dialog.Root>
  <Dialog.Trigger class={buttonVariants({ variant: "outline" })}
    >No Close Button</Dialog.Trigger
  >
  <Dialog.Content showCloseButton={false}>
    <Dialog.Header>
      <Dialog.Title>No Close Button</Dialog.Title>
      <Dialog.Description>
        This dialog doesn't have a close button in the top-right corner.
      </Dialog.Description>
    </Dialog.Header>
  </Dialog.Content>
</Dialog.Root>
```

View Code

## [Sticky Footer](#sticky-footer)

Keep actions visible while the content scrolls.

```svelte
<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Dialog.Root>
  <Dialog.Trigger class={buttonVariants({ variant: "outline" })}
    >Sticky Footer</Dialog.Trigger
  >
  <Dialog.Content>
    <Dialog.Header>
      <Dialog.Title>Sticky Footer</Dialog.Title>
      <Dialog.Description>
        This dialog has a sticky footer that stays visible while the content
        scrolls.
      </Dialog.Description>
    </Dialog.Header>
    <div class="-mx-4 no-scrollbar max-h-[50vh] overflow-y-auto px-4">
      {#each { length: 10 } as _, i (i)}
        <p class="mb-4 leading-normal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      {/each}
    </div>
    <Dialog.Footer>
      <Dialog.Close class={buttonVariants({ variant: "outline" })}
        >Close</Dialog.Close
      >
    </Dialog.Footer>
  </Dialog.Content>
</Dialog.Root>
```

View Code

## [Scrollable Content](#scrollable-content)

Long content can scroll while the header stays in view.

```svelte
<script lang="ts">
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Dialog.Root>
  <Dialog.Trigger class={buttonVariants({ variant: "outline" })}
    >Scrollable Content</Dialog.Trigger
  >
  <Dialog.Content>
    <Dialog.Header>
      <Dialog.Title>Scrollable Content</Dialog.Title>
      <Dialog.Description
        >This is a dialog with scrollable content.</Dialog.Description
      >
    </Dialog.Header>
    <div class="-mx-4 no-scrollbar max-h-[50vh] overflow-y-auto px-4">
      {#each { length: 10 } as _, i (i)}
        <p class="mb-4 leading-normal">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </p>
      {/each}
    </div>
  </Dialog.Content>
</Dialog.Root>
```

View Code