# Toggle

A two-state button that can be either on or off.

[Docs](https://bits-ui.com/docs/components/toggle)

[API Reference](https://bits-ui.com/docs/components/toggle#api-reference)

```svelte
<script lang="ts">
  import BookmarkIcon from "@lucide/svelte/icons/bookmark";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle
  aria-label="Toggle bookmark"
  size="sm"
  variant="outline"
  class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-blue-500 data-[state=on]:*:[svg]:stroke-blue-500"
>
  <BookmarkIcon />
  Bookmark
</Toggle>
```

## Installation

```bash
pnpm dlx shadcn-svelte@latest add toggle
```

```bash
npx shadcn-svelte@latest add toggle
```

```bash
bun x shadcn-svelte@latest add toggle
```

## Usage

```svelte
<script lang="ts">
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
```

```svelte
<Toggle>Toggle</Toggle>
```

## Examples

### Default

```svelte
<script lang="ts">
  import BookmarkIcon from "@lucide/svelte/icons/bookmark";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle
  aria-label="Toggle bookmark"
  size="sm"
  variant="outline"
  class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-blue-500 data-[state=on]:*:[svg]:stroke-blue-500"
>
  <BookmarkIcon />
  Bookmark
</Toggle>
```

### Outline

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle variant="outline" aria-label="Toggle italic">
  <ItalicIcon class="size-4" />
</Toggle>
```

### With Text

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle aria-label="Toggle italic">
  <ItalicIcon class="me-2 size-4" />
  Italic
</Toggle>
```

### Small

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle size="sm" aria-label="Toggle italic">
  <ItalicIcon class="size-4" />
</Toggle>
```

### Large

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle size="lg" aria-label="Toggle italic">
  <ItalicIcon class="size-4" />
</Toggle>
```

### Disabled

```svelte
<script lang="ts">
  import UnderlineIcon from "@lucide/svelte/icons/underline";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle aria-label="Toggle underline" disabled>
  <UnderlineIcon class="size-4" />
</Toggle>
```