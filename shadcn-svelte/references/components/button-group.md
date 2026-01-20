# Button Group

A container that groups related buttons together with consistent styling.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add button-group
```

```bash
npx shadcn-svelte@latest add button-group
```

```bash
bun x shadcn-svelte@latest add button-group
```

## Usage

```svelte
<script lang="ts">
  import * as ButtonGroup from "$lib/components/ui/button-group/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>

<ButtonGroup.Root>
  <Button variant="outline">Left</Button>
  <Button variant="outline">Center</Button>
  <Button variant="outline">Right</Button>
</ButtonGroup.Root>
```

## Overview

Use the `ButtonGroup` component when you want to group buttons that perform an action. This is different from the `ToggleGroup` component, which is used to toggle between states.

The component outputs `role="group"` for accessibility purposes.

## Orientation

The `orientation` prop adjusts the button group layout between horizontal and vertical configurations:

```svelte
<ButtonGroup.Root orientation="vertical">
  <Button variant="outline">Top</Button>
  <Button variant="outline">Middle</Button>
  <Button variant="outline">Bottom</Button>
</ButtonGroup.Root>
```

## Sizes

Button sizing is controlled through individual button `size` properties:

```svelte
<ButtonGroup.Root>
  <Button size="sm" variant="outline">Small</Button>
  <Button size="sm" variant="outline">Buttons</Button>
</ButtonGroup.Root>
```

## Nested Groups

Nested button groups create spacing between related button clusters:

```svelte
<ButtonGroup.Root>
  <ButtonGroup.Root>
    <Button variant="outline">Group 1</Button>
    <Button variant="outline">Button</Button>
  </ButtonGroup.Root>
  <ButtonGroup.Root>
    <Button variant="outline">Group 2</Button>
    <Button variant="outline">Button</Button>
  </ButtonGroup.Root>
</ButtonGroup.Root>
```

## Separator

The `ButtonGroupSeparator` visually divides buttons, particularly useful for variants without borders:

```svelte
<ButtonGroup.Root>
  <Button variant="ghost">Option 1</Button>
  <ButtonGroup.Separator />
  <Button variant="ghost">Option 2</Button>
</ButtonGroup.Root>
```

## Split Button

Split button configurations combine standard buttons with dropdowns or popovers:

```svelte
<ButtonGroup.Root>
  <Button>Save</Button>
  <DropdownMenu.Root>
    <DropdownMenu.Trigger>
      <Button size="icon" variant="outline">
        <ChevronDownIcon />
      </Button>
    </DropdownMenu.Trigger>
    <DropdownMenu.Content>
      <!-- menu items -->
    </DropdownMenu.Content>
  </DropdownMenu.Root>
</ButtonGroup.Root>
```

## Accessibility

- Use `aria-label` or `aria-labelledby` attributes to label button groups
- Use `tabindex` for keyboard navigation between grouped buttons
