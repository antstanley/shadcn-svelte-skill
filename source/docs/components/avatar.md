# Avatar

An image element with a fallback for representing the user.

[Docs](https://bits-ui.com/docs/components/avatar)

[API Reference](https://bits-ui.com/docs/components/avatar#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<div class="flex flex-row flex-wrap items-center gap-6 md:gap-12">
 <Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" class="grayscale" />
  <Avatar.Fallback>CN</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
  <Avatar.Fallback>ER</Avatar.Fallback>
  <Avatar.Badge class="bg-green-600 dark:bg-green-800" />
 </Avatar.Root>
 <Avatar.Group class="grayscale">
  <Avatar.Root>
   <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
   <Avatar.Fallback>CN</Avatar.Fallback>
  </Avatar.Root>
  <Avatar.Root>
   <Avatar.Image src="https://github.com/maxleiter.png" alt="@maxleiter" />
   <Avatar.Fallback>LR</Avatar.Fallback>
  </Avatar.Root>
  <Avatar.Root>
   <Avatar.Image src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
   <Avatar.Fallback>ER</Avatar.Fallback>
  </Avatar.Root>
  <Avatar.GroupCount>+3</Avatar.GroupCount>
 </Avatar.Group>
</div>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add avatar
```

```bash
npx shadcn-svelte@latest add avatar
```

```bash
bun x shadcn-svelte@latest add avatar
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
```

```svelte
<Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
</Avatar.Root>
```

## [Basic](#basic)

A basic avatar component with an image and a fallback.

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<Avatar.Root>
 <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" class="grayscale" />
 <Avatar.Fallback>CN</Avatar.Fallback>
</Avatar.Root>
```

View Code

## [Badge](#badge)

Use the `Avatar.Badge` component to add a badge to the avatar. The badge is positioned at the bottom right of the avatar.

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<Avatar.Root>
 <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
 <Avatar.Fallback>CN</Avatar.Fallback>
 <Avatar.Badge class="bg-green-600 dark:bg-green-800" />
</Avatar.Root>
```

View Code

Use the `class` prop to add custom styles to the badge such as custom colors, sizes, etc.

```svelte
<Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
  <Avatar.Badge class="bg-green-600 dark:bg-green-800" />
</Avatar.Root>
```

## [Badge with Icon](#badge-with-icon)

You can also use an icon inside `<Avatar.Badge>`.

```svelte
<script lang="ts">
 import PlusIcon from "@lucide/svelte/icons/plus";
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<Avatar.Root class="grayscale">
 <Avatar.Image src="https://github.com/pranathip.png" alt="@pranathip" />
 <Avatar.Fallback>PP</Avatar.Fallback>
 <Avatar.Badge>
  <PlusIcon />
 </Avatar.Badge>
</Avatar.Root>
```

View Code

## [Avatar Group](#avatar-group)

Use the `Avatar.Group` component to add a group of avatars.

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<Avatar.Group class="grayscale">
 <Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/maxleiter.png" alt="@maxleiter" />
  <Avatar.Fallback>LR</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
  <Avatar.Fallback>ER</Avatar.Fallback>
 </Avatar.Root>
</Avatar.Group>
```

View Code

## [Avatar Group Count](#avatar-group-count)

Use `<Avatar.GroupCount>` to add a count to the group.

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<Avatar.Group class="grayscale">
 <Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/maxleiter.png" alt="@maxleiter" />
  <Avatar.Fallback>LR</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
  <Avatar.Fallback>ER</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.GroupCount>+3</Avatar.GroupCount>
</Avatar.Group>
```

View Code

## [Avatar Group with Icon](#avatar-group-with-icon)

You can also use an icon inside `<Avatar.GroupCount>`.

```svelte
<script lang="ts">
 import PlusIcon from "@lucide/svelte/icons/plus";
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<Avatar.Group class="grayscale">
 <Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/maxleiter.png" alt="@maxleiter" />
  <Avatar.Fallback>LR</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
  <Avatar.Fallback>ER</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.GroupCount>
  <PlusIcon />
 </Avatar.GroupCount>
</Avatar.Group>
```

View Code

## [Sizes](#sizes)

Use the `size` prop to change the size of the avatar.

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>
<div class="flex flex-wrap items-center gap-2 grayscale">
 <Avatar.Root size="sm">
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
 </Avatar.Root>
 <Avatar.Root size="lg">
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
 </Avatar.Root>
</div>
```

View Code

## [Dropdown](#dropdown)

You can use the `Avatar` component as a trigger for a dropdown menu.

```svelte
<script lang="ts">
 import * as Avatar from "$lib/components/ui/avatar/index.js";
 import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
<DropdownMenu.Root>
 <DropdownMenu.Trigger>
  {#snippet child({ props })}
   <Button {...props} variant="ghost" size="icon" class="rounded-full">
    <Avatar.Root>
     <Avatar.Image src="https://github.com/shadcn.png" alt="shadcn" />
     <Avatar.Fallback>CN</Avatar.Fallback>
    </Avatar.Root>
   </Button>
  {/snippet}
 </DropdownMenu.Trigger>
 <DropdownMenu.Content class="w-32">
  <DropdownMenu.Group>
   <DropdownMenu.Item>Profile</DropdownMenu.Item>
   <DropdownMenu.Item>Billing</DropdownMenu.Item>
   <DropdownMenu.Item>Settings</DropdownMenu.Item>
  </DropdownMenu.Group>
  <DropdownMenu.Separator />
  <DropdownMenu.Group>
   <DropdownMenu.Item variant="destructive">Log out</DropdownMenu.Item>
  </DropdownMenu.Group>
 </DropdownMenu.Content>
</DropdownMenu.Root>
```

View Code