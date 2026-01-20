# Drawer

A drawer component for Svelte.

## About

Drawer is built on top of [Vaul Svelte](https://vaul-svelte.com), which is a Svelte port of [Vaul](https://vaul.emilkowal.ski) by Emil Kowalski.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add drawer
```

```bash
npx shadcn-svelte@latest add drawer
```

```bash
bun x shadcn-svelte@latest add drawer
```

## Usage

```svelte
<script lang="ts">
  import * as Drawer from "$lib/components/ui/drawer/index.js";
</script>

<Drawer.Root>
  <Drawer.Trigger>Open</Drawer.Trigger>
  <Drawer.Content>
    <Drawer.Header>
      <Drawer.Title>Are you sure absolutely sure?</Drawer.Title>
      <Drawer.Description>This action cannot be undone.</Drawer.Description>
    </Drawer.Header>
    <Drawer.Footer>
      <Button>Submit</Button>
      <Drawer.Close>Cancel</Drawer.Close>
    </Drawer.Footer>
  </Drawer.Content>
</Drawer.Root>
```

## Examples

### Responsive Dialog

Combine Dialog and Drawer for responsive behavior - Dialog on desktop, Drawer on mobile:

```svelte
<script lang="ts">
  import { MediaQuery } from "svelte/reactivity";
  import * as Dialog from "$lib/components/ui/dialog/index.js";
  import * as Drawer from "$lib/components/ui/drawer/index.js";
  import { Button, buttonVariants } from "$lib/components/ui/button/index.js";

  let open = $state(false);
  const isDesktop = new MediaQuery("(min-width: 768px)");
</script>

{#if isDesktop.current}
  <Dialog.Root bind:open>
    <Dialog.Trigger class={buttonVariants({ variant: "outline" })}>
      Edit Profile
    </Dialog.Trigger>
    <Dialog.Content>
      <!-- Dialog content -->
    </Dialog.Content>
  </Dialog.Root>
{:else}
  <Drawer.Root bind:open>
    <Drawer.Trigger class={buttonVariants({ variant: "outline" })}>
      Edit Profile
    </Drawer.Trigger>
    <Drawer.Content>
      <Drawer.Header class="text-start">
        <Drawer.Title>Edit profile</Drawer.Title>
        <Drawer.Description>
          Make changes to your profile here.
        </Drawer.Description>
      </Drawer.Header>
      <!-- Drawer content -->
      <Drawer.Footer>
        <Drawer.Close class={buttonVariants({ variant: "outline" })}>
          Cancel
        </Drawer.Close>
      </Drawer.Footer>
    </Drawer.Content>
  </Drawer.Root>
{/if}
```

## Components

- **Drawer.Root** - Root container
- **Drawer.Trigger** - Button that opens the drawer
- **Drawer.Content** - Drawer content container
- **Drawer.Header** - Header section
- **Drawer.Title** - Drawer title
- **Drawer.Description** - Drawer description
- **Drawer.Footer** - Footer section
- **Drawer.Close** - Close button
