# Collapsible

An interactive component which expands/collapses a panel.

[Docs](https://bits-ui.com/docs/components/collapsible)

[API Reference](https://bits-ui.com/docs/components/collapsible#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import ChevronsUpDownIcon from "@lucide/svelte/icons/chevrons-up-down";
 import * as Collapsible from "$lib/components/ui/collapsible/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 let isOpen = $state(false);
</script>
<Collapsible.Root bind:open={isOpen} class="flex w-[350px] flex-col gap-2">
 <div class="flex items-center justify-between gap-4 px-4">
  <h4 class="text-sm font-semibold">Order #4189</h4>
  <Collapsible.Trigger>
   {#snippet child({ props })}
    <Button {...props} variant="ghost" size="icon" class="size-8">
     <ChevronsUpDownIcon />
     <span class="sr-only">Toggle details</span>
    </Button>
   {/snippet}
  </Collapsible.Trigger>
 </div>
 <div class="flex items-center justify-between rounded-md border px-4 py-2 text-sm">
  <span class="text-muted-foreground">Status</span>
  <span class="font-medium">Shipped</span>
 </div>
 <Collapsible.Content class="flex flex-col gap-2">
  <div class="rounded-md border px-4 py-2 text-sm">
   <p class="font-medium">Shipping address</p>
   <p class="text-muted-foreground">100 Market St, San Francisco</p>
  </div>
  <div class="rounded-md border px-4 py-2 text-sm">
   <p class="font-medium">Items</p>
   <p class="text-muted-foreground">2x Studio Headphones</p>
  </div>
 </Collapsible.Content>
</Collapsible.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add collapsible
```

```bash
npx shadcn-svelte@latest add collapsible
```

```bash
bun x shadcn-svelte@latest add collapsible
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible/index.js";
</script>
```

```svelte
<Collapsible.Root>
  <Collapsible.Trigger>Can I use this in my project?</Collapsible.Trigger>
  <Collapsible.Content>
    Yes. Free to use for personal and commercial projects. No attribution
    required.
  </Collapsible.Content>
</Collapsible.Root>
```

## [Controlled State](#controlled-state)

Use `bind:open` to control the state.

```svelte
<script lang="ts">
  import * as Collapsible from "$lib/components/ui/collapsible/index.js";
  let open = $state(false);
</script>
<Collapsible.Root bind:open>
  <Collapsible.Trigger>Toggle</Collapsible.Trigger>
  <Collapsible.Content>Content</Collapsible.Content>
</Collapsible.Root>
```

## [Basic](#basic)

```svelte
<script lang="ts">
 import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Collapsible from "$lib/components/ui/collapsible/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
<Card.Root class="mx-auto w-full max-w-sm">
 <Card.Content>
  <Collapsible.Root class="rounded-md data-[state=open]:bg-muted">
   <Collapsible.Trigger>
    {#snippet child({ props })}
     <Button {...props} variant="ghost" class="group w-full">
      Product details
      <ChevronDownIcon class="ml-auto group-data-[state=open]:rotate-180" />
     </Button>
    {/snippet}
   </Collapsible.Trigger>
   <Collapsible.Content class="flex flex-col items-start gap-2 p-2.5 pt-0 text-sm">
    <div>This panel can be expanded or collapsed to reveal additional content.</div>
    <Button size="xs">Learn More</Button>
   </Collapsible.Content>
  </Collapsible.Root>
 </Card.Content>
</Card.Root>
```

View Code

## [Settings Panel](#settings-panel)

Use a trigger button to reveal additional settings.

```svelte
<script lang="ts">
 import MaximizeIcon from "@lucide/svelte/icons/maximize";
 import MinimizeIcon from "@lucide/svelte/icons/minimize";
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Collapsible from "$lib/components/ui/collapsible/index.js";
 import * as Field from "$lib/components/ui/field/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 let isOpen = $state(false);
</script>
<Card.Root class="mx-auto w-full max-w-xs" size="sm">
 <Card.Header>
  <Card.Title>Radius</Card.Title>
  <Card.Description>Set the corner radius of the element.</Card.Description>
 </Card.Header>
 <Card.Content>
  <Collapsible.Root bind:open={isOpen} class="flex items-start gap-2">
   <Field.Group class="grid w-full grid-cols-2 gap-2">
    <Field.Field>
     <Field.Label for="radius-top-left" class="sr-only">Radius Top Left</Field.Label>
     <Input id="radius-top-left" placeholder="0" value={0} />
    </Field.Field>
    <Field.Field>
     <Field.Label for="radius-top-right" class="sr-only">Radius Top Right</Field.Label>
     <Input id="radius-top-right" placeholder="0" value={0} />
    </Field.Field>
    <Collapsible.Content class="col-span-full grid grid-cols-subgrid gap-2">
     <Field.Field>
      <Field.Label for="radius-bottom-left" class="sr-only">Radius Bottom Left</Field.Label>
      <Input id="radius-bottom-left" placeholder="0" value={0} />
     </Field.Field>
     <Field.Field>
      <Field.Label for="radius-bottom-right" class="sr-only">Radius Bottom Right</Field.Label>
      <Input id="radius-bottom-right" placeholder="0" value={0} />
     </Field.Field>
    </Collapsible.Content>
   </Field.Group>
   <Collapsible.Trigger>
    {#snippet child({ props })}
     <Button {...props} variant="outline" size="icon">
      {#if isOpen}
       <MinimizeIcon />
      {:else}
       <MaximizeIcon />
      {/if}
     </Button>
    {/snippet}
   </Collapsible.Trigger>
  </Collapsible.Root>
 </Card.Content>
</Card.Root>
```

View Code

## [File Tree](#file-tree)

Use nested collapsibles to build a file tree.

```svelte
<script lang="ts">
 import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
 import FileIcon from "@lucide/svelte/icons/file";
 import FolderIcon from "@lucide/svelte/icons/folder";
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Collapsible from "$lib/components/ui/collapsible/index.js";
 import * as Tabs from "$lib/components/ui/tabs/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 type FileTreeItem = { name: string } | { name: string; items: FileTreeItem[] };
 const fileTree: FileTreeItem[] = [
  {
   name: "components",
   items: [
    {
     name: "ui",
     items: [
      { name: "button.svelte" },
      { name: "card.svelte" },
      { name: "dialog.svelte" },
      { name: "input.svelte" },
      { name: "select.svelte" },
      { name: "table.svelte" },
    ],
    },
    { name: "login-form.svelte" },
    { name: "register-form.svelte" },
   ],
  },
  {
   name: "lib",
   items: [{ name: "utils.ts" }, { name: "cn.ts" }, { name: "api.ts" }],
  },
  {
   name: "hooks",
   items: [
    { name: "use-media-query.svelte.ts" },
    { name: "use-debounce.svelte.ts" },
    { name: "use-local-storage.svelte.ts" },
  ],
  },
  {
   name: "types",
   items: [{ name: "index.d.ts" }, { name: "api.d.ts" }],
  },
  {
   name: "public",
   items: [{ name: "favicon.ico" }, { name: "logo.svg" }, { name: "images" }],
  },
  { name: "app.html" },
  { name: "+layout.svelte" },
  { name: "app.css" },
  { name: "package.json" },
  { name: "tsconfig.json" },
  { name: "README.md" },
  { name: ".gitignore" },
 ];
</script>
{#snippet treeItem(fileItem: FileTreeItem)}
 {#if "items" in fileItem}
  <Collapsible.Root>
   <Collapsible.Trigger>
    {#snippet child({ props })}
     <Button
      {...props}
      variant="ghost"
      size="sm"
      class="group w-full justify-start transition-none hover:bg-accent hover:text-accent-foreground"
     >
      <ChevronRightIcon class="transition-transform group-data-[state=open]:rotate-90" />
      <FolderIcon />
      {fileItem.name}
     </Button>
    {/snippet}
   </Collapsible.Trigger>
   <Collapsible.Content class="mt-1 ml-5 style-lyra:ml-4">
    <div class="flex flex-col gap-1">
     {#each fileItem.items as child (child.name)}
      {@render treeItem(child)}
     {/each}
    </div>
   </Collapsible.Content>
  </Collapsible.Root>
 {:else}
  <Button variant="link" size="sm" class="w-full justify-start gap-2 text-foreground">
   <FileIcon />
   <span>{fileItem.name}</span>
  </Button>
 {/if}
{/snippet}
<Card.Root class="mx-auto w-full max-w-[16rem] gap-2" size="sm">
 <Card.Header>
  <Tabs.Root value="explorer">
   <Tabs.List class="w-full">
    <Tabs.Trigger value="explorer">Explorer</Tabs.Trigger>
    <Tabs.Trigger value="settings">Outline</Tabs.Trigger>
   </Tabs.List>
  </Tabs.Root>
 </Card.Header>
 <Card.Content>
  <div class="flex flex-col gap-1">
   {#each fileTree as item (item.name)}
    {@render treeItem(item)}
   {/each}
  </div>
 </Card.Content>
</Card.Root>
```

View Code