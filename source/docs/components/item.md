# Item

A versatile component that you can use to display any content.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

The `Item` component is a straightforward flex container that can house nearly any type of content. Use it to display a title, description, and actions. Group it with the `ItemGroup` component to create a list of items.

You can pretty much achieve the same result with the `div` element and some classes, but **I've built this so many times** that I decided to create a component for it. Now I use it all the time.

View Code

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

## [Examples](#examples)

### [Variants](#variants)

View Code

### [Size](#size)

The `Item` component has different sizes for different use cases. For example, you can use the `sm` size for a compact item or the default size for a standard item.

View Code

### [Icon](#icon)

View Code

### [Avatar](#avatar)

View Code

### [Image](#image)

View Code

### [Group](#group)

View Code

### [Header](#header)

View Code

### [Link](#link)

To render an item as a link, use the the `child` snippet. The hover and focus states will be applied to the anchor element.

View Code

### [Dropdown](#dropdown)

View Code