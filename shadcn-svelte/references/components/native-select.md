# Native Select

A styled native HTML select element with consistent design system integration.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add native-select
```

```bash
npx shadcn-svelte@latest add native-select
```

```bash
bun x shadcn-svelte@latest add native-select
```

## Usage

```svelte
<script lang="ts">
  import * as NativeSelect from "$lib/components/ui/native-select/index.js";
</script>

<NativeSelect.Root>
  <NativeSelect.Option value="apple">Apple</NativeSelect.Option>
  <NativeSelect.Option value="banana">Banana</NativeSelect.Option>
  <NativeSelect.Option value="orange">Orange</NativeSelect.Option>
</NativeSelect.Root>
```

## When to Use

Use `NativeSelect` when you need:
- Native browser behavior
- Better performance
- Mobile-optimized dropdowns

For custom styled dropdowns with search and filtering, use the [Select](/docs/components/select) component instead.

## Components

- **NativeSelect.Root** - Container wrapping the native select element
- **NativeSelect.Option** - Individual selectable option
- **NativeSelect.OptGroup** - Group container for organizing related options

## Examples

### Grouped Options

```svelte
<NativeSelect.Root>
  <NativeSelect.OptGroup label="Fruits">
    <NativeSelect.Option value="apple">Apple</NativeSelect.Option>
    <NativeSelect.Option value="banana">Banana</NativeSelect.Option>
  </NativeSelect.OptGroup>
  <NativeSelect.OptGroup label="Vegetables">
    <NativeSelect.Option value="carrot">Carrot</NativeSelect.Option>
    <NativeSelect.Option value="broccoli">Broccoli</NativeSelect.Option>
  </NativeSelect.OptGroup>
</NativeSelect.Root>
```

### Disabled States

```svelte
<!-- Disabled option -->
<NativeSelect.Option value="unavailable" disabled>Unavailable</NativeSelect.Option>

<!-- Disabled select -->
<NativeSelect.Root disabled>
  <NativeSelect.Option value="1">Option 1</NativeSelect.Option>
</NativeSelect.Root>
```

### Invalid State

```svelte
<NativeSelect.Root aria-invalid="true">
  <NativeSelect.Option value="">Select an option</NativeSelect.Option>
  <NativeSelect.Option value="valid">Valid option</NativeSelect.Option>
</NativeSelect.Root>
```

## Accessibility

- Preserves native HTML select accessibility features
- Screen readers can navigate options via arrow keys
- Chevron icons are marked `aria-hidden="true"` to prevent duplication
- Add `aria-label` or `aria-labelledby` for additional context when necessary

## API

All components accept a `class` prop for customization, with other properties passed through to underlying HTML elements (`<select>`, `<option>`, `<optgroup>`).
