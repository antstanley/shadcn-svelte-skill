# Popover

Displays rich content in a portal, triggered by a button.

[Docs](https://bits-ui.com/docs/components/popover)

[API Reference](https://bits-ui.com/docs/components/popover#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<Popover.Root>
  <Popover.Trigger class={buttonVariants({ variant: "outline" })}
    >Open popover</Popover.Trigger
  >
  <Popover.Content class="w-80">
    <div class="grid gap-4">
      <div class="space-y-2">
        <h4 class="leading-none font-medium">Dimensions</h4>
        <p class="text-sm text-muted-foreground">
          Set the dimensions for the layer.
        </p>
      </div>
      <div class="grid gap-2">
        <div class="grid grid-cols-3 items-center gap-4">
          <Label for="width">Width</Label>
          <Input id="width" value="100%" class="col-span-2 h-8" />
        </div>
        <div class="grid grid-cols-3 items-center gap-4">
          <Label for="maxWidth">Max. width</Label>
          <Input id="maxWidth" value="300px" class="col-span-2 h-8" />
        </div>
        <div class="grid grid-cols-3 items-center gap-4">
          <Label for="height">Height</Label>
          <Input id="height" value="25px" class="col-span-2 h-8" />
        </div>
        <div class="grid grid-cols-3 items-center gap-4">
          <Label for="maxHeight">Max. height</Label>
          <Input id="maxHeight" value="none" class="col-span-2 h-8" />
        </div>
      </div>
    </div>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add popover
```

```bash
npx shadcn-svelte@latest add popover
```

```bash
bun x shadcn-svelte@latest add popover
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Popover from "$lib/components/ui/popover/index.js";
</script>
```

```svelte
<Popover.Root>
  <Popover.Trigger>Open</Popover.Trigger>
  <Popover.Content>Place content for the popover here.</Popover.Content>
</Popover.Root>
```

## [Basic](#basic)

A simple popover with a header, title, and description.

```svelte
<script lang="ts">
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Popover.Root>
  <Popover.Trigger
    class={buttonVariants({ variant: "outline", class: "w-fit" })}
    >Open Popover</Popover.Trigger
  >
  <Popover.Content align="start">
    <Popover.Header>
      <Popover.Title>Dimensions</Popover.Title>
      <Popover.Description
        >Set the dimensions for the layer.</Popover.Description
      >
    </Popover.Header>
  </Popover.Content>
</Popover.Root>
```

View Code

## [Align](#align)

Use the `align` prop on `Popover.Content` to control the horizontal alignment.

```svelte
<script lang="ts">
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  const alignments = ["start", "center", "end"] as const;
</script>
<div class="flex gap-6">
  {#each alignments as align (align)}
    <Popover.Root>
      <Popover.Trigger
        class={buttonVariants({
          variant: "outline",
          size: "sm",
          class: "capitalize"
        })}
      >
        {align}
      </Popover.Trigger>
      <Popover.Content {align} class="w-40">Aligned to {align}</Popover.Content>
    </Popover.Root>
  {/each}
</div>
```

View Code

## [With Form](#with-form)

A popover with form fields inside.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { buttonVariants } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Popover.Root>
  <Popover.Trigger class={buttonVariants({ variant: "outline" })}
    >Open Popover</Popover.Trigger
  >
  <Popover.Content class="w-64" align="start">
    <Popover.Header>
      <Popover.Title>Dimensions</Popover.Title>
      <Popover.Description
        >Set the dimensions for the layer.</Popover.Description
      >
    </Popover.Header>
    <Field.Group class="gap-4">
      <Field.Field orientation="horizontal">
        <Field.Label for="width" class="w-1/2">Width</Field.Label>
        <Input id="width" value="100%" />
      </Field.Field>
      <Field.Field orientation="horizontal">
        <Field.Label for="height" class="w-1/2">Height</Field.Label>
        <Input id="height" value="25px" />
      </Field.Field>
    </Field.Group>
  </Popover.Content>
</Popover.Root>
```

View Code