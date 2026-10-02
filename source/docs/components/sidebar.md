# Sidebar

A composable, themeable and customizable sidebar component.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

A sidebar that collapses to icons.

Sidebars are one of the most complex components to build. They are central to any application and often contain a lot of moving parts.

We now have a solid foundation to build on top of. Composable. Themeable. Customizable.

[Browse the Blocks Library](https://shadcn-svelte.com/blocks).

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add sidebar
```

```bash
npx shadcn-svelte@latest add sidebar
```

```bash
bun x shadcn-svelte@latest add sidebar
```

## [Usage](#usage)

src/routes/+layout.svelte

```svelte
<script lang="ts">
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
  import AppSidebar from "$lib/components/app-sidebar.svelte";
  let { children } = $props();
</script>
<Sidebar.Provider>
  <AppSidebar />
  <main>
    <Sidebar.Trigger />
    {@render children?.()}
  </main>
</Sidebar.Provider>
```

src/lib/components/app-sidebar.svelte

```svelte
<script lang="ts">
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
</script>
<Sidebar.Root>
  <Sidebar.Header />
  <Sidebar.Content>
    <Sidebar.Group />
    <Sidebar.Group />
  </Sidebar.Content>
  <Sidebar.Footer />
</Sidebar.Root>
```

## [Structure](#structure)

- **Sidebar.Provider**  Handles collapsible state and provides sidebar context to child components.
- **Sidebar.Root**  The main collapsible sidebar panel.
- **Sidebar.Header**  Sticky at the top; use for branding, titles, or workspace switchers.
- **Sidebar.Footer**  Sticky at the bottom; use for user menus, settings, or actions.
- **Sidebar.Content**  Scrollable region between the header and footer.
- **Sidebar.Group**  Groups related navigation with optional label, action, and content areas.
- **Sidebar.Menu** /
  **Sidebar.MenuItem**
   Menu structure for links, badges, actions, and nested submenus.
- **Sidebar.Rail**  Resize handle for adjusting sidebar width when applicable.
- **Sidebar.Inset**  Wraps main content when using the `inset` variant.
- **Sidebar.Trigger**  Control that toggles the sidebar open or collapsed.

![Sidebar structure](/img/sidebar/sidebar-structure.png) ![Sidebar structure](/img/sidebar/sidebar-structure-dark.png)

## [Sidebar.Provider](#sidebarprovider)

The `Sidebar.Provider` component is used to provide the sidebar context to the `Sidebar.Root` component. You should always wrap your application in a `Sidebar.Provider` component.

### [Props](#props)

| Name                          | Type                             | Description                                                                                                                                            |
| ----------------------------------------------------------- | -------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `open`         | `boolean`                 | Open state of the sidebar (bindable).                                                                                                                  |
| `onOpenChange` | `(open: boolean) => void` | A callback fired *after* the open state of the sidebar changes if uncontrolled, and *before* the sidebar opens or closes if controlled. |

### [Width](#width)

If you have a single sidebar in your application, you can use the `SIDEBAR_WIDTH` and `SIDEBAR_WIDTH_MOBILE` constants in `constants.ts` to set the width of the sidebar.

src/lib/components/ui/sidebar/constants.ts

```ts
export const SIDEBAR_WIDTH = "16rem";
export const SIDEBAR_WIDTH_MOBILE = "18rem";
```

For multiple sidebars in your application, you can use the `--sidebar-width` and `--sidebar-width-mobile` CSS variables in the `style` prop.

```svelte
<Sidebar.Provider
  style="--sidebar-width: 20rem; --sidebar-width-mobile: 20rem;"
>
  <Sidebar.Root />
</Sidebar.Provider>
```

### [Keyboard Shortcut](#keyboard-shortcut)

To trigger the sidebar, you use the `cmd+b` keyboard shortcut on Mac and `ctrl+b` on Windows.

src/lib/components/ui/sidebar/constants.ts

```ts
export const SIDEBAR_KEYBOARD_SHORTCUT = "b";
```

## [Sidebar.Root](#sidebarroot)

The main `Sidebar.Root` component used to render a collapsible sidebar.

### [Props](#props-1)

| Property                     | Type                                                                 | Description                                      |
| ---------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| `side`        | `left` or `right`                               | The side of the sidebar.                         |
| `variant`     | `sidebar`, `floating`, or `inset` | The variant of the sidebar.                      |
| `collapsible` | `offcanvas`, `icon`, or `none`    | Collapsible state of the sidebar. |

| Prop                       | Description                                                  |
| -------------------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `offcanvas` | A collapsible sidebar that slides in from the left or right. |
| `icon`      | A sidebar that collapses to icons.                           |
| `none`      | A non-collapsible sidebar.                    |

**Note:** If you use the `inset` variant, remember to wrap your main content in a `Sidebar.Inset` component.

```svelte
<Sidebar.Provider>
  <Sidebar.Root variant="inset" />
  <Sidebar.Inset>
    <main>
      {@render children?.()}
    </main>
  </Sidebar.Inset>
</Sidebar.Provider>
```

## [useSidebar](#usesidebar)

The `useSidebar` function is used to control the sidebar. It returns a reactive class instance, so it *cannot* be destructured. Additionally, it must be called during the lifecycle of the component.

```svelte
<script lang="ts">
  import { useSidebar } from "$lib/components/ui/sidebar/index.js";
  const sidebar = useSidebar();
  sidebar.state;
  sidebar.open;
  sidebar.setOpen(true);
  sidebar.openMobile;
  sidebar.setOpenMobile(true);
  sidebar.isMobile;
  sidebar.toggle();
</script>
```

| Property                       | Type                                           | Description                                             |
| ------------------------------------------------------------ | ---------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `state`         | `expanded` or `collapsed` | The current state of the sidebar.                       |
| `open`          | `boolean`                               | Whether the sidebar is open.                            |
| `setOpen`       | `(open: boolean) => void`               | Sets the open state of the sidebar.                     |
| `openMobile`    | `boolean`                               | Whether the sidebar is open on mobile.                  |
| `setOpenMobile` | `(open: boolean) => void`               | Sets the open state of the sidebar on mobile.           |
| `isMobile`      | `boolean`                               | Whether the sidebar is on mobile.                       |
| `toggle`        | `() => void`                            | Toggles the sidebar. Desktop and mobile. |

## [Sidebar.Header](#sidebarheader)

Use the `Sidebar.Header` component to add a sticky header to the sidebar.

src/lib/components/app-sidebar.svelte

```svelte
<Sidebar.Root>
  <Sidebar.Header>
    <Sidebar.Menu>
      <Sidebar.MenuItem>
        <DropdownMenu.Root>
          <DropdownMenu.Trigger>
            {#snippet child({ props })}
              <Sidebar.MenuButton {...props}>
                Select Workspace
                <ChevronDown class="ms-auto" />
              </Sidebar.MenuButton>
            {/snippet}
          </DropdownMenu.Trigger>
          <DropdownMenu.Content>
            <DropdownMenu.Item>
              <span>Acme Inc</span>
            </DropdownMenu.Item>
          </DropdownMenu.Content>
        </DropdownMenu.Root>
      </Sidebar.MenuItem>
    </Sidebar.Menu>
  </Sidebar.Header>
</Sidebar.Root>
```

## [Sidebar.Footer](#sidebarfooter)

Use the `Sidebar.Footer` component to add a sticky footer to the sidebar.

```svelte
<Sidebar.Root>
  <Sidebar.Footer>
    <Sidebar.Menu>
      <Sidebar.MenuItem>
        <Sidebar.MenuButton>
          <User2 /> Username
        </Sidebar.MenuButton>
      </Sidebar.MenuItem>
    </Sidebar.Menu>
  </Sidebar.Footer>
</Sidebar.Root>
```

## [Sidebar.Content](#sidebarcontent)

The `Sidebar.Content` component is used to wrap the content of the sidebar. This is where you add your `Sidebar.Group` components. It is scrollable.

```svelte
<Sidebar.Root>
  <Sidebar.Content>
    <Sidebar.Group />
    <Sidebar.Group />
  </Sidebar.Content>
</Sidebar.Root>
```

## [Sidebar.Group](#sidebargroup)

Use the `Sidebar.Group` component to create a section within the sidebar.

A `Sidebar.Group` has a `Sidebar.GroupLabel`, a `Sidebar.GroupContent` and an optional `Sidebar.GroupAction`.

```svelte
<Sidebar.Group>
  <Sidebar.GroupLabel>Application</Sidebar.GroupLabel>
  <Sidebar.GroupAction>
    <Plus /> <span class="sr-only">Add Project</span>
  </Sidebar.GroupAction>
  <Sidebar.GroupContent></Sidebar.GroupContent>
</Sidebar.Group>
```

To make a `Sidebar.Group` collapsible, wrap it in a `Collapsible`.

```svelte
<Collapsible.Root open class="group/collapsible">
  <Sidebar.Group>
    <Sidebar.GroupLabel>
      {#snippet child({ props })}
        <Collapsible.Trigger {...props}>
          Help
          <ChevronDown
            class="ms-auto transition-transform group-data-[state=open]/collapsible:rotate-180"
          />
        </Collapsible.Trigger>
      {/snippet}
    </Sidebar.GroupLabel>
    <Collapsible.Content>
      <Sidebar.GroupContent />
    </Collapsible.Content>
  </Sidebar.Group>
</Collapsible.Root>
```

## [Sidebar.Menu](#sidebarmenu)

The `Sidebar.Menu` component is used for building a menu within a `Sidebar.Group`.

![Sidebar menu](/img/sidebar/sidebar-menu.png) ![Sidebar menu](/img/sidebar/sidebar-menu-dark.png)

```svelte
<Sidebar.Menu>
  {#each projects as project (project.name)}
    <Sidebar.MenuItem>
      <Sidebar.MenuButton>
        {#snippet child({ props })}
          <a href={project.url} {...props}>
            <project.icon />
            <span>{project.name}</span>
          </a>
        {/snippet}
      </Sidebar.MenuButton>
    </Sidebar.MenuItem>
  {/each}
</Sidebar.Menu>
```

## [Sidebar.MenuButton](#sidebarmenubutton)

The `Sidebar.MenuButton` component is used to render a menu button within a `Sidebar.MenuItem`.

By default, the `Sidebar.MenuButton` renders a button but you can use the `child` snippet to render a different element such as an `<a>` tag.

Use the `isActive` prop to mark a menu item as active.

```svelte
<Sidebar.MenuButton isActive>
  {#snippet child({ props })}
    <a href="##" {...props}>Home</a>
  {/snippet}
</Sidebar.MenuButton>
```

## [Sidebar.MenuAction](#sidebarmenuaction)

The `Sidebar.MenuAction` component is used to render a menu action within a `Sidebar.MenuItem`.

```svelte
<Sidebar.MenuItem>
  <Sidebar.MenuButton>
    {#snippet child({ props })}
      <a href="##" {...props}>
        <House />
        <span>Home</span>
      </a>
    {/snippet}
  </Sidebar.MenuButton>
  <Sidebar.MenuAction>
    <Plus /> <span class="sr-only">Add Project</span>
  </Sidebar.MenuAction>
</Sidebar.MenuItem>
```

## [Sidebar.MenuSub](#sidebarmenusub)

The `Sidebar.MenuSub` component is used to render a submenu within a `Sidebar.Menu`.

```svelte
<Sidebar.MenuItem>
  <Sidebar.MenuButton />
  <Sidebar.MenuSub>
    <Sidebar.MenuSubItem>
      <Sidebar.MenuSubButton />
    </Sidebar.MenuSubItem>
  </Sidebar.MenuSub>
</Sidebar.MenuItem>
```

## [Sidebar.MenuBadge](#sidebarmenubadge)

The `Sidebar.MenuBadge` component is used to render a badge within a `Sidebar.MenuItem`.

```svelte
<Sidebar.MenuItem>
  <Sidebar.MenuButton />
  <Sidebar.MenuBadge>24</Sidebar.MenuBadge>
</Sidebar.MenuItem>
```

## [Sidebar.MenuSkeleton](#sidebarmenuskeleton)

The `Sidebar.MenuSkeleton` component is used to render a skeleton for a `Sidebar.Menu`.

```svelte
<Sidebar.Menu>
  {#each Array.from({ length: 5 }) as _, index (index)}
    <Sidebar.MenuItem>
      <Sidebar.MenuSkeleton />
    </Sidebar.MenuItem>
  {/each}
</Sidebar.Menu>
```

## [Sidebar.Trigger](#sidebartrigger)

Use the `Sidebar.Trigger` component to render a button that toggles the sidebar.

```svelte
<script lang="ts">
  import { useSidebar } from "$lib/components/ui/sidebar/index.js";
  const sidebar = useSidebar();
</script>
<button onclick={() => sidebar.toggle()}>Toggle Sidebar</button>
```

## [Sidebar.Rail](#sidebarrail)

The `Sidebar.Rail` component is used to render a rail within a `Sidebar.Root`. This rail can be used to toggle the sidebar.

```svelte
<Sidebar.Root>
  <Sidebar.Header />
  <Sidebar.Content>
    <Sidebar.Group />
  </Sidebar.Content>
  <Sidebar.Footer />
  <Sidebar.Rail />
</Sidebar.Root>
```

## [Controlled Sidebar](#controlled-sidebar)

Use `bind:open` to control the sidebar.

```svelte
<script lang="ts">
  import * as Sidebar from "$lib/components/ui/sidebar/index.js";
  let open = $state(false);
</script>
<Sidebar.Provider bind:open>
  <Sidebar.Root />
</Sidebar.Provider>
```

## [Theming](#theming)

We use the following CSS variables to theme the sidebar.

```css
:root {
  --sidebar: oklch(0.985 0 0);
  --sidebar-foreground: oklch(0.145 0 0);
  --sidebar-primary: oklch(0.205 0 0);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.97 0 0);
  --sidebar-accent-foreground: oklch(0.205 0 0);
  --sidebar-border: oklch(0.922 0 0);
  --sidebar-ring: oklch(0.708 0 0);
}
.dark {
  --sidebar: oklch(0.205 0 0);
  --sidebar-foreground: oklch(0.985 0 0);
  --sidebar-primary: oklch(0.488 0.243 264.376);
  --sidebar-primary-foreground: oklch(0.985 0 0);
  --sidebar-accent: oklch(0.269 0 0);
  --sidebar-accent-foreground: oklch(0.985 0 0);
  --sidebar-border: oklch(1 0 0 / 10%);
  --sidebar-ring: oklch(0.439 0 0);
}
```

## [Styling](#styling)

Here are some tips for styling the sidebar based on different states.

```svelte
<Sidebar.Root collapsible="icon">
  <Sidebar.Content>
    <Sidebar.Group class="group-data-[collapsible=icon]:hidden" />
  </Sidebar.Content>
</Sidebar.Root>
```

```svelte
<Sidebar.MenuItem>
  <Sidebar.MenuButton />
  <Sidebar.MenuAction
    class="peer-data-[active=true]/menu-button:opacity-100"
  />
</Sidebar.MenuItem>
```