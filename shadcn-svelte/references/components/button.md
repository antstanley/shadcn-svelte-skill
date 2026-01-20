# Button

Displays a button or a component that looks like a button.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add button
```

```bash
npx shadcn-svelte@latest add button
```

```bash
bun x shadcn-svelte@latest add button
```

## Usage

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>

<Button>Click me</Button>
```

## Variants

The Button component supports multiple variants:

- **default** - Primary button style
- **outline** - Border-only button
- **secondary** - Subdued button style
- **ghost** - Minimal/transparent button
- **destructive** - For dangerous actions
- **link** - Styled as a link

```svelte
<Button variant="outline">Outline</Button>
<Button variant="secondary">Secondary</Button>
<Button variant="ghost">Ghost</Button>
<Button variant="destructive">Destructive</Button>
<Button variant="link">Link</Button>
```

## Sizes

Available sizes: `sm`, `default`, `lg`, `icon`, `icon-sm`, `icon-lg`

```svelte
<Button size="sm">Small</Button>
<Button size="default">Default</Button>
<Button size="lg">Large</Button>
<Button size="icon"><SomeIcon /></Button>
```

## With Icon

The spacing between the icon and the text is automatically adjusted based on the size of the button.

```svelte
<Button>
  <MailIcon />
  Login with Email
</Button>
```

## Rounded

Add `rounded-full` class for pill-shaped buttons:

```svelte
<Button class="rounded-full">Rounded</Button>
```

## Loading State

Use the Spinner component for loading states:

```svelte
<Button disabled>
  <Spinner />
  Please wait
</Button>
```

## As Link

Pass an `href` prop to render the button as an anchor:

```svelte
<Button href="/dashboard">Go to Dashboard</Button>
```

## Button Variants Helper

Use the `buttonVariants` helper to style other elements like anchors:

```svelte
<script lang="ts">
  import { buttonVariants } from "$lib/components/ui/button/index.js";
</script>

<a href="/about" class={buttonVariants({ variant: "outline" })}>About</a>
```
