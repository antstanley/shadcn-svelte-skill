# Formsnap

Building forms with Formsnap, Superforms, & Zod.

> **Note:** Formsnap is no longer actively maintained. The team recommends using the `<Field />` component as the preferred alternative going forward.

## Overview

The Form components wrap Formsnap and Sveltekit-Superforms to deliver:

- Semantic HTML structure with proper accessibility support
- Composable field components for scoped form state management
- Validation integration using Zod and other Superforms-supported libraries
- ARIA attribute automation based on field states
- Component compatibility with Select, RadioGroup, Checkbox, Switch, and other UI elements

## Installation

```bash
pnpm dlx shadcn-svelte@latest add form
```

```bash
npx shadcn-svelte@latest add form
```

```bash
bun x shadcn-svelte@latest add form
```

## Core Architecture

Forms follow a consistent structure:

```
Form.Field → Form.Control → Form.Label
          → Form.Description
          → Form.FieldErrors
```

## Implementation Steps

### 1. Define Schema

Create a schema file using Zod:

```ts
// src/lib/schema.ts
import { z } from "zod";

export const formSchema = z.object({
  email: z.string().email("Invalid email address"),
  password: z.string().min(8, "Password must be at least 8 characters")
});

export type FormSchema = typeof formSchema;
```

### 2. Configure Server Load

```ts
// src/routes/+page.server.ts
import { superValidate } from "sveltekit-superforms";
import { zod } from "sveltekit-superforms/adapters";
import { formSchema } from "$lib/schema";

export const load = async () => {
  return {
    form: await superValidate(zod(formSchema))
  };
};
```

### 3. Build Form Component

```svelte
<script lang="ts">
  import * as Form from "$lib/components/ui/form/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { superForm } from "sveltekit-superforms";
  import { zodClient } from "sveltekit-superforms/adapters";
  import { formSchema } from "$lib/schema";

  let { data } = $props();

  const form = superForm(data.form, {
    validators: zodClient(formSchema)
  });

  const { form: formData, enhance } = form;
</script>

<form method="POST" use:enhance>
  <Form.Field {form} name="email">
    <Form.Control>
      {#snippet children({ props })}
        <Form.Label>Email</Form.Label>
        <Input {...props} bind:value={$formData.email} />
      {/snippet}
    </Form.Control>
    <Form.Description>Your email address.</Form.Description>
    <Form.FieldErrors />
  </Form.Field>

  <button type="submit">Submit</button>
</form>
```

### 4. Create Server Action

```ts
// src/routes/+page.server.ts
import { fail } from "@sveltejs/kit";
import { superValidate } from "sveltekit-superforms";
import { zod } from "sveltekit-superforms/adapters";
import { formSchema } from "$lib/schema";

export const actions = {
  default: async ({ request }) => {
    const form = await superValidate(request, zod(formSchema));

    if (!form.valid) {
      return fail(400, { form });
    }

    // Process the form data
    return { form };
  }
};
```

## Migration Path

For new projects, consider using the newer `<Field />` component which provides modern form handling patterns with ongoing support.
