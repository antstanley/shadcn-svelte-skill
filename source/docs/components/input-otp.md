# Input OTP

Accessible one-time password component with copy-paste functionality.

[Docs](https://bits-ui.com/docs/components/pin-input)

[API Reference](https://bits-ui.com/docs/components/pin-input#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
 let value = $state("123456");
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
```

View Code

## [About](#about)

Input OTP is built on top of Bits UI's [PinInput](https://bits-ui.com/docs/components/pin-input) which is inspired by [@guilherme\_rodz](https://twitter.com/guilherme_rodz)'s Input OTP component.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add input-otp
```

```bash
npx shadcn-svelte@latest add input-otp
```

```bash
bun x shadcn-svelte@latest add input-otp
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
```

```svelte
<InputOTP.Root maxlength={6}>
  {#snippet children({ cells })}
    <InputOTP.Group>
      {#each cells.slice(0, 3) as cell}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
    <InputOTP.Separator />
    <InputOTP.Group>
      {#each cells.slice(3, 6) as cell}
        <InputOTP.Slot {cell} />
      {/each}
    </InputOTP.Group>
  {/snippet}
</InputOTP.Root>
```

## [Pattern](#pattern)

Use the `pattern` prop to define a custom pattern for the OTP input.

```svelte
<script lang="ts">
  import * as InputOTP from "$lib/components/ui/input-otp/index.js";
  import { REGEXP_ONLY_DIGITS_AND_CHARS } from "bits-ui";
</script>
<InputOTP.Root maxlength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
</InputOTP.Root>
```

```svelte
<script lang="ts">
 import { REGEXP_ONLY_DIGITS } from "bits-ui";
 import * as Field from "$lib/components/ui/field/index.js";
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
<Field.Field class="w-fit">
 <Field.Label for="digits-only">Digits Only</Field.Label>
 <InputOTP.Root id="digits-only" maxlength={6} pattern={REGEXP_ONLY_DIGITS}>
  {#snippet children({ cells })}
   <InputOTP.Group>
    {#each cells as cell (cell)}
     <InputOTP.Slot {cell} />
    {/each}
   </InputOTP.Group>
  {/snippet}
 </InputOTP.Root>
</Field.Field>
```

View Code

## [Separator](#separator)

Use the `<InputOTP.Separator />` component to add a separator between input groups.

```svelte
<script lang="ts">
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
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

View Code

## [Disabled](#disabled)

Use the `disabled` prop to disable the input.

```svelte
<script lang="ts">
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
<InputOTP.Root id="disabled" maxlength={6} disabled value="123456">
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

View Code

## [Controlled](#controlled)

Use `bind:value` to control the input value.

```svelte
<script lang="ts">
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
 let value = $state("");
</script>
<div class="space-y-2">
 <InputOTP.Root maxlength={6} bind:value>
  {#snippet children({ cells })}
   <InputOTP.Group>
    {#each cells.slice(0, 6) as cell (cell)}
     <InputOTP.Slot {cell} />
    {/each}
   </InputOTP.Group>
  {/snippet}
 </InputOTP.Root>
 <div class="text-center text-sm">
  {value === "" ? "Enter your one-time password." : `You entered: ${value}`}
 </div>
</div>
```

View Code

## [Invalid](#invalid)

Use `aria-invalid` on the slots to show an error state.

```svelte
<script lang="ts">
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
 let value = $state("000000");
</script>
<InputOTP.Root maxlength={6} bind:value>
 {#snippet children({ cells })}
  <InputOTP.Group>
   {#each cells.slice(0, 2) as cell (cell)}
    <InputOTP.Slot aria-invalid {cell} />
   {/each}
  </InputOTP.Group>
  <InputOTP.Separator />
  <InputOTP.Group>
   {#each cells.slice(2, 4) as cell (cell)}
    <InputOTP.Slot aria-invalid {cell} />
   {/each}
  </InputOTP.Group>
  <InputOTP.Separator />
  <InputOTP.Group>
   {#each cells.slice(4, 6) as cell (cell)}
    <InputOTP.Slot aria-invalid {cell} />
   {/each}
  </InputOTP.Group>
 {/snippet}
</InputOTP.Root>
```

View Code

## [Four Digits](#four-digits)

A common pattern for PIN codes. This uses the `pattern={REGEXP_ONLY_DIGITS}` prop.

```svelte
<script lang="ts">
 import { REGEXP_ONLY_DIGITS } from "bits-ui";
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
<InputOTP.Root maxlength={4} pattern={REGEXP_ONLY_DIGITS}>
 {#snippet children({ cells })}
  <InputOTP.Group>
   {#each cells as cell (cell)}
    <InputOTP.Slot {cell} />
   {/each}
  </InputOTP.Group>
 {/snippet}
</InputOTP.Root>
```

View Code

## [Alphanumeric](#alphanumeric)

Use `REGEXP_ONLY_DIGITS_AND_CHARS` to accept both letters and numbers.

```svelte
<script lang="ts">
 import { REGEXP_ONLY_DIGITS_AND_CHARS } from "bits-ui";
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
</script>
<InputOTP.Root maxlength={6} pattern={REGEXP_ONLY_DIGITS_AND_CHARS}>
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

View Code

## [Form](#form)

```svelte
<script lang="ts">
 import RefreshCwIcon from "@lucide/svelte/icons/refresh-cw";
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Field from "$lib/components/ui/field/index.js";
 import * as InputOTP from "$lib/components/ui/input-otp/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
</script>
<Card.Root class="mx-auto max-w-md">
 <Card.Header>
  <Card.Title>Verify your login</Card.Title>
  <Card.Description>
   Enter the verification code we sent to your email address:
   <span class="font-medium">m@example.com</span>.
  </Card.Description>
 </Card.Header>
 <Card.Content>
  <Field.Field>
   <div class="flex items-center justify-between">
    <Field.Label for="otp-verification">Verification code</Field.Label>
    <Button variant="outline" size="xs">
     <RefreshCwIcon />
     Resend Code
    </Button>
   </div>
   <InputOTP.Root maxlength={6} id="otp-verification" required>
    {#snippet children({ cells })}
     <InputOTP.Group
      class="*:data-[slot=input-otp-slot]:h-12 *:data-[slot=input-otp-slot]:w-11 *:data-[slot=input-otp-slot]:text-xl"
     >
      {#each cells.slice(0, 3) as cell (cell)}
       <InputOTP.Slot {cell} />
      {/each}
     </InputOTP.Group>
     <InputOTP.Separator class="mx-2" />
     <InputOTP.Group
      class="*:data-[slot=input-otp-slot]:h-12 *:data-[slot=input-otp-slot]:w-11 *:data-[slot=input-otp-slot]:text-xl"
     >
      {#each cells.slice(3, 6) as cell (cell)}
       <InputOTP.Slot {cell} />
      {/each}
     </InputOTP.Group>
    {/snippet}
   </InputOTP.Root>
   <Field.Description>
    <a href="##">I no longer have access to this email address.</a>
   </Field.Description>
  </Field.Field>
 </Card.Content>
 <Card.Footer>
  <Field.Field>
   <Button type="submit" class="w-full">Verify</Button>
   <div class="text-sm text-muted-foreground">
    Having trouble signing in?
    <a href="##" class="underline underline-offset-4 transition-colors hover:text-primary">
     Contact support
    </a>
   </div>
  </Field.Field>
 </Card.Footer>
</Card.Root>
```

View Code