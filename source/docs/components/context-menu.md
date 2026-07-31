# Context Menu

Displays a menu to the user  such as a set of actions or functions  triggered by right click.

[Docs](https://bits-ui.com/docs/components/context-menu)

[API Reference](https://bits-ui.com/docs/components/context-menu#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add context-menu
```

```bash
npx shadcn-svelte@latest add context-menu
```

```bash
bun x shadcn-svelte@latest add context-menu
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as ContextMenu from "$lib/components/ui/context-menu/index.js";
</script>
```

```svelte
<ContextMenu.Root>
  <ContextMenu.Trigger>Right click</ContextMenu.Trigger>
  <ContextMenu.Content>
    <ContextMenu.Item>Profile</ContextMenu.Item>
    <ContextMenu.Item>Billing</ContextMenu.Item>
    <ContextMenu.Item>Team</ContextMenu.Item>
    <ContextMenu.Item>Subscription</ContextMenu.Item>
  </ContextMenu.Content>
</ContextMenu.Root>
```