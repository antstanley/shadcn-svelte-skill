# Button Group

A container that groups related buttons together with consistent styling.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add button-group
```

```bash
npx shadcn-svelte@latest add button-group
```

```bash
bun x shadcn-svelte@latest add button-group
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as ButtonGroup from "$lib/components/ui/button-group/index.js";
</script>
```

```svelte
<ButtonGroup.Root>
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup.Root>
```

## [Accessibility](#accessibility)

- The `ButtonGroup` component has the `role` attribute set to `group` .
- Use `tabindex` to navigate between the buttons in the group.
- Use `aria-label` or `aria-labelledby` to label the button group.

```svelte
<ButtonGroup aria-label="Button group">
  <Button>Button 1</Button>
  <Button>Button 2</Button>
</ButtonGroup>
```

## [ButtonGroup vs ToggleGroup](#buttongroup-vs-togglegroup)

- Use the `ButtonGroup` component when you want to group buttons that perform an action.
- Use the `ToggleGroup` component when you want to group buttons that toggle a state.

## [Examples](#examples)

### [Orientation](#orientation)

Set the `orientation` prop to change the button group layout.

View Code

### [Size](#size)

Control the size of buttons using the `size` prop on individual buttons.

View Code

### [Nested](#nested)

Nest `ButtonGroup` components to create button groups with spacing.

View Code

### [Separator](#separator)

The `ButtonGroupSeparator` component visually divides buttons within a group.

Buttons with variant `outline` do not need a separator since they have a border. For other variants, a separator is recommended to improve the visual hierarchy.

View Code

### [Split](#split)

Create a split button group by adding two buttons separated by a `ButtonGroupSeparator`.

View Code

### [Input](#input)

Wrap an `Input` component with buttons.

View Code

### [Input Group](#input-group)

Wrap an `InputGroup` component to create complex input layouts.

View Code

### [Dropdown Menu](#dropdown-menu)

Create a split button group with a `DropdownMenu` component.

View Code

### [Select](#select)

Pair with a `Select` component.

View Code

### [Popover](#popover)

Use with a `Popover` component.

View Code