# Sheet

Extends the Dialog component to display content that complements the main content of the screen.

[Docs](https://bits-ui.com/docs/components/dialog)

[API Reference](https://bits-ui.com/docs/components/dialog#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as Sheet from "$lib/components/ui/sheet/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
</script>
<Sheet.Root>
 <Sheet.Trigger class={buttonVariants({ variant: "outline" })}>Open</Sheet.Trigger>
 <Sheet.Content side="right">
  <Sheet.Header>
   <Sheet.Title>Edit profile</Sheet.Title>
   <Sheet.Description>
    Make changes to your profile here. Click save when you're done.
   </Sheet.Description>
  </Sheet.Header>
  <div class="grid flex-1 auto-rows-min gap-6 px-4">
   <div class="grid gap-3">
    <Label for="sheet-demo-name">Name</Label>
    <Input id="sheet-demo-name" value="Pedro Duarte" />
   </div>
   <div class="grid gap-3">
    <Label for="sheet-demo-username">Username</Label>
    <Input id="sheet-demo-username" value="@peduarte" />
   </div>
  </div>
  <Sheet.Footer>
   <Button type="submit">Save changes</Button>
   <Sheet.Close class={buttonVariants({ variant: "outline" })}>Close</Sheet.Close>
  </Sheet.Footer>
 </Sheet.Content>
</Sheet.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add sheet
```

```bash
npx shadcn-svelte@latest add sheet
```

```bash
bun x shadcn-svelte@latest add sheet
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Sheet from "$lib/components/ui/sheet/index.js";
</script>
```

```svelte
<Sheet.Root>
  <Sheet.Trigger>Open</Sheet.Trigger>
  <Sheet.Content>
    <Sheet.Header>
      <Sheet.Title>Are you sure absolutely sure?</Sheet.Title>
      <Sheet.Description>
        This action cannot be undone. This will permanently delete your account
        and remove your data from our servers.
      </Sheet.Description>
    </Sheet.Header>
  </Sheet.Content>
</Sheet.Root>
```

## [Side](#side)

Use the `side` prop on `Sheet.Content` to set the edge of the screen where the sheet appears. Values are `top`, `right`, `bottom`, or `left`.

```svelte
<script lang="ts">
 import * as Sheet from "$lib/components/ui/sheet/index.js";
 import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
 const SHEET_SIDES = ["top", "right", "bottom", "left"] as const;
</script>
<div class="flex flex-wrap gap-2">
 {#each SHEET_SIDES as side (side)}
  <Sheet.Root>
   <Sheet.Trigger class={buttonVariants({ variant: "outline", class: "capitalize" })}>
    {side}
   </Sheet.Trigger>
   <Sheet.Content {side} class="data-[side=bottom]:max-h-[50vh] data-[side=top]:max-h-[50vh]">
    <Sheet.Header>
     <Sheet.Title>Edit profile</Sheet.Title>
     <Sheet.Description>
      Make changes to your profile here. Click save when you're done.
     </Sheet.Description>
    </Sheet.Header>
    <div class="no-scrollbar overflow-y-auto px-4">
     {#each { length: 10 } as _, index (index)}
      <p class="mb-2 leading-relaxed">
       Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor
       incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud
       exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure
       dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
       Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
       mollit anim id est laborum.
      </p>
     {/each}
    </div>
    <Sheet.Footer>
     <Button type="submit">Save changes</Button>
     <Sheet.Close class={buttonVariants({ variant: "outline" })}>Cancel</Sheet.Close>
    </Sheet.Footer>
   </Sheet.Content>
  </Sheet.Root>
 {/each}
</div>
```

View Code

## [No Close Button](#no-close-button)

Use `showCloseButton={false}` on `Sheet.Content` to hide the close button.

```svelte
<script lang="ts">
 import * as Sheet from "$lib/components/ui/sheet/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Sheet.Root>
 <Sheet.Trigger class={buttonVariants({ variant: "outline" })}>Open Sheet</Sheet.Trigger>
 <Sheet.Content showCloseButton={false}>
  <Sheet.Header>
   <Sheet.Title>No Close Button</Sheet.Title>
   <Sheet.Description>
    This sheet doesn't have a close button in the top-right corner. Click outside to close.
   </Sheet.Description>
  </Sheet.Header>
 </Sheet.Content>
</Sheet.Root>
```

View Code