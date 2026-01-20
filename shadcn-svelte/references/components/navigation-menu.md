# Navigation Menu

A collection of links for navigating websites.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add navigation-menu
```

```bash
npx shadcn-svelte@latest add navigation-menu
```

```bash
bun x shadcn-svelte@latest add navigation-menu
```

## Usage

```svelte
<script lang="ts">
  import * as NavigationMenu from "$lib/components/ui/navigation-menu/index.js";
</script>

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

## Examples

### With Dropdown Content

```svelte
<script lang="ts">
  import * as NavigationMenu from "$lib/components/ui/navigation-menu/index.js";
  import { cn } from "$lib/utils.js";

  const components = [
    { title: "Alert Dialog", href: "/docs/components/alert-dialog", description: "A modal dialog..." },
    { title: "Hover Card", href: "/docs/components/hover-card", description: "Preview content..." },
    // ... more items
  ];
</script>

<NavigationMenu.Root>
  <NavigationMenu.List>
    <NavigationMenu.Item>
      <NavigationMenu.Trigger>Components</NavigationMenu.Trigger>
      <NavigationMenu.Content>
        <ul class="grid w-[400px] gap-2 p-2 md:grid-cols-2">
          {#each components as component}
            <li>
              <NavigationMenu.Link>
                {#snippet child()}
                  <a href={component.href} class="block p-3 rounded-md hover:bg-accent">
                    <div class="text-sm font-medium">{component.title}</div>
                    <p class="text-sm text-muted-foreground">{component.description}</p>
                  </a>
                {/snippet}
              </NavigationMenu.Link>
            </li>
          {/each}
        </ul>
      </NavigationMenu.Content>
    </NavigationMenu.Item>
  </NavigationMenu.List>
</NavigationMenu.Root>
```

### Simple Link

Use `navigationMenuTriggerStyle()` for standalone links:

```svelte
<script lang="ts">
  import { navigationMenuTriggerStyle } from "$lib/components/ui/navigation-menu/navigation-menu-trigger.svelte";
</script>

<NavigationMenu.Link>
  {#snippet child()}
    <a href="/docs" class={navigationMenuTriggerStyle()}>Docs</a>
  {/snippet}
</NavigationMenu.Link>
```

### With Icons

```svelte
<NavigationMenu.Link href="#" class="flex-row items-center gap-2">
  <CircleCheckIcon />
  Done
</NavigationMenu.Link>
```

## Components

- **NavigationMenu.Root** - Container with viewport prop for mobile
- **NavigationMenu.List** - List of navigation items
- **NavigationMenu.Item** - Individual navigation item
- **NavigationMenu.Trigger** - Button that opens content
- **NavigationMenu.Content** - Dropdown content area
- **NavigationMenu.Link** - Navigation link

## API

Built on [Bits UI Navigation Menu](https://bits-ui.com/docs/components/navigation-menu).
