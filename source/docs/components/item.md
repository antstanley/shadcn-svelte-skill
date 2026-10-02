# Item

A versatile component for displaying content with media, title, description, and actions.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import BadgeCheckIcon from "@lucide/svelte/icons/badge-check";
  import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
  import * as Item from "$lib/components/ui/item/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex w-full max-w-md flex-col gap-6">
  <Item.Root variant="outline">
    <Item.Content>
      <Item.Title>Basic Item</Item.Title>
      <Item.Description
        >A simple item with title and description.</Item.Description
      >
    </Item.Content>
    <Item.Actions>
      <Button variant="outline" size="sm">Action</Button>
    </Item.Actions>
  </Item.Root>
  <Item.Root variant="outline" size="sm">
    {#snippet child({ props })}
      <a href="##" {...props}>
        <Item.Media>
          <BadgeCheckIcon class="size-5" />
        </Item.Media>
        <Item.Content>
          <Item.Title>Your profile has been verified.</Item.Title>
        </Item.Content>
        <Item.Actions>
          <ChevronRightIcon class="size-4" />
        </Item.Actions>
      </a>
    {/snippet}
  </Item.Root>
</div>
```

View Code

The `Item` component is a straightforward flex container that can house nearly any type of content. Use it to display a title, description, and actions. Group it with the `Item.Group` component to create a list of items.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add item
```

```bash
npx shadcn-svelte@latest add item
```

```bash
bun x shadcn-svelte@latest add item
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Item from "$lib/components/ui/item/index.js";
</script>
```

```svelte
<Item.Root>
  <Item.Header>Item Header</Item.Header>
  <Item.Media />
  <Item.Content>
    <Item.Title>Item</Item.Title>
    <Item.Description>Item</Item.Description>
  </Item.Content>
  <Item.Actions />
  <Item.Footer>Item Footer</Item.Footer>
</Item.Root>
```

## [Item vs Field](#item-vs-field)

Use Field if you need to display a form input such as a checkbox, input, radio, or select.

If you only need to display content such as a title, description, and actions, use `Item`.

## [Variant](#variant)

Use the `variant` prop to change the visual style of the item.

```svelte
<script lang="ts">
  import InboxIcon from "@lucide/svelte/icons/inbox";
  import * as Item from "$lib/components/ui/item/index.js";
</script>
<div class="flex w-full max-w-md flex-col gap-6">
  <Item.Root>
    <Item.Media variant="icon">
      <InboxIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Default Variant</Item.Title>
      <Item.Description>Transparent background with no border.</Item.Description
      >
    </Item.Content>
  </Item.Root>
  <Item.Root variant="outline">
    <Item.Media variant="icon">
      <InboxIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Outline Variant</Item.Title>
      <Item.Description>Outlined style with a visible border.</Item.Description>
    </Item.Content>
  </Item.Root>
  <Item.Root variant="muted">
    <Item.Media variant="icon">
      <InboxIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Muted Variant</Item.Title>
      <Item.Description
        >Muted background for secondary content.</Item.Description
      >
    </Item.Content>
  </Item.Root>
</div>
```

View Code

## [Size](#size)

Use the `size` prop to change the size of the item. Available sizes are `default`, `sm`, and `xs`.

```svelte
<script lang="ts">
  import InboxIcon from "@lucide/svelte/icons/inbox";
  import * as Item from "$lib/components/ui/item/index.js";
</script>
<div class="flex w-full max-w-md flex-col gap-6">
  <Item.Root variant="outline">
    <Item.Media variant="icon">
      <InboxIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Default Size</Item.Title>
      <Item.Description>The standard size for most use cases.</Item.Description>
    </Item.Content>
  </Item.Root>
  <Item.Root variant="outline" size="sm">
    <Item.Media variant="icon">
      <InboxIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Small Size</Item.Title>
      <Item.Description>A compact size for dense layouts.</Item.Description>
    </Item.Content>
  </Item.Root>
  <Item.Root variant="outline" size="xs">
    <Item.Media variant="icon">
      <InboxIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Extra Small Size</Item.Title>
      <Item.Description>The most compact size available.</Item.Description>
    </Item.Content>
  </Item.Root>
</div>
```

View Code

## [Icon](#icon)

Use `Item.Media` with `variant="icon"` to display an icon.

```svelte
<script lang="ts">
  import ShieldAlertIcon from "@lucide/svelte/icons/shield-alert";
  import * as Item from "$lib/components/ui/item/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex w-full max-w-lg flex-col gap-6">
  <Item.Root variant="outline">
    <Item.Media variant="icon">
      <ShieldAlertIcon />
    </Item.Media>
    <Item.Content>
      <Item.Title>Security Alert</Item.Title>
      <Item.Description
        >New login detected from unknown device.</Item.Description
      >
    </Item.Content>
    <Item.Actions>
      <Button size="sm" variant="outline">Review</Button>
    </Item.Actions>
  </Item.Root>
</div>
```

View Code

## [Avatar](#avatar)

You can use `Item.Media` with `variant="avatar"` to display an avatar.

```svelte
<script lang="ts">
  import Plus from "@lucide/svelte/icons/plus";
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Item from "$lib/components/ui/item/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex w-full max-w-lg flex-col gap-6">
  <Item.Root variant="outline">
    <Item.Media>
      <Avatar.Root class="size-10">
        <Avatar.Image src="https://github.com/evilrabbit.png" />
        <Avatar.Fallback>ER</Avatar.Fallback>
      </Avatar.Root>
    </Item.Media>
    <Item.Content>
      <Item.Title>Evil Rabbit</Item.Title>
      <Item.Description>Last seen 5 months ago</Item.Description>
    </Item.Content>
    <Item.Actions>
      <Button
        size="icon-sm"
        variant="outline"
        class="rounded-full"
        aria-label="Invite"
      >
        <Plus />
      </Button>
    </Item.Actions>
  </Item.Root>
  <Item.Root variant="outline">
    <Item.Media>
      <div
        class="flex -space-x-2 *:data-[slot=avatar]:ring-2 *:data-[slot=avatar]:ring-background *:data-[slot=avatar]:grayscale"
      >
        <Avatar.Root class="hidden sm:flex">
          <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
          <Avatar.Fallback>CN</Avatar.Fallback>
        </Avatar.Root>
        <Avatar.Root class="hidden sm:flex">
          <Avatar.Image
            src="https://github.com/maxleiter.png"
            alt="@maxleiter"
          />
          <Avatar.Fallback>LR</Avatar.Fallback>
        </Avatar.Root>
        <Avatar.Root>
          <Avatar.Image
            src="https://github.com/evilrabbit.png"
            alt="@evilrabbit"
          />
          <Avatar.Fallback>ER</Avatar.Fallback>
        </Avatar.Root>
      </div>
    </Item.Media>
    <Item.Content>
      <Item.Title>No Team Members</Item.Title>
      <Item.Description
        >Invite your team to collaborate on this project.</Item.Description
      >
    </Item.Content>
    <Item.Actions>
      <Button size="sm" variant="outline">Invite</Button>
    </Item.Actions>
  </Item.Root>
</div>
```

View Code

## [Image](#image)

Use `Item.Media` with `variant="image"` to display an image.

```svelte
<script lang="ts">
  import * as Item from "$lib/components/ui/item/index.js";
  const music = [
    {
      title: "Midnight City Lights",
      artist: "Neon Dreams",
      album: "Electric Nights",
      duration: "3:45"
    },
    {
      title: "Coffee Shop Conversations",
      artist: "The Morning Brew",
      album: "Urban Stories",
      duration: "4:05"
    },
    {
      title: "Digital Rain",
      artist: "Cyber Symphony",
      album: "Binary Beats",
      duration: "3:30"
    }
 ];
</script>
<div class="flex w-full max-w-md flex-col gap-6">
  <Item.Group class="gap-4">
    {#each music as song (song.title)}
      <Item.Root variant="outline" role="listitem">
        {#snippet child({ props })}
          <a href="##" {...props}>
            <Item.Media variant="image">
              <img
                src={`https://avatar.vercel.sh/${song.title}`}
                alt={song.title}
                width={32}
                height={32}
                class="object-cover grayscale"
              />
            </Item.Media>
            <Item.Content>
              <Item.Title class="line-clamp-1">
                {song.title} -
                <span class="text-muted-foreground">{song.album}</span>
              </Item.Title>
              <Item.Description>{song.artist}</Item.Description>
            </Item.Content>
            <Item.Content class="flex-none text-center">
              <Item.Description>{song.duration}</Item.Description>
            </Item.Content>
          </a>
        {/snippet}
      </Item.Root>
    {/each}
  </Item.Group>
</div>
```

View Code

## [Group](#group)

Use `Item.Group` to group related items together.

```svelte
<script lang="ts">
  import Plus from "@lucide/svelte/icons/plus";
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as Item from "$lib/components/ui/item/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const people = [
    {
      username: "shadcn",
      avatar: "https://github.com/shadcn.png",
      email: "shadcn@vercel.com"
    },
    {
      username: "maxleiter",
      avatar: "https://github.com/maxleiter.png",
      email: "maxleiter@vercel.com"
    },
    {
      username: "evilrabbit",
      avatar: "https://github.com/evilrabbit.png",
      email: "evilrabbit@vercel.com"
    }
 ];
</script>
<Item.Group class="max-w-sm">
  {#each people as person (person.username)}
    <Item.Root variant="outline">
      <Item.Media>
        <Avatar.Root>
          <Avatar.Image src={person.avatar} class="grayscale" />
          <Avatar.Fallback>{person.username.charAt(0)}</Avatar.Fallback>
        </Avatar.Root>
      </Item.Media>
      <Item.Content class="gap-1">
        <Item.Title>{person.username}</Item.Title>
        <Item.Description>{person.email}</Item.Description>
      </Item.Content>
      <Item.Actions>
        <Button variant="ghost" size="icon" class="rounded-full">
          <Plus />
        </Button>
      </Item.Actions>
    </Item.Root>
  {/each}
</Item.Group>
```

View Code

## [Header](#header)

Use `Item.Header` to add a header above the item content.

```svelte
<script lang="ts">
  import * as Item from "$lib/components/ui/item/index.js";
  const models = [
    {
      name: "v0-1.5-sm",
      description: "Everyday tasks and UI generation.",
      image:
        "https://images.unsplash.com/photo-1650804068570-7fb2e3dbf888?q=80&w=640&auto=format&fit=crop",
      credit: "Valeria Reverdo on Unsplash"
    },
    {
      name: "v0-1.5-lg",
      description: "Advanced thinking or reasoning.",
      image:
        "https://images.unsplash.com/photo-1610280777472-54133d004c8c?q=80&w=640&auto=format&fit=crop",
      credit: "Michael Oeser on Unsplash"
    },
    {
      name: "v0-2.0-mini",
      description: "Open Source model for everyone.",
      image:
        "https://images.unsplash.com/photo-1602146057681-08560aee8cde?q=80&w=640&auto=format&fit=crop",
      credit: "Cherry Laithang on Unsplash"
    }
 ];
</script>
<div class="flex w-full max-w-xl flex-col gap-6">
  <Item.Group class="grid grid-cols-3 gap-4">
    {#each models as model (model.name)}
      <Item.Root variant="outline">
        <Item.Header>
          <img
            src={model.image}
            alt={model.name}
            width={128}
            height={128}
            class="aspect-square w-full rounded-sm object-cover"
          />
        </Item.Header>
        <Item.Content>
          <Item.Title>{model.name}</Item.Title>
          <Item.Description>{model.description}</Item.Description>
        </Item.Content>
      </Item.Root>
    {/each}
  </Item.Group>
</div>
```

View Code

## [Link](#link)

Use the `child` snippet to render the item as a link. The hover and focus states will be applied to the anchor element.

```svelte
<script lang="ts">
  import ChevronRightIcon from "@lucide/svelte/icons/chevron-right";
  import ExternalLinkIcon from "@lucide/svelte/icons/external-link";
  import * as Item from "$lib/components/ui/item/index.js";
</script>
<div class="flex w-full max-w-md flex-col gap-4">
  <Item.Root>
    {#snippet child({ props })}
      <a href="##" {...props}>
        <Item.Content>
          <Item.Title>Visit our documentation</Item.Title>
          <Item.Description
            >Learn how to get started with our components.</Item.Description
          >
        </Item.Content>
        <Item.Actions>
          <ChevronRightIcon class="size-4" />
        </Item.Actions>
      </a>
    {/snippet}
  </Item.Root>
  <Item.Root variant="outline">
    {#snippet child({ props })}
      <a href="##" target="_blank" rel="noopener noreferrer" {...props}>
        <Item.Content>
          <Item.Title>External resource</Item.Title>
          <Item.Description
            >Opens in a new tab with security attributes.</Item.Description
          >
        </Item.Content>
        <Item.Actions>
          <ExternalLinkIcon class="size-4" />
        </Item.Actions>
      </a>
    {/snippet}
  </Item.Root>
</div>
```

View Code

```svelte
<Item.Root>
  {#snippet child({ props })}
    <a href="/dashboard" {...props}>
      <Item.Media variant="icon">
        <HomeIcon />
      </Item.Media>
      <Item.Content>
        <Item.Title>Dashboard</Item.Title>
        <Item.Description
          >Overview of your account and activity.</Item.Description
        >
      </Item.Content>
    </a>
  {/snippet}
</Item.Root>
```

## [Dropdown](#dropdown)

```svelte
<script lang="ts">
  import ChevronDown from "@lucide/svelte/icons/chevron-down";
  import * as Avatar from "$lib/components/ui/avatar/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import * as Item from "$lib/components/ui/item/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  const people = [
    {
      username: "shadcn",
      avatar: "https://github.com/shadcn.png",
      email: "shadcn@vercel.com"
    },
    {
      username: "maxleiter",
      avatar: "https://github.com/maxleiter.png",
      email: "maxleiter@vercel.com"
    },
    {
      username: "evilrabbit",
      avatar: "https://github.com/evilrabbit.png",
      email: "evilrabbit@vercel.com"
    }
 ];
</script>
<DropdownMenu.Root>
  <DropdownMenu.Trigger>
    {#snippet child({ props })}
      <Button {...props} variant="outline">
        Select <ChevronDown />
      </Button>
    {/snippet}
  </DropdownMenu.Trigger>
  <DropdownMenu.Content class="w-auto" align="end">
    <DropdownMenu.Group>
      {#each people as person (person.username)}
        <DropdownMenu.Item>
          <Item.Root size="xs" class="w-full p-2">
            <Item.Media>
              <Avatar.Root class="size-[--spacing(6.5)]">
                <Avatar.Image src={person.avatar} class="grayscale" />
                <Avatar.Fallback>{person.username.charAt(0)}</Avatar.Fallback>
              </Avatar.Root>
            </Item.Media>
            <Item.Content class="gap-0">
              <Item.Title>{person.username}</Item.Title>
              <Item.Description class="leading-none"
                >{person.email}</Item.Description
              >
            </Item.Content>
          </Item.Root>
        </DropdownMenu.Item>
      {/each}
    </DropdownMenu.Group>
  </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code