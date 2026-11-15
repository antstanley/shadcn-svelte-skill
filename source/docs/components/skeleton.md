# Skeleton

Use to show a placeholder while content is loading.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
<div class="flex items-center gap-4">
 <Skeleton class="size-12 rounded-full" />
 <div class="space-y-2">
  <Skeleton class="h-4 w-[250px]" />
  <Skeleton class="h-4 w-[200px]" />
 </div>
</div>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add skeleton
```

```bash
npx shadcn-svelte@latest add skeleton
```

```bash
bun x shadcn-svelte@latest add skeleton
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
```

```svelte
<Skeleton class="h-[20px] w-[100px] rounded-full" />
```

## [Avatar](#avatar)

```svelte
<script lang="ts">
 import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
<div class="flex w-fit items-center gap-4">
 <Skeleton class="size-10 shrink-0 rounded-full" />
 <div class="grid gap-2">
  <Skeleton class="h-4 w-[150px]" />
  <Skeleton class="h-4 w-[100px]" />
 </div>
</div>
```

View Code

## [Card](#card)

```svelte
<script lang="ts">
 import * as Card from "$lib/components/ui/card/index.js";
 import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
<Card.Root class="w-full max-w-xs">
 <Card.Header>
  <Skeleton class="h-4 w-2/3" />
  <Skeleton class="h-4 w-1/2" />
 </Card.Header>
 <Card.Content>
  <Skeleton class="aspect-video w-full" />
 </Card.Content>
</Card.Root>
```

View Code

## [Text](#text)

```svelte
<script lang="ts">
 import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
<div class="flex w-full max-w-xs flex-col gap-2">
 <Skeleton class="h-4 w-full" />
 <Skeleton class="h-4 w-full" />
 <Skeleton class="h-4 w-3/4" />
</div>
```

View Code

## [Form](#form)

```svelte
<script lang="ts">
 import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
<div class="flex w-full max-w-xs flex-col gap-7">
 <div class="flex flex-col gap-3">
  <Skeleton class="h-4 w-20" />
  <Skeleton class="h-8 w-full" />
 </div>
 <div class="flex flex-col gap-3">
  <Skeleton class="h-4 w-24" />
  <Skeleton class="h-8 w-full" />
 </div>
 <Skeleton class="h-8 w-24" />
</div>
```

View Code

## [Table](#table)

```svelte
<script lang="ts">
 import { Skeleton } from "$lib/components/ui/skeleton/index.js";
</script>
<div class="flex w-full max-w-sm flex-col gap-2">
 {#each { length: 5 } as _, i (i)}
  <div class="flex gap-4">
   <Skeleton class="h-4 flex-1" />
   <Skeleton class="h-4 w-24" />
   <Skeleton class="h-4 w-20" />
  </div>
 {/each}
</div>
```

View Code