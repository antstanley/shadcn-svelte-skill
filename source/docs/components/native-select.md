# Native Select

A styled native HTML select element with consistent design system integration.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

For a styled select component, see the [Select](https://shadcn-svelte.com/docs/components/select) component.

View Code

```svelte
<script lang="ts">
  import * as NativeSelect from "$lib/components/ui/native-select/index.js";
</script>
<NativeSelect.Root>
  <NativeSelect.Option value="">Select status</NativeSelect.Option>
  <NativeSelect.Option value="todo">Todo</NativeSelect.Option>
  <NativeSelect.Option value="in-progress">In Progress</NativeSelect.Option>
  <NativeSelect.Option value="done">Done</NativeSelect.Option>
  <NativeSelect.Option value="cancelled">Cancelled</NativeSelect.Option>
</NativeSelect.Root>
```

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

## [Groups](#groups)

Use `NativeSelect.OptGroup` to organize options into categories.

```svelte
<script lang="ts">
  import * as NativeSelect from "$lib/components/ui/native-select/index.js";
</script>
<NativeSelect.Root>
  <NativeSelect.Option value="">Select department</NativeSelect.Option>
  <NativeSelect.OptGroup label="Engineering">
    <NativeSelect.Option value="frontend">Frontend</NativeSelect.Option>
    <NativeSelect.Option value="backend">Backend</NativeSelect.Option>
    <NativeSelect.Option value="devops">DevOps</NativeSelect.Option>
  </NativeSelect.OptGroup>
  <NativeSelect.OptGroup label="Sales">
    <NativeSelect.Option value="sales-rep">Sales Rep</NativeSelect.Option>
    <NativeSelect.Option value="account-manager"
      >Account Manager</NativeSelect.Option
    >
    <NativeSelect.Option value="sales-director"
      >Sales Director</NativeSelect.Option
    >
  </NativeSelect.OptGroup>
  <NativeSelect.OptGroup label="Operations">
    <NativeSelect.Option value="support">Customer Support</NativeSelect.Option>
    <NativeSelect.Option value="product-manager"
      >Product Manager</NativeSelect.Option
    >
    <NativeSelect.Option value="ops-manager"
      >Operations Manager</NativeSelect.Option
    >
  </NativeSelect.OptGroup>
</NativeSelect.Root>
```

View Code

## [Disabled](#disabled)

Add the `disabled` prop to the `NativeSelect.Root` component to disable the select.

```svelte
<script lang="ts">
  import * as NativeSelect from "$lib/components/ui/native-select/index.js";
</script>
<NativeSelect.Root disabled>
  <NativeSelect.Option value="">Disabled</NativeSelect.Option>
  <NativeSelect.Option value="apple">Apple</NativeSelect.Option>
  <NativeSelect.Option value="banana">Banana</NativeSelect.Option>
  <NativeSelect.Option value="blueberry">Blueberry</NativeSelect.Option>
</NativeSelect.Root>
```

View Code

## [Invalid](#invalid)

Use `aria-invalid` to show validation errors and the `data-invalid` attribute to the `Field.Field` component for styling.

```svelte
<script lang="ts">
  import * as NativeSelect from "$lib/components/ui/native-select/index.js";
</script>
<NativeSelect.Root aria-invalid="true">
  <NativeSelect.Option value="">Error state</NativeSelect.Option>
  <NativeSelect.Option value="apple">Apple</NativeSelect.Option>
  <NativeSelect.Option value="banana">Banana</NativeSelect.Option>
  <NativeSelect.Option value="blueberry">Blueberry</NativeSelect.Option>
</NativeSelect.Root>
```

View Code

## [Native Select vs Select](#native-select-vs-select)

- Use `NativeSelect` for native browser behavior, better performance, or mobile-optimized dropdowns.
- Use `Select` for custom styling, animations, or complex interactions.

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