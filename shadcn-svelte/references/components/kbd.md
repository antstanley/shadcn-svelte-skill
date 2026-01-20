# Kbd

Used to display textual user input from keyboard.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add kbd
```

```bash
npx shadcn-svelte@latest add kbd
```

```bash
bun x shadcn-svelte@latest add kbd
```

## Usage

```svelte
<script lang="ts">
  import * as Kbd from "$lib/components/ui/kbd/index.js";
</script>

<Kbd.Root>B</Kbd.Root>
```

## Examples

### Single Key

```svelte
<Kbd.Root>⌘</Kbd.Root>
<Kbd.Root>Ctrl</Kbd.Root>
<Kbd.Root>Esc</Kbd.Root>
```

### Key Group

```svelte
<Kbd.Group>
  <Kbd.Root>⌘</Kbd.Root>
  <Kbd.Root>⇧</Kbd.Root>
  <Kbd.Root>⌥</Kbd.Root>
  <Kbd.Root>⌃</Kbd.Root>
</Kbd.Group>
```

### With Plus Sign

```svelte
<Kbd.Group>
  <Kbd.Root>Ctrl</Kbd.Root>
  <span>+</span>
  <Kbd.Root>B</Kbd.Root>
</Kbd.Group>
```

### In Button

```svelte
<Button variant="outline" size="sm" class="pe-2">
  Accept <Kbd.Root>↵</Kbd.Root>
</Button>

<Button variant="outline" size="sm" class="pe-2">
  Cancel <Kbd.Root>Esc</Kbd.Root>
</Button>
```

### In Tooltip

```svelte
<Tooltip.Content>
  <div class="flex items-center gap-2">
    Save Changes <Kbd.Root>⌘S</Kbd.Root>
  </div>
</Tooltip.Content>
```

### In Input Group

```svelte
<InputGroup.Root>
  <InputGroup.Input placeholder="Search..." />
  <InputGroup.Addon>
    <SearchIcon />
  </InputGroup.Addon>
  <InputGroup.Addon align="inline-end">
    <Kbd.Root>⌘</Kbd.Root>
    <Kbd.Root>K</Kbd.Root>
  </InputGroup.Addon>
</InputGroup.Root>
```

### Inline Text

```svelte
<p class="text-muted-foreground text-sm">
  Use
  <Kbd.Group>
    <Kbd.Root>Ctrl + B</Kbd.Root>
    <Kbd.Root>Ctrl + K</Kbd.Root>
  </Kbd.Group>
  to open the command palette
</p>
```

## Components

- **Kbd.Root** - Individual key display
- **Kbd.Group** - Groups multiple keys together
