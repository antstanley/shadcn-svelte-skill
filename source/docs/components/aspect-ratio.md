# Aspect Ratio

Displays content within a desired ratio.

[Docs](https://bits-ui.com/docs/components/aspect-ratio)

[API Reference](https://bits-ui.com/docs/components/aspect-ratio#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { AspectRatio } from "$lib/components/ui/aspect-ratio/index.js";
</script>
<div class="w-full max-w-sm">
 <AspectRatio ratio={16 / 9} class="rounded-lg bg-muted">
  <img
   src="https://avatar.vercel.sh/shadcn1"
   alt="Placeholder"
   class="size-full rounded-lg object-cover grayscale dark:brightness-20"
  />
 </AspectRatio>
</div>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add aspect-ratio
```

```bash
npx shadcn-svelte@latest add aspect-ratio
```

```bash
bun x shadcn-svelte@latest add aspect-ratio
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { AspectRatio } from "$lib/components/ui/aspect-ratio/index.js";
</script>
```

```svelte
<AspectRatio ratio={16 / 9}>
  <img src="..." alt="Image" class="rounded-md object-cover" />
</AspectRatio>
```

## [Square](#square)

A square aspect ratio component using the `ratio={1 / 1}` prop. This is useful for displaying images in a square format.

```svelte
<script lang="ts">
 import { AspectRatio } from "$lib/components/ui/aspect-ratio/index.js";
</script>
<div class="w-full max-w-[12rem]">
 <AspectRatio ratio={1 / 1} class="rounded-lg bg-muted">
  <img
   src="https://avatar.vercel.sh/shadcn1"
   alt="Placeholder"
   class="size-full rounded-lg object-cover grayscale dark:brightness-20"
  />
 </AspectRatio>
</div>
```

View Code

## [Portrait](#portrait)

A portrait aspect ratio component using the `ratio={9 / 16}` prop. This is useful for displaying images in a portrait format.

```svelte
<script lang="ts">
 import { AspectRatio } from "$lib/components/ui/aspect-ratio/index.js";
</script>
<div class="w-full max-w-[10rem]">
 <AspectRatio ratio={9 / 16} class="rounded-lg bg-muted">
  <img
   src="https://avatar.vercel.sh/shadcn1"
   alt="Placeholder"
   class="size-full rounded-lg object-cover grayscale dark:brightness-20"
  />
 </AspectRatio>
</div>
```

View Code