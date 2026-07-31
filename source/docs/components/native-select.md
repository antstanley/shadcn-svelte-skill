# Native Select

A styled native HTML select element with consistent design system integration.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

For a styled select component, see the [Select](https://shadcn-svelte.com/docs/components/select) component.

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add native-select
```

```bash
npx shadcn-svelte@latest add native-select
```

```bash
bun x shadcn-svelte@latest add native-select
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as NativeSelect from "$lib/components/ui/native-select/index.js";
</script>
```

```svelte
<NativeSelect.Root>
  <NativeSelect.Option value="">Select a fruit</NativeSelect.Option>
  <NativeSelect.Option value="apple">Apple</NativeSelect.Option>
  <NativeSelect.Option value="banana">Banana</NativeSelect.Option>
  <NativeSelect.Option value="blueberry">Blueberry</NativeSelect.Option>
  <NativeSelect.Option value="grapes" disabled>Grapes</NativeSelect.Option>
  <NativeSelect.Option value="pineapple">Pineapple</NativeSelect.Option>
</NativeSelect.Root>
```

## [Examples](#examples)

### [With Groups](#with-groups)

Organize options using `NativeSelect.OptGroup` for better categorization.

View Code

```svelte
<NativeSelect.Root>
  <NativeSelect.Option value="">Select a food</NativeSelect.Option>
  <NativeSelect.OptGroup label="Fruits">
    <NativeSelect.Option value="apple">Apple</NativeSelect.Option>
    <NativeSelect.Option value="banana">Banana</NativeSelect.Option>
    <NativeSelect.Option value="blueberry">Blueberry</NativeSelect.Option>
  </NativeSelect.OptGroup>
  <NativeSelect.OptGroup label="Vegetables">
    <NativeSelect.Option value="carrot">Carrot</NativeSelect.Option>
    <NativeSelect.Option value="broccoli">Broccoli</NativeSelect.Option>
    <NativeSelect.Option value="spinach">Spinach</NativeSelect.Option>
  </NativeSelect.OptGroup>
</NativeSelect.Root>
```

### [Disabled State](#disabled-state)

Disable individual options or the entire select component.

View Code

### [Invalid State](#invalid-state)

Show validation errors with the `aria-invalid` attribute and error styling.

View Code

```svelte
<NativeSelect.Root aria-invalid="true">
  <NativeSelect.Option value="">Select a country</NativeSelect.Option>
  <NativeSelect.Option value="us">United States</NativeSelect.Option>
  <NativeSelect.Option value="uk">United Kingdom</NativeSelect.Option>
  <NativeSelect.Option value="ca">Canada</NativeSelect.Option>
</NativeSelect.Root>
```

## [Native Select vs Select](#native-select-vs-select)

- Use `NativeSelect` when you need native browser behavior, better performance, or mobile-optimized dropdowns.
- Use `Select` when you need custom styling, animations, or complex interactions.

The `NativeSelect` component provides native HTML select functionality with consistent styling that matches your design system.

## [Accessibility](#accessibility)

- The component maintains all native HTML select accessibility features.  
- Screen readers can navigate through options using arrow keys.  
- The chevron icon is marked as `aria-hidden="true"` to avoid duplication.
- Use `aria-label` or `aria-labelledby` for additional context when needed.

```tsx
<NativeSelect.Root aria-label="Choose your preferred language">
  <NativeSelect.Option value="en">English</NativeSelect.Option>
  <NativeSelect.Option value="es">Spanish</NativeSelect.Option>
  <NativeSelect.Option value="fr">French</NativeSelect.Option>
</NativeSelect.Root>
```

## [API Reference](#api-reference)

### [NativeSelect.Root](#nativeselectroot)

The main select component that wraps the native HTML select element.

| Prop                   | Type            | Default  |
| ---------------------------------------------------- | --------------------------------------------- | ----------------------------------------------------- |
| `class` | `string` |  |

All other props are passed through to the underlying `<select>` element.

```svelte
<NativeSelect.Root>
  <NativeSelect.Option value="option1">Option 1</NativeSelect.Option>
  <NativeSelect.Option value="option2">Option 2</NativeSelect.Option>
</NativeSelect.Root>
```

### [NativeSelect.Option](#nativeselectoption)

Represents an individual option within the select.

| Prop                      | Type             | Default        |
| ------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------- |
| `value`    | `string`  |                       |
| `disabled` | `boolean` | `false` |
| `class`    | `string`  |        |

All other props are passed through to the underlying `<option>` element.

```svelte
<NativeSelect.Option value="apple">Apple</NativeSelect.Option>
<NativeSelect.Option value="banana" disabled>Banana</NativeSelect.Option>
```

### [NativeSelect.OptGroup](#nativeselectoptgroup)

Groups related options together for better organization.

| Prop                      | Type             | Default        |
| ------------------------------------------------------- | ---------------------------------------------- | ----------------------------------------------------------- |
| `label`    | `string`  |                       |
| `disabled` | `boolean` | `false` |
| `class`    | `string`  |        |

All other props are passed through to the underlying `<optgroup>` element.

```svelte
<NativeSelect.OptGroup label="Fruits">
  <NativeSelect.Option value="apple">Apple</NativeSelect.Option>
  <NativeSelect.Option value="banana">Banana</NativeSelect.Option>
</NativeSelect.OptGroup>
```