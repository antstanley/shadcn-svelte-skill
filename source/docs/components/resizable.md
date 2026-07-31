# Resizable

Accessible resizable panel groups and layouts with keyboard support.

[Docs](https://www.paneforge.com)

[API Reference](https://www.paneforge.com/docs/components/pane-group)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [About](#about)

The `Resizable` component is built on top of [PaneForge](https://github.com/svecosystem/paneforge) by [Huntabyte](https://github.com/huntabyte). Visit the [PaneForge documentation](https://paneforge.com) for all the available props and abilities of the `Resizable` component.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add resizable
```

```bash
npx shadcn-svelte@latest add resizable
```

```bash
bun x shadcn-svelte@latest add resizable
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Resizable from "$lib/components/ui/resizable/index.js";
</script>
```

```svelte
<Resizable.PaneGroup direction="horizontal">
  <Resizable.Pane>One</Resizable.Pane>
  <Resizable.Handle />
  <Resizable.Pane>Two</Resizable.Pane>
</Resizable.PaneGroup>
```

## [Examples](#examples)

### [Vertical](#vertical)

Use the `direction` prop to set the direction of the resizable panels.

View Code

```svelte
<script lang="ts">
  import * as Resizable from "$lib/components/ui/resizable/index.js";
</script>
<Resizable.PaneGroup direction="vertical">
  <Resizable.Pane>One</Resizable.Pane>
  <Resizable.Handle />
  <Resizable.Pane>Two</Resizable.Pane>
</Resizable.PaneGroup>
```

### [Handle](#handle)

You can set or hide the handle by using the `withHandle` prop on the `ResizableHandle` component.

View Code

```svelte
<script lang="ts">
  import * as Resizable from "$lib/components/ui/resizable/index.js";
</script>
<Resizable.PaneGroup direction="vertical">
  <Resizable.Pane>One</Resizable.Pane>
  <Resizable.Handle withHandle />
  <Resizable.Pane>Two</Resizable.Pane>
</Resizable.PaneGroup>
```