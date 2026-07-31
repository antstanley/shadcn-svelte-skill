# Spinner

An indicator that can be used to show a loading state.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add spinner
```

```bash
npx shadcn-svelte@latest add spinner
```

```bash
bun x shadcn-svelte@latest add spinner
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
```

```svelte
<Spinner />
```

## [Customization](#customization)

You can replace the default spinner icon with any other icon by editing the `Spinner` component.

View Code

## [Examples](#examples)

### [Size](#size)

Use the `size-*` utility class to change the size of the spinner.

View Code

### [Color](#color)

Use the `text-*` utility class to change the color of the spinner.

View Code

### [Button](#button)

Add a spinner to a button to indicate a loading state. The `<Button />` will handle the spacing between the spinner and the text.

View Code

### [Badge](#badge)

You can also use a spinner inside a badge.

View Code

### [Input Group](#input-group)

Input Group can have spinners inside `<InputGroup.Addon>`.

View Code

### [Empty](#empty)

View Code

### [Item](#item)

Use the spinner inside `<Item.Media>` to indicate a loading state.

View Code