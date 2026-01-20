# Input OTP

Accessible one-time password component with copy paste functionality.

## About

Input OTP is built on top of Bits UI's [PinInput](https://bits-ui.com/docs/components/pin-input).

## Installation

```bash
pnpm dlx shadcn-svelte@latest add input-otp
```

```bash
npx shadcn-svelte@latest add input-otp
```

```bash
bun x shadcn-svelte@latest add input-otp
```

## Usage

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>

<InputOTP.Root maxlength={6}>
  {#snippet children({ cells })}
    <InputOTP.Group>
      {#each cells.slice(0, 3) as cell (cell)}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
    <InputOTP.Separator />
    <InputOTP.Group>
      {#each cells.slice(3, 6) as cell (cell)}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
  {/snippet}
</InputOTP.Root>
```

## Examples

### Pattern

Use the `pattern` prop to define a custom pattern for the OTP input:

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
  import { REGEXP_ONLY_DIGITS_AND_CHARS } from "bits-ui";
</script>

<InputOTP.Root maxlength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
  {#snippet children({ cells })}
    <InputOTP.Group>
      {#each cells as cell (cell)}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
  {/snippet}
</InputOTP.Root>
```

### Separator

Use `InputOTP.Separator` to add separators between groups:

```svelte
<InputOTP.Root maxlength={6}>
  {#snippet children({ cells })}
    <InputOTP.Group>
      {#each cells.slice(0, 2) as cell (cell)}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
    <InputOTP.Separator />
    <InputOTP.Group>
      {#each cells.slice(2, 4) as cell (cell)}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
    <InputOTP.Separator />
    <InputOTP.Group>
      {#each cells.slice(4, 6) as cell (cell)}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
  {/snippet}
</InputOTP.Root>
```

### Controlled

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
  let value = $state("");
</script>

<InputOTP.Root maxlength={6} bind:value>
  {#snippet children({ cells })}
    <InputOTP.Group>
      {#each cells as cell (cell)}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
  {/snippet}
</InputOTP.Root>

<div class="text-center text-sm">
  {value === "" ? "Enter your one-time password." : `You entered: ${value}`}
</div>
```

### With Form

Integrates with Formsnap and Superforms for validation:

```svelte
<script lang="ts">
  import { z } from "zod";
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
  import * as Form from "$lib/components/ui/form/index.js";

  const formSchema = z.object({
    pin: z.string().min(6, {
      message: "Your one-time password must be at least 6 characters."
    })
  });
</script>

<Form.Field {form} name="pin">
  <Form.Control>
    {#snippet children({ props })}
      <Form.Label>One-Time Password</Form.Label>
      <InputOTP.Root maxlength={6} {...props} bind:value={$formData.pin}>
        {#snippet children({ cells })}
          <InputOTP.Group>
            {#each cells as cell (cell)}
              <InputOTP.Slot {cell} />
            {/each}
          </InputOTP.Group>
        {/snippet}
      </InputOTP.Root>
    {/snippet}
  </Form.Control>
  <Form.Description>Please enter the one-time password sent to your phone.</Form.Description>
  <Form.FieldErrors />
</Form.Field>
```
