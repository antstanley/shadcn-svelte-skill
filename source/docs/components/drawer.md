# Drawer

A drawer component for Svelte.

[Docs](https://github.com/huntabyte/vaul-svelte)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { toast } from "svelte-sonner";
 import * as Drawer from "$lib/components/ui/drawer/index.js";
 import * as Field from "$lib/components/ui/field/index.js";
 import * as RadioGroup from "$lib/components/ui/radio-group/index.js";
 import { IsMobile } from "$lib/components/hooks/is-mobile.svelte.js";
 import { Badge } from "$lib/components/ui/badge/index.js";
 import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
 const deliveryTimes = [
  {
   value: "asap",
   id: "delivery-asap",
   label: "Standard delivery",
   description: "2535 min  Driver assigned now",
   badge: "Fastest",
  },
  {
   value: "5-00",
   id: "delivery-5-00",
   label: "5:00 PM  5:15 PM",
   description: "Prep starts at 4:45 PM",
  },
  {
   value: "5-30",
   id: "delivery-5-30",
   label: "5:30 PM  5:45 PM",
   description: "Good if you're heading home",
  },
  {
   value: "6-00",
   id: "delivery-6-00",
   label: "6:00 PM  6:15 PM",
   description: "Most popular  High demand",
  },
  {
   value: "6-30",
   id: "delivery-6-30",
   label: "6:30 PM  6:45 PM",
   description: "Last slot before kitchen closes",
  },
];
 let open = $state(false);
 let deliveryTime = $state("asap");
 const isMobile = new IsMobile();
 function handleConfirm() {
  const selected = deliveryTimes.find((time) => time.value === deliveryTime);
  if (!selected) {
   return;
  }
  open = false;
  toast("Delivery time confirmed", {
   description: selected.label,
  });
 }
</script>
<Drawer.Root bind:open direction={isMobile.current ? "bottom" : "right"}>
 <Drawer.Trigger class={buttonVariants({ variant: "secondary" })}>Open Drawer</Drawer.Trigger>
 <Drawer.Content>
  <Drawer.Header>
   <Drawer.Title>Pick a delivery time</Drawer.Title>
   <Drawer.Description>We&apos;ll prepare your order as soon as possible.</Drawer.Description>
  </Drawer.Header>
  <div class="flex-1 overflow-y-auto p-4">
   <RadioGroup.Root bind:value={deliveryTime} class="gap-2">
    {#each deliveryTimes as time (time.value)}
     <Field.Label for={time.id}>
      <Field.Field orientation="horizontal">
       <Field.Content>
        <Field.Title class="flex items-center gap-2">
         {time.label}
         {#if time.badge}
          <Badge variant="secondary">{time.badge}</Badge>
         {/if}
        </Field.Title>
        <Field.Description>{time.description}</Field.Description>
       </Field.Content>
       <RadioGroup.Item value={time.value} id={time.id} />
      </Field.Field>
     </Field.Label>
    {/each}
   </RadioGroup.Root>
  </div>
  <Drawer.Footer>
   <Button onclick={handleConfirm} class="h-[34px]">Confirm Delivery Time</Button>
   <Drawer.Close class={buttonVariants({ variant: "outline" })}>Cancel</Drawer.Close>
  </Drawer.Footer>
 </Drawer.Content>
</Drawer.Root>
```

View Code

## [About](#about)

Drawer is built on top of [Vaul Svelte](https://vaul-svelte.com), which is a Svelte port of [Vaul](https://vaul.emilkowal.ski) by [Emil Kowalski](https://twitter.com/emilkowalski_).

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add drawer
```

```bash
npx shadcn-svelte@latest add drawer
```

```bash
bun x shadcn-svelte@latest add drawer
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Drawer from "$lib/components/ui/drawer/index.js";
</script>
```

```svelte
<Drawer.Root>
  <Drawer.Trigger>Open</Drawer.Trigger>
  <Drawer.Content>
    <Drawer.Header>
      <Drawer.Title>Are you absolutely sure?</Drawer.Title>
      <Drawer.Description>This action cannot be undone.</Drawer.Description>
    </Drawer.Header>
    <Drawer.Footer>
      <Button>Submit</Button>
      <Drawer.Close>Cancel</Drawer.Close>
    </Drawer.Footer>
  </Drawer.Content>
</Drawer.Root>
```

## [Position](#position)

Use the `direction` prop to set the side of the drawer.

Available options are `top`, `right`, `bottom`, and `left`.

```svelte
<script lang="ts">
 import * as Drawer from "$lib/components/ui/drawer/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Drawer.Root direction="left">
 <Drawer.Trigger class={buttonVariants({ variant: "secondary" })}>Open Left Drawer</Drawer.Trigger>
 <Drawer.Content>
  <Drawer.Header>
   <Drawer.Title>Move Goal</Drawer.Title>
   <Drawer.Description>Set your daily activity goal.</Drawer.Description>
  </Drawer.Header>
  <div class="flex-1 p-4">
   <div class="size-full rounded-2xl bg-muted"></div>
  </div>
  <Drawer.Footer>
   <Drawer.Close class={buttonVariants()}>Close</Drawer.Close>
  </Drawer.Footer>
 </Drawer.Content>
</Drawer.Root>
```

View Code

## [Nested](#nested)

Open drawers from inside another drawer using `<Drawer.NestedRoot />`. Parent drawers stay mounted and stack behind the frontmost drawer.

```svelte
<script lang="ts">
 import * as Drawer from "$lib/components/ui/drawer/index.js";
 import { IsMobile } from "$lib/components/hooks/is-mobile.svelte.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
 const isMobile = new IsMobile();
 const direction = $derived(isMobile.current ? "bottom" : "right");
</script>
{#snippet placeholder()}
 <div class="flex-1 p-4">
  <div
   class="bg-muted group-data-[vaul-drawer-direction=bottom]/drawer-content:aspect-video group-data-[vaul-drawer-direction=bottom]/drawer-content:w-full group-data-[vaul-drawer-direction=right]/drawer-content:size-full"
  ></div>
 </div>
{/snippet}
<Drawer.Root {direction}>
 <Drawer.Trigger class={buttonVariants({ variant: "secondary" })}>Open Drawer</Drawer.Trigger>
 <Drawer.Content>
  <Drawer.Header>
   <Drawer.Title>Drawer</Drawer.Title>
   <Drawer.Description>Open another drawer from the same direction.</Drawer.Description>
  </Drawer.Header>
  {@render placeholder()}
  <Drawer.Footer>
   <Drawer.NestedRoot {direction}>
    <Drawer.Trigger class={buttonVariants({ variant: "outline" })}>
     Open Nested Drawer
    </Drawer.Trigger>
    <Drawer.Content>
     <Drawer.Header>
      <Drawer.Title>Nested Drawer</Drawer.Title>
      <Drawer.Description>
       The parent drawer stays mounted behind this one.
      </Drawer.Description>
     </Drawer.Header>
     {@render placeholder()}
     <Drawer.Footer>
      <Drawer.NestedRoot {direction}>
       <Drawer.Trigger class={buttonVariants({ variant: "outline" })}>
        Open Third Drawer
       </Drawer.Trigger>
       <Drawer.Content>
        <Drawer.Header>
         <Drawer.Title>Third Drawer</Drawer.Title>
         <Drawer.Description>Two drawers are stacked behind this one.</Drawer.Description>
        </Drawer.Header>
        {@render placeholder()}
        <Drawer.Footer>
         <Drawer.NestedRoot {direction}>
          <Drawer.Trigger class={buttonVariants({ variant: "outline" })}>
           Open Fourth Drawer
          </Drawer.Trigger>
          <Drawer.Content>
           <Drawer.Header>
            <Drawer.Title>Fourth Drawer</Drawer.Title>
            <Drawer.Description>
             This is the frontmost drawer in the stack.
            </Drawer.Description>
           </Drawer.Header>
           {@render placeholder()}
           <Drawer.Footer>
            <Drawer.Close class={buttonVariants({ variant: "outline" })}>
             Close
            </Drawer.Close>
           </Drawer.Footer>
          </Drawer.Content>
         </Drawer.NestedRoot>
         <Drawer.Close class={buttonVariants({ variant: "outline" })}>Close</Drawer.Close>
        </Drawer.Footer>
       </Drawer.Content>
      </Drawer.NestedRoot>
      <Drawer.Close class={buttonVariants({ variant: "outline" })}>Close</Drawer.Close>
     </Drawer.Footer>
    </Drawer.Content>
   </Drawer.NestedRoot>
   <Drawer.Close class={buttonVariants({ variant: "outline" })}>Close</Drawer.Close>
  </Drawer.Footer>
 </Drawer.Content>
</Drawer.Root>
```

View Code

## [Non Modal](#non-modal)

Set `modal={false}` to allow interaction with the rest of the page while the drawer is open. Clicking outside a non-modal drawer does not close it.

```svelte
<script lang="ts">
 import * as Drawer from "$lib/components/ui/drawer/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>
<Drawer.Root modal={false} direction="right">
 <Drawer.Trigger class={buttonVariants({ variant: "outline" })}>Non Modal</Drawer.Trigger>
 <Drawer.Content>
  <Drawer.Header>
   <Drawer.Title>Non Modal Drawer</Drawer.Title>
  </Drawer.Header>
  <div class="flex-1 p-4">
   <div class="size-full rounded-2xl bg-muted"></div>
  </div>
  <Drawer.Footer>
   <Drawer.Close class={buttonVariants()}>Close</Drawer.Close>
  </Drawer.Footer>
 </Drawer.Content>
</Drawer.Root>
```

View Code

## [Snap Points](#snap-points)

Use `snapPoints` to snap a drawer to preset heights. Numbers between `0` and `1` represent fractions of the viewport. String values support `px` units. Snap points apply to vertical drawers.

Track the active snap point with `bind:activeSnapPoint`.

```svelte
<script lang="ts">
 import * as Drawer from "$lib/components/ui/drawer/index.js";
 import { buttonVariants } from "$lib/components/ui/button/index.js";
 const SNAP_POINTS = ["496px", 1];
 let snapPoint = $state<string | number | null>(SNAP_POINTS[0]);
</script>
<Drawer.Root snapPoints={SNAP_POINTS} bind:activeSnapPoint={snapPoint}>
 <Drawer.Trigger class={buttonVariants({ variant: "outline" })}>Open Snap Drawer</Drawer.Trigger>
 <Drawer.Content class="h-full data-[vaul-drawer-direction=bottom]:max-h-[97%]">
  <Drawer.Header>
   <Drawer.Title>Snap points</Drawer.Title>
   <Drawer.Description>
    Drag the drawer to snap between a compact peek and a near full-height view.
   </Drawer.Description>
  </Drawer.Header>
  <div class="p-4">
   <div class="h-80 w-full rounded-2xl bg-muted"></div>
  </div>
  <Drawer.Footer>
   <Drawer.Close class={buttonVariants()}>Close</Drawer.Close>
  </Drawer.Footer>
 </Drawer.Content>
</Drawer.Root>
```

View Code

## [Responsive](#responsive)

You can combine the `Dialog` and `Drawer` components to create a responsive dialog. This renders a `Dialog` component on desktop and a `Drawer` on mobile.

```svelte
<script lang="ts">
 import { MediaQuery } from "svelte/reactivity";
 import * as Dialog from "$lib/components/ui/dialog/index.js";
 import * as Drawer from "$lib/components/ui/drawer/index.js";
 import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
 import { Input } from "$lib/components/ui/input/index.js";
 import { Label } from "$lib/components/ui/label/index.js";
 let open = $state(false);
 const isDesktop = new MediaQuery("(min-width: 768px)");
 const id = $props.id();
</script>
{#if isDesktop.current}
 <Dialog.Root bind:open>
  <Dialog.Trigger class={buttonVariants({ variant: "outline" })}>Edit Profile</Dialog.Trigger>
  <Dialog.Content class="sm:max-w-[425px]">
   <Dialog.Header>
    <Dialog.Title>Edit profile</Dialog.Title>
    <Dialog.Description>
     Make changes to your profile here. Click save when you're done.
    </Dialog.Description>
   </Dialog.Header>
   <form class="grid items-start gap-6">
    <div class="grid gap-3">
     <Label for="email-{id}">Email</Label>
     <Input type="email" id="email-{id}" value="shadcn@example.com" />
    </div>
    <div class="grid gap-3">
     <Label for="username-{id}">Username</Label>
     <Input id="username-{id}" value="@shadcn" />
    </div>
    <Button type="submit">Save changes</Button>
   </form>
  </Dialog.Content>
 </Dialog.Root>
{:else}
 <Drawer.Root bind:open>
  <Drawer.Trigger class={buttonVariants({ variant: "outline" })}>Edit Profile</Drawer.Trigger>
  <Drawer.Content>
   <Drawer.Header class="text-start">
    <Drawer.Title>Edit profile</Drawer.Title>
    <Drawer.Description>
     Make changes to your profile here. Click save when you're done.
    </Drawer.Description>
   </Drawer.Header>
   <form class="grid items-start gap-6 p-4">
    <div class="grid gap-3">
     <Label for="email-{id}">Email</Label>
     <Input type="email" id="email-{id}" value="shadcn@example.com" />
    </div>
    <div class="grid gap-3">
     <Label for="username-{id}">Username</Label>
     <Input id="username-{id}" value="@shadcn" />
    </div>
    <Button type="submit">Save changes</Button>
   </form>
  </Drawer.Content>
 </Drawer.Root>
{/if}
```

View Code