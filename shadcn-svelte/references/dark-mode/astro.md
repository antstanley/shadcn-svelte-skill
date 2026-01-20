# Astro

Adding dark mode to your Astro site.

## Setup

### Add Inline Script

Add an inline script to your `<head>` to prevent flash of incorrect theme:

```astro
---
// src/pages/index.astro
---

<html>
  <head>
    <script is:inline>
      const getTheme = () => {
        if (typeof localStorage !== "undefined" && localStorage.getItem("mode-watcher-mode")) {
          return localStorage.getItem("mode-watcher-mode");
        }
        if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
          return "dark";
        }
        return "light";
      };

      const theme = getTheme();

      if (theme === "light") {
        document.documentElement.classList.remove("dark");
      } else {
        document.documentElement.classList.add("dark");
      }

      window.localStorage.setItem("mode-watcher-mode", theme);
    </script>
  </head>
  <body>
    <!-- content -->
  </body>
</html>
```

### Install mode-watcher

```bash
pnpm i mode-watcher@0.5.1
```

```bash
npm i mode-watcher@0.5.1
```

```bash
bun install mode-watcher@0.5.1
```

### Add ModeWatcher

```astro
---
import { ModeWatcher } from "mode-watcher";
---

<ModeWatcher client:load />
```

## Theme Toggle

### Light Switch

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

### Add to Page

```astro
---
import ModeToggle from "@/components/mode-toggle.svelte";
---

<ModeToggle client:load />
```
