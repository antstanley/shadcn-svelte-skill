# Toggle Group

A set of two-state buttons that can be toggled on or off.

[Docs](https://bits-ui.com/docs/components/toggle-group)

[API Reference](https://bits-ui.com/docs/components/toggle-group#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import BookmarkIcon from "@lucide/svelte/icons/bookmark";
  import HeartIcon from "@lucide/svelte/icons/heart";
  import StarIcon from "@lucide/svelte/icons/star";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root type="multiple" variant="outline" spacing={2} size="sm">
  <ToggleGroup.Item
    value="star"
    aria-label="Toggle star"
    class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-yellow-500 data-[state=on]:*:[svg]:stroke-yellow-500"
  >
    <StarIcon />
    Star
  </ToggleGroup.Item>
  <ToggleGroup.Item
    value="heart"
    aria-label="Toggle heart"
    class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-red-500 data-[state=on]:*:[svg]:stroke-red-500"
  >
    <HeartIcon />
    Heart
  </ToggleGroup.Item>
  <ToggleGroup.Item
    value="bookmark"
    aria-label="Toggle bookmark"
    class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-blue-500 data-[state=on]:*:[svg]:stroke-blue-500"
  >
    <BookmarkIcon />
    Bookmark
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add toggle-group
```

```bash
npx shadcn-svelte@latest add toggle-group
```

```bash
bun x shadcn-svelte@latest add toggle-group
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
```

```svelte
<ToggleGroup.Root type="single">
  <ToggleGroup.Item value="a">A</ToggleGroup.Item>
  <ToggleGroup.Item value="b">B</ToggleGroup.Item>
  <ToggleGroup.Item value="c">C</ToggleGroup.Item>
</ToggleGroup.Root>
```

## [Examples](#examples)

### [Outline](#outline)

```svelte
<script lang="ts">
  import BoldIcon from "@lucide/svelte/icons/bold";
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import UnderlineIcon from "@lucide/svelte/icons/underline";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root variant="outline" type="multiple">
  <ToggleGroup.Item value="bold" aria-label="Toggle bold">
    <BoldIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="italic" aria-label="Toggle italic">
    <ItalicIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="strikethrough" aria-label="Toggle strikethrough">
    <UnderlineIcon class="size-4" />
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

### [Single](#single)

```svelte
<script lang="ts">
  import BoldIcon from "@lucide/svelte/icons/bold";
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import UnderlineIcon from "@lucide/svelte/icons/underline";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root type="single">
  <ToggleGroup.Item value="bold" aria-label="Toggle bold">
    <BoldIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="italic" aria-label="Toggle italic">
    <ItalicIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="strikethrough" aria-label="Toggle strikethrough">
    <UnderlineIcon class="size-4" />
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

### [Small](#small)

```svelte
<script lang="ts">
  import BoldIcon from "@lucide/svelte/icons/bold";
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import UnderlineIcon from "@lucide/svelte/icons/underline";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root size="sm" type="single">
  <ToggleGroup.Item value="bold" aria-label="Toggle bold">
    <BoldIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="italic" aria-label="Toggle italic">
    <ItalicIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="strikethrough" aria-label="Toggle strikethrough">
    <UnderlineIcon class="size-4" />
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

### [Large](#large)

```svelte
<script lang="ts">
  import BoldIcon from "@lucide/svelte/icons/bold";
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import UnderlineIcon from "@lucide/svelte/icons/underline";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root size="lg" type="multiple">
  <ToggleGroup.Item value="bold" aria-label="Toggle bold">
    <BoldIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="italic" aria-label="Toggle italic">
    <ItalicIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="strikethrough" aria-label="Toggle strikethrough">
    <UnderlineIcon class="size-4" />
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

### [Disabled](#disabled)

```svelte
<script lang="ts">
  import BoldIcon from "@lucide/svelte/icons/bold";
  import ItalicIcon from "@lucide/svelte/icons/italic";
  import UnderlineIcon from "@lucide/svelte/icons/underline";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root disabled type="single">
  <ToggleGroup.Item value="bold" aria-label="Toggle bold">
    <BoldIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="italic" aria-label="Toggle italic">
    <ItalicIcon class="size-4" />
  </ToggleGroup.Item>
  <ToggleGroup.Item value="strikethrough" aria-label="Toggle strikethrough">
    <UnderlineIcon class="size-4" />
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code

### [Spacing](#spacing)

Use `spacing={2}` to add spacing between toggle group items.

```svelte
<script lang="ts">
  import BookmarkIcon from "@lucide/svelte/icons/bookmark";
  import HeartIcon from "@lucide/svelte/icons/heart";
  import StarIcon from "@lucide/svelte/icons/star";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
</script>
<ToggleGroup.Root type="multiple" variant="outline" spacing={2} size="sm">
  <ToggleGroup.Item
    value="star"
    aria-label="Toggle star"
    class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-yellow-500 data-[state=on]:*:[svg]:stroke-yellow-500"
  >
    <StarIcon />
    Star
  </ToggleGroup.Item>
  <ToggleGroup.Item
    value="heart"
    aria-label="Toggle heart"
    class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-red-500 data-[state=on]:*:[svg]:stroke-red-500"
  >
    <HeartIcon />
    Heart
  </ToggleGroup.Item>
  <ToggleGroup.Item
    value="bookmark"
    aria-label="Toggle bookmark"
    class="data-[state=on]:bg-transparent data-[state=on]:*:[svg]:fill-blue-500 data-[state=on]:*:[svg]:stroke-blue-500"
  >
    <BookmarkIcon />
    Bookmark
  </ToggleGroup.Item>
</ToggleGroup.Root>
```

View Code