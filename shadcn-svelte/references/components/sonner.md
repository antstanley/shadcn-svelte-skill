# Sonner

An opinionated toast component for Svelte.

## About

The Sonner component is provided by [svelte-sonner](https://svelte-sonner.vercel.app/), which is a Svelte port of [Sonner](https://sonner.emilkowal.ski/), originally created by Emil Kowalski for React.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add sonner
```

```bash
npx shadcn-svelte@latest add sonner
```

```bash
bun x shadcn-svelte@latest add sonner
```

## Setup

Add the Toaster component to your root layout:

```svelte
<!-- +layout.svelte -->
<script lang="ts">
  import { Toaster } from "$lib/components/ui/sonner/index.js";
  let { children } = $props();
</script>

<Toaster />
{@render children?.()}
```

## Usage

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
  import { Button } from "$lib/components/ui/button/index.js";
</script>

<Button onclick={() => toast("Hello world")}>Show toast</Button>
```

## Examples

### Toast Types

```svelte
<script lang="ts">
  import { toast } from "svelte-sonner";
</script>

<!-- Default -->
<Button onclick={() => toast("Event has been created")}>Default</Button>

<!-- Success -->
<Button onclick={() => toast.success("Event has been created")}>Success</Button>

<!-- Info -->
<Button onclick={() => toast.info("Be at the area 10 minutes before")}>Info</Button>

<!-- Warning -->
<Button onclick={() => toast.warning("Event time cannot be earlier than 8am")}>Warning</Button>

<!-- Error -->
<Button onclick={() => toast.error("Event has not been created")}>Error</Button>
```

### With Description and Action

```svelte
toast("Event has been created", {
  description: "Sunday, December 03, 2023 at 9:00 AM",
  action: {
    label: "Undo",
    onClick: () => console.info("Undo")
  }
})
```

### Promise

```svelte
toast.promise(
  () => new Promise((resolve) => setTimeout(() => resolve({ name: "Event" }), 2000)),
  {
    loading: "Loading...",
    success: (data) => `${data.name} has been created`,
    error: "Error"
  }
)
```

## Theme Support

By default, Sonner uses system preferences for light/dark theme. You can use [mode-watcher](https://github.com/svecosystem/mode-watcher) for proper dark mode support.

See [Dark Mode documentation](/docs/dark-mode) for more details.
