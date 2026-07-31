# Navigation Menu

A collection of links for navigating websites.

[Docs](https://bits-ui.com/docs/components/navigation-menu)

[API Reference](https://bits-ui.com/docs/components/navigation-menu#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add navigation-menu
```

```bash
npx shadcn-svelte@latest add navigation-menu
```

```bash
bun x shadcn-svelte@latest add navigation-menu
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as NavigationMenu from "$lib/components/ui/navigation-menu/index.js";
</script>
```

```svelte
<NavigationMenu.Root>
  <NavigationMenu.List>
    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Item One</NavigationMenu.Trigger>
      <NavigationMenu.Content>
        <NavigationMenu.Link>Link</NavigationMenu.Link>
      </NavigationMenu.Content>
    </NavigationMenu.Item>
  </NavigationMenu.List>
</NavigationMenu.Root>
```