# Sheet

Extends the Dialog component to display content that complements the main content of the screen.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add sheet
```

```bash
npx shadcn-svelte@latest add sheet
```

```bash
bun x shadcn-svelte@latest add sheet
```

## Usage

```svelte
<script lang="ts">
  import * as Sheet from "$lib/components/ui/sheet/index.js";
</script>

<Sheet.Root>
  <Sheet.Trigger>Open</Sheet.Trigger>
  <Sheet.Content>
    <Sheet.Header>
      <Sheet.Title>Edit profile</Sheet.Title>
      <Sheet.Description>
        Make changes to your profile here.
      </Sheet.Description>
    </Sheet.Header>
    <!-- Content here -->
    <Sheet.Footer>
      <Sheet.Close>Save changes</Sheet.Close>
    </Sheet.Footer>
  </Sheet.Content>
</Sheet.Root>
```

## Examples

### Side Positioning

Use the `side` property to position the sheet. Options: "top", "right", "bottom", "left":

```svelte
<Sheet.Content side="left">
  <!-- Content slides in from left -->
</Sheet.Content>

<Sheet.Content side="right">
  <!-- Content slides in from right (default) -->
</Sheet.Content>

<Sheet.Content side="top">
  <!-- Content slides in from top -->
</Sheet.Content>

<Sheet.Content side="bottom">
  <!-- Content slides in from bottom -->
</Sheet.Content>
```

### Custom Size

Adjust the sheet's dimensions with CSS classes:

```svelte
<Sheet.Content class="w-[400px] sm:w-[540px]">
  <!-- Custom width -->
</Sheet.Content>
```

### With Form

```svelte
<script lang="ts">
  import { Button, buttonVariants } from "$lib/components/ui/button/index.js";
  import * as Sheet from "$lib/components/ui/sheet/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<Sheet.Root>
  <Sheet.Trigger class={buttonVariants({ variant: "outline" })}>
    Edit Profile
  </Sheet.Trigger>
  <Sheet.Content>
    <Sheet.Header>
      <Sheet.Title>Edit profile</Sheet.Title>
      <Sheet.Description>
        Make changes to your profile here. Click save when you're done.
      </Sheet.Description>
    </Sheet.Header>
    <div class="grid gap-4 py-4">
      <div class="grid gap-2">
        <Label for="name">Name</Label>
        <Input id="name" value="Pedro Duarte" />
      </div>
      <div class="grid gap-2">
        <Label for="username">Username</Label>
        <Input id="username" value="@peduarte" />
      </div>
    </div>
    <Sheet.Footer>
      <Button type="submit">Save changes</Button>
    </Sheet.Footer>
  </Sheet.Content>
</Sheet.Root>
```

## Components

- **Sheet.Root** - Root container
- **Sheet.Trigger** - Button that opens the sheet
- **Sheet.Content** - Sheet content container
- **Sheet.Header** - Header section
- **Sheet.Title** - Sheet title
- **Sheet.Description** - Sheet description
- **Sheet.Footer** - Footer section
- **Sheet.Close** - Close button

## API

Built on [Bits UI Dialog](https://bits-ui.com/docs/components/dialog).
