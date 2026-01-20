# Resizable

Accessible resizable panel groups and layouts with keyboard support.

## About

The Resizable component is built on top of [PaneForge](https://github.com/svecosystem/paneforge) by Huntabyte. Visit the [PaneForge documentation](https://paneforge.com) for all available props and abilities.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add resizable
```

```bash
npx shadcn-svelte@latest add resizable
```

```bash
bun x shadcn-svelte@latest add resizable
```

## Usage

```svelte
<script lang="ts">
  import * as Resizable from "$lib/components/ui/resizable/index.js";
</script>

<Resizable.PaneGroup direction="horizontal">
  <Resizable.Pane>One</Resizable.Pane>
  <Resizable.Handle />
  <Resizable.Pane>Two</Resizable.Pane>
</Resizable.PaneGroup>
```

## Examples

### Horizontal

```svelte
<Resizable.PaneGroup direction="horizontal" class="max-w-md rounded-lg border">
  <Resizable.Pane defaultSize={50}>
    <div class="flex h-[200px] items-center justify-center p-6">
      <span class="font-semibold">One</span>
    </div>
  </Resizable.Pane>
  <Resizable.Handle />
  <Resizable.Pane defaultSize={50}>
    <div class="flex h-[200px] items-center justify-center p-6">
      <span class="font-semibold">Two</span>
    </div>
  </Resizable.Pane>
</Resizable.PaneGroup>
```

### Vertical

Use the `direction` prop to set the direction:

```svelte
<Resizable.PaneGroup direction="vertical" class="min-h-[200px] max-w-md rounded-lg border">
  <Resizable.Pane defaultSize={25}>
    <div class="flex h-full items-center justify-center p-6">
      <span class="font-semibold">Header</span>
    </div>
  </Resizable.Pane>
  <Resizable.Handle />
  <Resizable.Pane defaultSize={75}>
    <div class="flex h-full items-center justify-center p-6">
      <span class="font-semibold">Content</span>
    </div>
  </Resizable.Pane>
</Resizable.PaneGroup>
```

### Nested Panels

```svelte
<Resizable.PaneGroup direction="horizontal">
  <Resizable.Pane defaultSize={50}>One</Resizable.Pane>
  <Resizable.Handle />
  <Resizable.Pane defaultSize={50}>
    <Resizable.PaneGroup direction="vertical">
      <Resizable.Pane defaultSize={25}>Two</Resizable.Pane>
      <Resizable.Handle />
      <Resizable.Pane defaultSize={75}>Three</Resizable.Pane>
    </Resizable.PaneGroup>
  </Resizable.Pane>
</Resizable.PaneGroup>
```

### With Handle

Use the `withHandle` prop on the Handle component to show a visible drag handle:

```svelte
<Resizable.Handle withHandle />
```

## Components

- **Resizable.PaneGroup** - Container for resizable panes
- **Resizable.Pane** - Individual resizable pane
- **Resizable.Handle** - Drag handle between panes

## Props

### PaneGroup

- `direction` - "horizontal" or "vertical"
- `class` - Additional CSS classes

### Pane

- `defaultSize` - Initial size (percentage)
- `minSize` - Minimum size
- `maxSize` - Maximum size
- `collapsible` - Whether the pane can collapse

### Handle

- `withHandle` - Show visible handle grip
