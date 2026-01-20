# Spinner

An indicator that can be used to show a loading state.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add spinner
```

```bash
npx shadcn-svelte@latest add spinner
```

```bash
bun x shadcn-svelte@latest add spinner
```

## Usage

```svelte
<script lang="ts">
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>

<Spinner />
```

## Examples

### Size

Use the `size-*` utility class to change the size:

```svelte
<Spinner class="size-3" />
<Spinner class="size-4" />
<Spinner class="size-6" />
<Spinner class="size-8" />
```

### Color

Use the `text-*` utility class to change the color:

```svelte
<Spinner class="size-6 text-red-500" />
<Spinner class="size-6 text-green-500" />
<Spinner class="size-6 text-blue-500" />
<Spinner class="size-6 text-yellow-500" />
```

### In Button

```svelte
<Button disabled size="sm">
  <Spinner />
  Loading...
</Button>

<Button variant="outline" disabled size="sm">
  <Spinner />
  Please wait
</Button>
```

### In Badge

```svelte
<Badge>
  <Spinner />
  Syncing
</Badge>

<Badge variant="secondary">
  <Spinner />
  Updating
</Badge>
```

### In Input Group

```svelte
<InputGroup.Root>
  <InputGroup.Input placeholder="Send a message..." disabled />
  <InputGroup.Addon align="inline-end">
    <Spinner />
  </InputGroup.Addon>
</InputGroup.Root>
```

### In Empty State

```svelte
<Empty.Root>
  <Empty.Header>
    <Empty.Media variant="icon">
      <Spinner />
    </Empty.Media>
    <Empty.Title>Processing your request</Empty.Title>
    <Empty.Description>
      Please wait while we process your request.
    </Empty.Description>
  </Empty.Header>
</Empty.Root>
```

## Customization

You can replace the default spinner icon by editing the Spinner component:

```svelte
<script lang="ts">
  import { cn } from "$lib/utils.js";
  import LoaderIcon from "@lucide/svelte/icons/loader";
  import type { ComponentProps } from "svelte";

  type Props = ComponentProps<typeof LoaderIcon>;
  let { class: className, ...restProps }: Props = $props();
</script>

<LoaderIcon
  role="status"
  aria-label="Loading"
  class={cn("size-4 animate-spin", className)}
  {...restProps}
/>
```
