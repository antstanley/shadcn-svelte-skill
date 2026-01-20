# Avatar

An image element with a fallback for representing the user.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add avatar
```

```bash
npx shadcn-svelte@latest add avatar
```

```bash
bun x shadcn-svelte@latest add avatar
```

## Usage

```svelte
<script lang="ts">
  import * as Avatar from "$lib/components/ui/avatar/index.js";
</script>

<Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
</Avatar.Root>
```

## Examples

### Basic

```svelte
<Avatar.Root>
  <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
  <Avatar.Fallback>CN</Avatar.Fallback>
</Avatar.Root>
```

### Rounded Corners

```svelte
<Avatar.Root class="rounded-lg">
  <Avatar.Image src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
  <Avatar.Fallback>ER</Avatar.Fallback>
</Avatar.Root>
```

### Avatar Group

Stack avatars with overlapping effect:

```svelte
<div class="*:data-[slot=avatar]:ring-background flex -space-x-2 *:data-[slot=avatar]:ring-2">
  <Avatar.Root>
    <Avatar.Image src="https://github.com/shadcn.png" alt="@shadcn" />
    <Avatar.Fallback>CN</Avatar.Fallback>
  </Avatar.Root>
  <Avatar.Root>
    <Avatar.Image src="https://github.com/leerob.png" alt="@leerob" />
    <Avatar.Fallback>LR</Avatar.Fallback>
  </Avatar.Root>
  <Avatar.Root>
    <Avatar.Image src="https://github.com/evilrabbit.png" alt="@evilrabbit" />
    <Avatar.Fallback>ER</Avatar.Fallback>
  </Avatar.Root>
</div>
```

## Components

- **Avatar.Root** - Container element
- **Avatar.Image** - The avatar image
- **Avatar.Fallback** - Fallback when image fails to load

## API

Built on [Bits UI Avatar](https://bits-ui.com/docs/components/avatar).
