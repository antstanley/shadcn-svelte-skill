# Drawer

A drawer component for Svelte.

[Docs](https://github.com/huntabyte/vaul-svelte)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [About](#about)

Drawer is built on top of [Vaul Svelte](https://vaul-svelte.com), which is a Svelte port of [Vaul](https://vaul.emilkowal.ski) by [Emil Kowalski](https://twitter.com/emilkowalski_).

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add drawer
```

```bash
npx shadcn-svelte@latest add drawer
```

```bash
bun x shadcn-svelte@latest add drawer
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Drawer from "$lib/components/ui/drawer/index.js";
</script>
```

```svelte
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

## [Examples](#examples)

### [Sides](#sides)

Use the `direction` prop to set the side of the drawer. Available options are `top`, `right`, `bottom`, and `left`.

View Code

### [Responsive Dialog](#responsive-dialog)

You can combine the `Dialog` and `Drawer` components to create a responsive dialog. This renders a `Dialog` on desktop and a `Drawer` on mobile.

View Code