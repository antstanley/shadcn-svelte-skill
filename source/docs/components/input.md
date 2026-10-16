# Input

A text input component for forms and user data entry with built-in styling and accessibility features.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field>
  <Field.Label for="input-demo-api-key">API Key</Field.Label>
  <Input id="input-demo-api-key" type="password" placeholder="sk-..." />
  <Field.Description
    >Your API key is encrypted and stored securely.</Field.Description
  >
</Field.Field>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add input
```

```bash
npx shadcn-svelte@latest add input
```

```bash
bun x shadcn-svelte@latest add input
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
</script>
```

```svelte
<Input />
```

## [Basic](#basic)

```svelte
<script lang="ts">
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Input placeholder="Enter text" />
```

View Code

## [Field](#field)

Use `Field.Field`, `Field.Label`, and `Field.Description` to create an input with a label and description.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field>
  <Field.Label for="input-field-username">Username</Field.Label>
  <Input
    id="input-field-username"
    type="text"
    placeholder="Enter your username"
  />
  <Field.Description
    >Choose a unique username for your account.</Field.Description
  >
</Field.Field>
```

View Code

## [Field Group](#field-group)

Use `Field.Group` to show multiple `Field.Field` blocks and to build forms.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Group>
  <Field.Field>
    <Field.Label for="fieldgroup-name">Name</Field.Label>
    <Input id="fieldgroup-name" placeholder="Jordan Lee" />
  </Field.Field>
  <Field.Field>
    <Field.Label for="fieldgroup-email">Email</Field.Label>
    <Input id="fieldgroup-email" type="email" placeholder="name@example.com" />
    <Field.Description>We'll send updates to this address.</Field.Description>
  </Field.Field>
  <Field.Field orientation="horizontal">
    <Button type="reset" variant="outline">Reset</Button>
    <Button type="submit">Submit</Button>
  </Field.Field>
</Field.Group>
```

View Code

## [Disabled](#disabled)

Use the `disabled` prop to disable the input. To style the disabled state, add the `data-disabled` attribute to the `Field.Field` component.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field data-disabled>
  <Field.Label for="input-demo-disabled">Email</Field.Label>
  <Input id="input-demo-disabled" type="email" placeholder="Email" disabled />
  <Field.Description>This field is currently disabled.</Field.Description>
</Field.Field>
```

View Code

## [Invalid](#invalid)

Use the `aria-invalid` prop to mark the input as invalid. To style the invalid state, add the `data-invalid` attribute to the `Field.Field` component.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field data-invalid>
  <Field.Label for="input-invalid">Invalid Input</Field.Label>
  <Input id="input-invalid" placeholder="Error" aria-invalid />
  <Field.Description>This field contains validation errors.</Field.Description>
</Field.Field>
```

View Code

## [File](#file)

Use the `type="file"` prop to create a file input.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field>
  <Field.Label for="picture">Picture</Field.Label>
  <Input id="picture" type="file" />
  <Field.Description>Select a picture to upload.</Field.Description>
</Field.Field>
```

View Code

## [Inline](#inline)

Use `Field.Field` with `orientation="horizontal"` to create an inline input. Pair with `Button` to create a search input with a button.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field orientation="horizontal">
  <Input type="search" placeholder="Search..." />
  <Button>Search</Button>
</Field.Field>
```

View Code

## [Grid](#grid)

Use a grid layout to place multiple inputs side by side.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Group class="grid max-w-sm grid-cols-2">
  <Field.Field>
    <Field.Label for="first-name">First Name</Field.Label>
    <Input id="first-name" placeholder="Jordan" />
  </Field.Field>
  <Field.Field>
    <Field.Label for="last-name">Last Name</Field.Label>
    <Input id="last-name" placeholder="Lee" />
  </Field.Field>
</Field.Group>
```

View Code

## [Required](#required)

Use the `required` attribute to indicate required inputs.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field>
  <Field.Label for="input-required">
    Required Field <span class="text-destructive">*</span>
  </Field.Label>
  <Input id="input-required" placeholder="This field is required" required />
  <Field.Description>This field must be filled out.</Field.Description>
</Field.Field>
```

View Code

## [Badge](#badge)

Use `Badge` in the label to highlight a recommended field.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import { Badge } from "$lib/components/ui/badge/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field>
  <Field.Label for="input-badge">
    Webhook URL
    <Badge variant="secondary" class="ml-auto">Beta</Badge>
  </Field.Label>
  <Input
    id="input-badge"
    type="url"
    placeholder="https://api.example.com/webhook"
  />
</Field.Field>
```

View Code

## [Input Group](#input-group)

To add icons, text, or buttons inside an input, use the `InputGroup` component. See the [Input Group](https://shadcn-svelte.com/docs/components/input-group) component for more examples.

```svelte
<script lang="ts">
  import InfoIcon from "@lucide/svelte/icons/info";
  import * as Field from "$lib/components/ui/field/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>
<Field.Field>
  <Field.Label for="input-group-url">Website URL</Field.Label>
  <InputGroup.Root>
    <InputGroup.Input id="input-group-url" placeholder="example.com" />
    <InputGroup.Addon>
      <InputGroup.Text>https://</InputGroup.Text>
    </InputGroup.Addon>
    <InputGroup.Addon align="inline-end">
      <InfoIcon />
    </InputGroup.Addon>
  </InputGroup.Root>
</Field.Field>
```

View Code

## [Button Group](#button-group)

To add buttons to an input, use the `ButtonGroup` component. See the [Button Group](https://shadcn-svelte.com/docs/components/button-group) component for more examples.

```svelte
<script lang="ts">
  import * as ButtonGroup from "$lib/components/ui/button-group/index.js";
  import * as Field from "$lib/components/ui/field/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
</script>
<Field.Field>
  <Field.Label for="input-button-group">Search</Field.Label>
  <ButtonGroup.Root>
    <Input id="input-button-group" placeholder="Type to search..." />
    <Button variant="outline">Search</Button>
  </ButtonGroup.Root>
</Field.Field>
```

View Code

## [Form](#form)

A full form example with multiple inputs, a select, and a button.

```svelte
<script lang="ts">
  import * as Field from "$lib/components/ui/field/index.js";
  import * as Select from "$lib/components/ui/select/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  const countries = [
    { value: "us", label: "United States" },
    { value: "uk", label: "United Kingdom" },
    { value: "ca", label: "Canada" }
 ];
  let country = $state("us");
</script>
<form class="w-full max-w-sm">
  <Field.Group>
    <Field.Field>
      <Field.Label for="form-name">Name</Field.Label>
      <Input id="form-name" type="text" placeholder="Evil Rabbit" required />
    </Field.Field>
    <Field.Field>
      <Field.Label for="form-email">Email</Field.Label>
      <Input id="form-email" type="email" placeholder="john@example.com" />
      <Field.Description
        >We'll never share your email with anyone.</Field.Description
      >
    </Field.Field>
    <div class="grid grid-cols-2 gap-4">
      <Field.Field>
        <Field.Label for="form-phone">Phone</Field.Label>
        <Input id="form-phone" type="tel" placeholder="+1 (555) 123-4567" />
      </Field.Field>
      <Field.Field>
        <Field.Label for="form-country">Country</Field.Label>
        <Select.Root type="single" items={countries} bind:value={country}>
          <Select.Trigger id="form-country">
            <Select.Value />
          </Select.Trigger>
          <Select.Content>
            <Select.Group>
              {#each countries as item (item.value)}
                <Select.Item value={item.value} label={item.label}
                  >{item.label}</Select.Item
                >
              {/each}
            </Select.Group>
          </Select.Content>
        </Select.Root>
      </Field.Field>
    </div>
    <Field.Field>
      <Field.Label for="form-address">Address</Field.Label>
      <Input id="form-address" type="text" placeholder="123 Main St" />
    </Field.Field>
    <Field.Field orientation="horizontal">
      <Button type="button" variant="outline">Cancel</Button>
      <Button type="submit">Submit</Button>
    </Field.Field>
  </Field.Group>
</form>
```

View Code