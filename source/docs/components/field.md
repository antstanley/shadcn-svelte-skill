# Field

Combine labels, controls, and help text to compose accessible form fields and grouped inputs.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add field
```

```bash
npx shadcn-svelte@latest add field
```

```bash
bun x shadcn-svelte@latest add field
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
</script>
```

```svelte
<Field.Set>
  <Field.Legend>Profile</Field.Legend>
  <Field.Description>This appears on invoices and emails.</Field.Description>
  <Field.Group>
    <Field.Field>
      <Field.Label for="name">Full name</Field.Label>
      <Input id="name" autocomplete="off" placeholder="Evil Rabbit" />
      <Field.Description
        >This appears on invoices and emails.</Field.Description
      >
    </Field.Field>
    <Field.Field>
      <Field.Label for="username">Username</Field.Label>
      <Input id="username" autocomplete="off" aria-invalid />
      <Field.Error>Choose another username.</Field.Error>
    </Field.Field>
    <Field.Field orientation="horizontal">
      <Switch id="newsletter" />
      <Field.Label for="newsletter">Subscribe to the newsletter</Field.Label>
    </Field.Field>
  </Field.Group>
</Field.Set>
```

## [Anatomy](#anatomy)

The `Field` family is designed for composing accessible forms. A typical field is structured as follows:

```svelte
<Field.Field>
  <Field.Label for="input-id">Label</Field.Label>
  <Field.Description>Optional helper text.</Field.Description>
  <Field.Error>Validation message.</Field.Error>
</Field.Field>
```

- `Field.Field` is the core wrapper for a single field.
- `Field.Content` is a flex column that groups label and description. Not required if you have no description.
- Wrap related fields with `Field.Group` , and use `Field.Set` with `Field.Legend` for semantic grouping.

## [Examples](#examples)

### [Input](#input)

View Code

### [Textarea](#textarea)

View Code

### [Select](#select)

View Code

### [Slider](#slider)

View Code

### [Fieldset](#fieldset)

View Code

### [Checkbox](#checkbox)

View Code

### [Radio](#radio)

View Code

### [Switch](#switch)

View Code

### [Choice Card](#choice-card)

Wrap `Field` components inside `FieldLabel` to create selectable field groups. This works with `RadioItem`, `Checkbox` and `Switch` components.

View Code

### [Field Group](#field-group)

Stack `Field` components with `Field.Group`. Add `Field.Separator` to divide them.

View Code

### [Responsive Layout](#responsive-layout)

- **Vertical fields:** Default orientation stacks label, control, and helper textideal for mobile-first layouts.
- **Horizontal fields:** Set `orientation="horizontal"` on `Field` to align the label and control side-by-side. Pair with `Field.Content` to keep descriptions aligned.
- **Responsive fields:** Set `orientation="responsive"` for automatic column layouts inside container-aware parents. Apply `@container/field-group` classes on `Field.Group` to switch orientations at specific breakpoints.

View Code

## [Validation and Errors](#validation-and-errors)

- Add `data-invalid` to `Field` to switch the entire block into an error state.
- Add `aria-invalid` on the input itself for assistive technologies.
- Render `FieldError` immediately after the control or inside `FieldContent` to keep error messages aligned with the field. Copy

```svelte
<Field.Field data-invalid>
  <Field.Label for="email">Email</Field.Label>
  <Input id="email" type="email" aria-invalid />
  <Field.Error>Enter a valid email address.</Field.Error>
</Field.Field>
```

## [Accessibility](#accessibility)

- `Field.Set` and `Field.Legend` keep related controls grouped for keyboard and assistive tech users.
- `Field` outputs `role="group"` so nested controls inherit labeling from `Field.Label` and `Field.Legend` when combined.
- Apply `Field.Separator` sparingly to ensure screen readers encounter clear section boundaries.