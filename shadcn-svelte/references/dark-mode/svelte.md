# Svelte

Adding dark mode to your Svelte/SvelteKit site.

## Installation

```bash
pnpm i mode-watcher
```

```bash
npm i mode-watcher
```

```bash
bun install mode-watcher
```

## Setup

Add the `ModeWatcher` component to your root layout:

```svelte
<!-- src/routes/+layout.svelte -->
<script lang="ts">
  import { ModeWatcher } from "mode-watcher";

  let { children } = $props();
</script>

<ModeWatcher />
{@render children()}
```

## Theme Toggle

### Light Switch

Simple toggle button with animated icons:

```svelte
<script lang="ts">
  import { toggleMode } from "mode-watcher";
  import { Button } from "$lib/components/ui/button/index.js";
  import Sun from "lucide-svelte/icons/sun";
  import Moon from "lucide-svelte/icons/moon";
</script>

<Button onclick={toggleMode} variant="outline" size="icon">
  <Sun
    class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
  />
  <Moon
    class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
  />
  <span class="sr-only">Toggle theme</span>
</Button>
```

### Dropdown Menu

More control with light, dark, and system options:

```svelte
<script lang="ts">
  import { setMode, resetMode } from "mode-watcher";
  import { Button } from "$lib/components/ui/button/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import Sun from "lucide-svelte/icons/sun";
  import Moon from "lucide-svelte/icons/moon";
</script>

<DropdownMenu.Root>
  <DropdownMenu.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="outline" size="icon">
        <Sun
          class="h-[1.2rem] w-[1.2rem] rotate-0 scale-100 transition-all dark:-rotate-90 dark:scale-0"
        />
        <Moon
          class="absolute h-[1.2rem] w-[1.2rem] rotate-90 scale-0 transition-all dark:rotate-0 dark:scale-100"
        />
        <span class="sr-only">Toggle theme</span>
      </Button>
    {/snippet}
  </DropdownMenu.Trigger>
  <DropdownMenu.Content align="end">
    <DropdownMenu.Item onclick={() => setMode("light")}>Light</DropdownMenu.Item>
    <DropdownMenu.Item onclick={() => setMode("dark")}>Dark</DropdownMenu.Item>
    <DropdownMenu.Item onclick={() => resetMode()}>System</DropdownMenu.Item>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

## mode-watcher Functions

- `toggleMode()` - Toggle between light and dark
- `setMode("light" | "dark")` - Set specific mode
- `resetMode()` - Reset to system preference
