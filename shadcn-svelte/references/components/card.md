# Card

Displays a card with header, content, and footer.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add card
```

```bash
npx shadcn-svelte@latest add card
```

```bash
bun x shadcn-svelte@latest add card
```

## Usage

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
</script>

<Card.Root>
  <Card.Header>
    <Card.Title>Card Title</Card.Title>
    <Card.Description>Card Description</Card.Description>
  </Card.Header>
  <Card.Content>
    <p>Card Content</p>
  </Card.Content>
  <Card.Footer>
    <p>Card Footer</p>
  </Card.Footer>
</Card.Root>
```

## Examples

### Login Card

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
</script>

<Card.Root class="w-full max-w-sm">
  <Card.Header>
    <Card.Title>Login to your account</Card.Title>
    <Card.Description>Enter your email below to login</Card.Description>
    <Card.Action>
      <Button variant="link">Sign Up</Button>
    </Card.Action>
  </Card.Header>
  <Card.Content>
    <form>
      <div class="flex flex-col gap-6">
        <div class="grid gap-2">
          <Label for="email">Email</Label>
          <Input id="email" type="email" placeholder="m@example.com" required />
        </div>
        <div class="grid gap-2">
          <Label for="password">Password</Label>
          <Input id="password" type="password" required />
        </div>
      </div>
    </form>
  </Card.Content>
  <Card.Footer class="flex-col gap-2">
    <Button type="submit" class="w-full">Login</Button>
    <Button variant="outline" class="w-full">Login with Google</Button>
  </Card.Footer>
</Card.Root>
```

## Components

- **Card.Root** - Main container
- **Card.Header** - Header section
- **Card.Title** - Card title
- **Card.Description** - Card description
- **Card.Action** - Optional action in header
- **Card.Content** - Main content area
- **Card.Footer** - Footer section
