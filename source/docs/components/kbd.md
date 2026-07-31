# Kbd

Used to display textual user input from keyboard.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add kbd
```

```bash
npx shadcn-svelte@latest add kbd
```

```bash
bun x shadcn-svelte@latest add kbd
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Kbd from "$lib/components/ui/kbd/index.js";
</script>
```

```svelte
<Kbd.Root>B</Kbd.Root>
```

## [Examples](#examples)

### [Group](#group)

Use the `Kbd.Group` component to group keyboard keys together.

View Code

### [Button](#button)

Use the `Kbd.Root` component inside a `Button` component to display a keyboard key inside a button.

View Code

### [Tooltip](#tooltip)

You can use the `Kbd.Root` component inside a `Tooltip` component to display a tooltip with a keyboard key.

View Code

### [Input Group](#input-group)

You can use the `Kbd.Root` component inside a `InputGroup.Addon` component to display a keyboard key inside an input group.

View Code