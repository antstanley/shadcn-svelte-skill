# Toggle

A two-state button that can be either on or off.

[Docs](https://bits-ui.com/docs/components/toggle)

[API Reference](https://bits-ui.com/docs/components/toggle#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import BookmarkIcon from "@lucide/svelte/icons/bookmark";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle aria-label="Toggle bookmark" size="sm" variant="outline">
  <BookmarkIcon class="group-aria-pressed/toggle:fill-foreground" />
  Bookmark
</Toggle>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add toggle
```

```bash
npx shadcn-svelte@latest add toggle
```

```bash
bun x shadcn-svelte@latest add toggle
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
```

```svelte
<Toggle>Toggle</Toggle>
```

## [Outline](#outline)

Use `variant="outline"` for an outline style.

```svelte
<script lang="ts">
  import BoldIcon from "@lucide/svelte/icons/bold";
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<div class="flex flex-wrap items-center gap-2">
  <Toggle variant="outline" aria-label="Toggle italic">
    <ItalicIcon />
    Italic
  </Toggle>
  <Toggle variant="outline" aria-label="Toggle bold">
    <BoldIcon />
    Bold
  </Toggle>
</div>
```

View Code

## [With Text](#with-text)

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle aria-label="Toggle italic">
  <ItalicIcon />
  Italic
</Toggle>
```

View Code

## [Size](#size)

Use the `size` prop to change the size of the toggle.

```svelte
<script lang="ts">
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<div class="flex flex-wrap items-center gap-2">
  <Toggle variant="outline" aria-label="Toggle small" size="sm">Small</Toggle>
  <Toggle variant="outline" aria-label="Toggle default" size="default"
    >Default</Toggle
  >
  <Toggle variant="outline" aria-label="Toggle large" size="lg">Large</Toggle>
</div>
```

View Code

## [Disabled](#disabled)

```svelte
<script lang="ts">
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<div class="flex flex-wrap items-center gap-2">
  <Toggle aria-label="Toggle disabled" disabled>Disabled</Toggle>
  <Toggle variant="outline" aria-label="Toggle disabled outline" disabled
    >Disabled</Toggle
  >
</div>
```

View Code