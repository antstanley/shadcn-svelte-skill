# Item

A versatile component that you can use to display any content.

The `Item` component is a straightforward flex container that can house nearly any type of content. Use it to display a title, description, and actions. Group it with the `ItemGroup` component to create a list of items.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add item
```

```bash
npx shadcn-svelte@latest add item
```

```bash
bun x shadcn-svelte@latest add item
```

## Usage

```svelte
<script lang="ts">
  import * as Item from "$lib/components/ui/item/index.js";
</script>

<Item.Root>
  <Item.Header>Item Header</Item.Header>
  <Item.Media />
  <Item.Content>
    <Item.Title>Item</Item.Title>
    <Item.Description>Item description</Item.Description>
  </Item.Content>
  <Item.Actions />
  <Item.Footer>Item Footer</Item.Footer>
</Item.Root>
```

## Components

- **Item.Root** - Main container
- **Item.Header** - Header section (above content)
- **Item.Media** - Icon, avatar, or image
- **Item.Content** - Main content area
- **Item.Title** - Title text
- **Item.Description** - Description text
- **Item.Actions** - Action buttons
- **Item.Footer** - Footer section (below content)
- **Item.Group** - Groups multiple items
- **Item.Separator** - Divider between items

## Variants

```svelte
<Item.Root>Default</Item.Root>
<Item.Root variant="outline">Outlined with borders</Item.Root>
<Item.Root variant="muted">Subdued background</Item.Root>
```

## Sizes

```svelte
<Item.Root>Default size</Item.Root>
<Item.Root size="sm">Compact size</Item.Root>
```

## Examples

### With Icon

```svelte
<Item.Root variant="outline">
  <Item.Media variant="icon">
    <ShieldAlertIcon />
  </Item.Media>
  <Item.Content>
    <Item.Title>Security Alert</Item.Title>
    <Item.Description>New login detected</Item.Description>
  </Item.Content>
  <Item.Actions>
    <Button size="sm" variant="outline">Review</Button>
  </Item.Actions>
</Item.Root>
```

### With Avatar

```svelte
<Item.Root variant="outline">
  <Item.Media>
    <Avatar.Root>
      <Avatar.Image src="..." />
      <Avatar.Fallback>JD</Avatar.Fallback>
    </Avatar.Root>
  </Item.Media>
  <Item.Content>
    <Item.Title>John Doe</Item.Title>
    <Item.Description>john@example.com</Item.Description>
  </Item.Content>
</Item.Root>
```

### As Link

```svelte
<Item.Root>
  {#snippet child({ props })}
    <a href="/docs" {...props}>
      <Item.Content>
        <Item.Title>Visit documentation</Item.Title>
      </Item.Content>
      <Item.Actions>
        <ChevronRightIcon />
      </Item.Actions>
    </a>
  {/snippet}
</Item.Root>
```

### Item Group

```svelte
<Item.Group>
  {#each items as item, index}
    <Item.Root>
      <Item.Content>
        <Item.Title>{item.title}</Item.Title>
      </Item.Content>
    </Item.Root>
    {#if index !== items.length - 1}
      <Item.Separator />
    {/if}
  {/each}
</Item.Group>
```

## Item vs Field

Use **Field** for form inputs (checkbox, input, radio, select).
Use **Item** for display content (titles, descriptions, actions).
