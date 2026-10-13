# Spinner

An indicator that can be used to show a loading state.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Item from "$lib/components/ui/item/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex w-full max-w-xs flex-col gap-4 [--radius:1rem]">
  <Item.Root variant="muted">
    <Item.Media>
      <Spinner />
    </Item.Media>
    <Item.Content>
      <Item.Title class="line-clamp-1">Processing payment...</Item.Title>
    </Item.Content>
    <Item.Content class="flex-none justify-end">
      <span class="text-sm tabular-nums">$100.00</span>
    </Item.Content>
  </Item.Root>
</div>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add spinner
```

```bash
npx shadcn-svelte@latest add spinner
```

```bash
bun x shadcn-svelte@latest add spinner
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
```

```svelte
<Spinner />
```

## [Customization](#customization)

You can replace the default spinner icon with any other icon by editing the `Spinner` component.

```svelte
<script lang="ts">
  import LoaderIcon from "@lucide/svelte/icons/loader";
</script>
<div class="flex items-center gap-4">
  <LoaderIcon role="status" aria-label="Loading" class="size-4 animate-spin" />
</div>
```

View Code

components/ui/spinner/spinner.svelte

```svelte
<script lang="ts">
  import LoaderIcon from "@lucide/svelte/icons/loader";
  import { cn } from "$lib/utils.js";
  import type { SVGAttributes } from "svelte/elements";
  let { class: className, ...restProps }: SVGAttributes<SVGSVGElement> =
    $props();
</script>
<LoaderIcon
  role="status"
  aria-label="Loading"
  class={cn("size-4 animate-spin", className)}
  {...restProps}
/>
```

## [Size](#size)

Use the `size-*` utility class to change the size of the spinner.

```svelte
<script lang="ts">
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex items-center gap-6">
  <Spinner class="size-3" />
  <Spinner class="size-4" />
  <Spinner class="size-6" />
  <Spinner class="size-8" />
</div>
```

View Code

## [Button](#button)

Add a spinner to a button to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex flex-col items-center gap-4">
  <Button disabled size="sm">
    <Spinner data-icon="inline-start" />
    Loading...
  </Button>
  <Button variant="outline" disabled size="sm">
    <Spinner data-icon="inline-start" />
    Please wait
  </Button>
  <Button variant="secondary" disabled size="sm">
    <Spinner data-icon="inline-start" />
    Processing
  </Button>
</div>
```

View Code

## [Badge](#badge)

Add a spinner to a badge to indicate a loading state. Place the `<Spinner />` before the label with `data-icon="inline-start"` for a start position, or after the label with `data-icon="inline-end"` for an end position.

```svelte
<script lang="ts">
  import { Badge } from "$lib/components/ui/badge/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex items-center gap-4 [--radius:1.2rem]">
  <Badge>
    <Spinner data-icon="inline-start" />
    Syncing
  </Badge>
  <Badge variant="secondary">
    <Spinner data-icon="inline-start" />
    Updating
  </Badge>
  <Badge variant="outline">
    <Spinner data-icon="inline-start" />
    Processing
  </Badge>
</div>
```

View Code

## [Input Group](#input-group)

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex w-full max-w-md flex-col gap-4">
  <InputGroup.Root>
    <InputGroup.Input placeholder="Send a message..." disabled />
    <InputGroup.Addon align="inline-end">
      <Spinner />
    </InputGroup.Addon>
  </InputGroup.Root>
  <InputGroup.Root>
    <InputGroup.Textarea placeholder="Send a message..." disabled />
    <InputGroup.Addon align="block-end">
      <Spinner /> Validating...
      <InputGroup.Button class="ms-auto" variant="default">
        <ArrowUpIcon />
        <span class="sr-only">Send</span>
      </InputGroup.Button>
    </InputGroup.Addon>
  </InputGroup.Root>
</div>
```

View Code

## [Empty](#empty)

```svelte
<script lang="ts">
  import * as Empty from "$lib/components/ui/empty/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<Empty.Root class="w-full">
  <Empty.Header>
    <Empty.Media variant="icon">
      <Spinner />
    </Empty.Media>
    <Empty.Title>Processing your request</Empty.Title>
    <Empty.Description>
      Please wait while we process your request. Do not refresh the page.
    </Empty.Description>
  </Empty.Header>
  <Empty.Content>
    <Button variant="outline" size="sm">Cancel</Button>
  </Empty.Content>
</Empty.Root>
```

View Code