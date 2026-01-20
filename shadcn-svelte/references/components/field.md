# Field

Combine labels, controls, and help text to compose accessible form fields and grouped inputs.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add field
```

```bash
npx shadcn-svelte@latest add field
```

```bash
bun x shadcn-svelte@latest add field
```

## Usage

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>

<Field.Field>
  <Field.Label>Email</Field.Label>
  <Field.Content>
    <Input type="email" placeholder="you@example.com" />
  </Field.Content>
  <Field.Description>We'll never share your email.</Field.Description>
</Field.Field>
```

## Core Structure

The Field component family consists of:

- `Field.Field` - The wrapper component
- `Field.Content` - Contains the form control
- `Field.Label` - The label for the field
- `Field.Description` - Helper text below the field
- `Field.Error` - Error message display

## Grouping & Organization

Wrap related fields with `Field.Group`, and use `Field.Set` with `Field.Legend` for semantic grouping:

```svelte
<Field.Group>
  <Field.Set>
    <Field.Legend>Personal Information</Field.Legend>
    <Field.Field>
      <Field.Label>First Name</Field.Label>
      <Field.Content>
        <Input />
      </Field.Content>
    </Field.Field>
    <Field.Field>
      <Field.Label>Last Name</Field.Label>
      <Field.Content>
        <Input />
      </Field.Content>
    </Field.Field>
  </Field.Set>
</Field.Group>
```

## Orientation

Fields support three layout modes:

### Vertical (Default)

```svelte
<Field.Field>
  <Field.Label>Name</Field.Label>
  <Field.Content>
    <Input />
  </Field.Content>
</Field.Field>
```

### Horizontal

```svelte
<Field.Field orientation="horizontal">
  <Field.Label>Name</Field.Label>
  <Field.Content>
    <Input />
  </Field.Content>
</Field.Field>
```

### Responsive

Automatically adjusts based on container width:

```svelte
<Field.Field orientation="responsive">
  <Field.Label>Name</Field.Label>
  <Field.Content>
    <Input />
  </Field.Content>
</Field.Field>
```

## Validation States

Mark fields as invalid using `data-invalid`:

```svelte
<Field.Field data-invalid>
  <Field.Label>Email</Field.Label>
  <Field.Content>
    <Input aria-invalid="true" />
  </Field.Content>
  <Field.Error>Please enter a valid email address.</Field.Error>
</Field.Field>
```

## Accessibility

- Field outputs `role="group"` so nested controls inherit labeling
- Labels are automatically associated with inputs via `for` attribute
- Error messages are linked via `aria-describedby`
- Description text provides additional context for screen readers

## Examples

The Field component works with:

- Inputs and Textareas
- Selects (native and custom)
- Sliders
- Checkboxes
- Radio buttons
- Switches
- Choice cards
