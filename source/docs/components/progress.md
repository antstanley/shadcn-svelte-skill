# Progress

Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

[Docs](https://bits-ui.com/docs/components/progress)

[API Reference](https://bits-ui.com/docs/components/progress#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { onMount } from "svelte";
 import { Progress } from "$lib/components/ui/progress/index.js";
 let value = $state(13);
 onMount(() => {
  const timer = setTimeout(() => (value = 66), 500);
  return () => clearTimeout(timer);
 });
</script>
<Progress {value} max={100} class="w-[60%]" />
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add progress
```

```bash
npx shadcn-svelte@latest add progress
```

```bash
bun x shadcn-svelte@latest add progress
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Progress } from "$lib/components/ui/progress/index.js";
</script>
```

```svelte
<Progress value={33} />
```

## [Label](#label)

Use a `Field` component to add a label to the progress bar.

```svelte
<script lang="ts">
 import * as Field from "$lib/components/ui/field/index.js";
 import { Progress } from "$lib/components/ui/progress/index.js";
</script>
<Field.Field class="w-full max-w-sm">
 <Field.Label for="progress-upload" class="w-full">
  <span>Upload progress</span>
  <span class="ml-auto font-normal text-muted-foreground tabular-nums">56%</span>
 </Field.Label>
 <Progress value={56} id="progress-upload" />
</Field.Field>
```

View Code

## [Controlled](#controlled)

A progress bar that can be controlled by a slider.

```svelte
<script lang="ts">
 import { Progress } from "$lib/components/ui/progress/index.js";
 import { Slider } from "$lib/components/ui/slider/index.js";
 let value = $state(50);
</script>
<div class="flex w-full max-w-sm flex-col gap-4">
 <Progress {value} />
 <Slider type="single" bind:value min={0} max={100} step={1} />
</div>
```

View Code