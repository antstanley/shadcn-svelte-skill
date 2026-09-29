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

## [Examples](#examples)

### [Default](#default)

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

View Code

### [Outline](#outline)

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle variant="outline" aria-label="Toggle italic">
  <ItalicIcon class="size-4" />
</Toggle>
```

View Code

### [With Text](#with-text)

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

View Code

### [Small](#small)

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle size="sm" aria-label="Toggle italic">
  <ItalicIcon class="size-4" />
</Toggle>
```

View Code

### [Large](#large)

```svelte
<script lang="ts">
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle size="lg" aria-label="Toggle italic">
  <ItalicIcon class="size-4" />
</Toggle>
```

View Code

### [Disabled](#disabled)

```svelte
<script lang="ts">
  import UnderlineIcon from "@lucide/svelte/icons/underline";
  import { Toggle } from "$lib/components/ui/toggle/index.js";
</script>
<Toggle aria-label="Toggle underline" disabled>
  <UnderlineIcon class="size-4" />
</Toggle>
```

View Code