# Badge

Displays a badge or a component that looks like a badge.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { Badge } from "$lib/components/ui/badge/index.js";
</script>
<div class="flex w-full flex-wrap justify-center gap-2">
 <Badge>Badge</Badge>
 <Badge variant="secondary">Secondary</Badge>
 <Badge variant="destructive">Destructive</Badge>
 <Badge variant="outline">Outline</Badge>
</div>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add badge
```

```bash
npx shadcn-svelte@latest add badge
```

```bash
bun x shadcn-svelte@latest add badge
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Badge } from "$lib/components/ui/badge/index.js";
</script>
```

```svelte
<Badge variant="default | outline | secondary | destructive">Badge</Badge>
```

## [Variants](#variants)

Use the `variant` prop to change the variant of the badge.

```svelte
<script lang="ts">
 import { Badge } from "$lib/components/ui/badge/index.js";
</script>
<div class="flex flex-wrap gap-2">
 <Badge>Default</Badge>
 <Badge variant="secondary">Secondary</Badge>
 <Badge variant="destructive">Destructive</Badge>
 <Badge variant="outline">Outline</Badge>
 <Badge variant="ghost">Ghost</Badge>
</div>
```

View Code

## [With Icon](#with-icon)

You can render an icon inside the badge. Use `data-icon="inline-start"` to render the icon on the left and `data-icon="inline-end"` to render the icon on the right.

```svelte
<script lang="ts">
 import BadgeCheckIcon from "@lucide/svelte/icons/badge-check";
 import BookmarkIcon from "@lucide/svelte/icons/bookmark";
 import { Badge } from "$lib/components/ui/badge/index.js";
</script>
<div class="flex flex-wrap gap-2">
 <Badge variant="secondary">
  <BadgeCheckIcon data-icon="inline-start" />
  Verified
 </Badge>
 <Badge variant="outline">
  Bookmark
  <BookmarkIcon data-icon="inline-end" />
 </Badge>
</div>
```

View Code

## [With Spinner](#with-spinner)

You can render a spinner inside the badge. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` prop to the spinner.

```svelte
<script lang="ts">
 import { Badge } from "$lib/components/ui/badge/index.js";
 import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex flex-wrap gap-2">
 <Badge variant="destructive">
  <Spinner data-icon="inline-start" />
  Deleting
 </Badge>
 <Badge variant="secondary">
  Generating
  <Spinner data-icon="inline-end" />
 </Badge>
</div>
```

View Code

## [Link](#link)

Use the `href` prop to render a link as a badge.

```svelte
<script lang="ts">
 import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
 import { Badge } from "$lib/components/ui/badge/index.js";
</script>
<Badge href="#link">
 Open Link <ArrowUpRightIcon data-icon="inline-end" />
</Badge>
```

View Code

## [Custom Colors](#custom-colors)

You can customize the colors of a badge by adding custom classes such as `bg-green-50 dark:bg-green-800` to the `Badge` component.

```svelte
<script lang="ts">
 import { Badge } from "$lib/components/ui/badge/index.js";
</script>
<div class="flex flex-wrap gap-2">
 <Badge class="bg-blue-50 text-blue-700 dark:bg-blue-950 dark:text-blue-300">Blue</Badge>
 <Badge class="bg-green-50 text-green-700 dark:bg-green-950 dark:text-green-300">Green</Badge>
 <Badge class="bg-sky-50 text-sky-700 dark:bg-sky-950 dark:text-sky-300">Sky</Badge>
 <Badge class="bg-purple-50 text-purple-700 dark:bg-purple-950 dark:text-purple-300">Purple</Badge>
 <Badge class="bg-red-50 text-red-700 dark:bg-red-950 dark:text-red-300">Red</Badge>
</div>
```

View Code