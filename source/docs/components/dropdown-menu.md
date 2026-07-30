# Dropdown Menu

Displays a menu to the user  such as a set of actions or functions  triggered by a button.

[Docs](https://bits-ui.com/docs/components/dropdown-menu)

[API Reference](https://bits-ui.com/docs/components/dropdown-menu#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

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
      <DropdownMenu.Separator />
      <DropdownMenu.Item>Profile</DropdownMenu.Item>
      <DropdownMenu.Item>Billing</DropdownMenu.Item>
      <DropdownMenu.Item>Team</DropdownMenu.Item>
      <DropdownMenu.Item>Subscription</DropdownMenu.Item>
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

## [Examples](#examples)

### [Checkboxes](#checkboxes)

View Code

### [Radio Group](#radio-group)

View Code

### [Dialog](#dialog)

This example shows how to open a dialog from a dropdown menu.

```svelte
<DropdownMenu.Root>
  <DropdownMenu.Trigger class={buttonVariants({ variant: "outline" })}>
    Actions
  </DropdownMenu.Trigger>
</DropdownMenu.Root>
```

View Code

## [Changelog](#changelog)

### [2024-10-30 Classes for DropdownMenu.SubTrigger](#2024-10-30-classes-for-dropdownmenusubtrigger)

- Added `gap-2 [&_svg]:pointer-events-none [&_svg]:size-4 [&_svg]:shrink-0` to the `<DropdownMenu.SubTrigger>` to automatically style icon inside the dropdown menu sub trigger.
- Removed `size-4` from the icon inside the `<DropdownMenu.SubTrigger>` since it is now handled by the parent `<DropdownMenu.SubTrigger>` .