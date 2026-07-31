# Progress

Displays an indicator showing the completion progress of a task, typically displayed as a progress bar.

[Docs](https://bits-ui.com/docs/components/progress)

[API Reference](https://bits-ui.com/docs/components/progress#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

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