# Breadcrumb

Displays the path to the current resource using a hierarchy of links.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add breadcrumb
```

```bash
npx shadcn-svelte@latest add breadcrumb
```

```bash
bun x shadcn-svelte@latest add breadcrumb
```

## Usage

```svelte
<script lang="ts">
  import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
</script>

<Breadcrumb.Root>
  <Breadcrumb.List>
    <Breadcrumb.Item>
      <Breadcrumb.Link href="/">Home</Breadcrumb.Link>
    </Breadcrumb.Item>
    <Breadcrumb.Separator />
    <Breadcrumb.Item>
      <Breadcrumb.Link href="/components">Components</Breadcrumb.Link>
    </Breadcrumb.Item>
    <Breadcrumb.Separator />
    <Breadcrumb.Item>
      <Breadcrumb.Page>Breadcrumb</Breadcrumb.Page>
    </Breadcrumb.Item>
  </Breadcrumb.List>
</Breadcrumb.Root>
```

## Examples

### Custom Separator

Use a custom component in the slot of `<Breadcrumb.Separator />`:

```svelte
<script lang="ts">
  import SlashIcon from "@lucide/svelte/icons/slash";
  import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
</script>

<Breadcrumb.Separator>
  <SlashIcon />
</Breadcrumb.Separator>
```

### With Dropdown

Compose with `<DropdownMenu />` for expandable breadcrumb items:

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import * as Breadcrumb from "$lib/components/ui/breadcrumb/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
</script>

<Breadcrumb.Item>
  <DropdownMenu.Root>
    <DropdownMenu.Trigger class="flex items-center gap-1">
      Components
      <ChevronDownIcon class="size-4" />
    </DropdownMenu.Trigger>
    <DropdownMenu.Content align="start">
      <DropdownMenu.Item>Documentation</DropdownMenu.Item>
      <DropdownMenu.Item>Themes</DropdownMenu.Item>
      <DropdownMenu.Item>GitHub</DropdownMenu.Item>
    </DropdownMenu.Content>
  </DropdownMenu.Root>
</Breadcrumb.Item>
```

### Collapsed

Use `<Breadcrumb.Ellipsis />` for collapsed states:

```svelte
<Breadcrumb.Item>
  <Breadcrumb.Ellipsis />
</Breadcrumb.Item>
```

### Responsive

Use `<Popover />` on desktop and `<Drawer />` on mobile for responsive breadcrumbs that handle long paths gracefully.

## Components

- **Breadcrumb.Root** - Container wrapper
- **Breadcrumb.List** - List container with proper semantics
- **Breadcrumb.Item** - Individual breadcrumb item
- **Breadcrumb.Link** - Clickable link
- **Breadcrumb.Page** - Current page (non-clickable)
- **Breadcrumb.Separator** - Visual separator between items
- **Breadcrumb.Ellipsis** - Collapsed items indicator
