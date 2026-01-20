# Sidebar

A composable, themeable and customizable sidebar component.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add sidebar
```

```bash
npx shadcn-svelte@latest add sidebar
```

```bash
bun x shadcn-svelte@latest add sidebar
```

Add the sidebar CSS variables to your stylesheet for theming support.

## Core Structure

```svelte
<script lang="ts">
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
</script>

<Sidebar.Provider>
  <Sidebar.Root>
    <Sidebar.Header />
    <Sidebar.Content>
      <Sidebar.Group>
        <Sidebar.GroupLabel>Application</Sidebar.GroupLabel>
        <Sidebar.GroupContent>
          <Sidebar.Menu>
            <Sidebar.MenuItem>
              <Sidebar.MenuButton>
                Dashboard
              </Sidebar.MenuButton>
            </Sidebar.MenuItem>
          </Sidebar.Menu>
        </Sidebar.GroupContent>
      </Sidebar.Group>
    </Sidebar.Content>
    <Sidebar.Footer />
  </Sidebar.Root>
  <main>
    <Sidebar.Trigger />
    <!-- Main content -->
  </main>
</Sidebar.Provider>
```

## Components

- **Sidebar.Provider** - Manages collapsible state
- **Sidebar.Root** - Main container
- **Sidebar.Header** - Sticky header area
- **Sidebar.Footer** - Sticky footer area
- **Sidebar.Content** - Scrollable content area
- **Sidebar.Group** - Section grouping
- **Sidebar.GroupLabel** - Label for groups
- **Sidebar.GroupContent** - Content container
- **Sidebar.Menu** - Menu container
- **Sidebar.MenuItem** - Menu item wrapper
- **Sidebar.MenuButton** - Clickable menu button
- **Sidebar.MenuAction** - Action buttons
- **Sidebar.MenuBadge** - Badge indicators
- **Sidebar.MenuSub** - Submenu container
- **Sidebar.Trigger** - Toggle button
- **Sidebar.Rail** - Additional toggle rail

## Collapsible Modes

The sidebar supports three collapsible modes:

- **offcanvas** - Slides in from the side
- **icon** - Collapses to show only icons
- **none** - Fixed, non-collapsible

```svelte
<Sidebar.Root collapsible="icon">
  <!-- content -->
</Sidebar.Root>
```

## Context Hook

Use `useSidebar()` for state management:

```svelte
<script lang="ts">
  import { useSidebar } from "$lib/components/ui/sidebar/index.js";

  const sidebar = useSidebar();
  // Properties: open, isMobile, state
  // Methods: toggle(), setOpen(), openMobile, setOpenMobile
</script>

<button onclick={() => sidebar.toggle()}>Toggle</button>
```

## Menu System

Build menus with nested submenus:

```svelte
<Sidebar.Menu>
  <Sidebar.MenuItem>
    <Sidebar.MenuButton>
      <HomeIcon />
      Home
    </Sidebar.MenuButton>
  </Sidebar.MenuItem>
  <Sidebar.MenuItem>
    <Sidebar.MenuButton>
      <SettingsIcon />
      Settings
      <Sidebar.MenuBadge>5</Sidebar.MenuBadge>
    </Sidebar.MenuButton>
    <Sidebar.MenuSub>
      <Sidebar.MenuSubItem>
        <Sidebar.MenuSubButton>Profile</Sidebar.MenuSubButton>
      </Sidebar.MenuSubItem>
    </Sidebar.MenuSub>
  </Sidebar.MenuItem>
</Sidebar.Menu>
```

## Theming

Uses OKLch color variables for light and dark modes:

```css
:root {
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-border: oklch(0.922 0 0);
}

.dark {
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  /* ... */
}
```

## Customization

The code is yours - use the provided components as a starting point to build your own custom sidebar implementation.
