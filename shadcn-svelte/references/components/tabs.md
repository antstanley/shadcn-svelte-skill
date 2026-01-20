# Tabs

A set of layered sections of content—known as tab panels—that are displayed one at a time.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add tabs
```

```bash
npx shadcn-svelte@latest add tabs
```

```bash
bun x shadcn-svelte@latest add tabs
```

## Usage

```svelte
<script lang="ts">
  import * as Tabs from "$lib/components/ui/tabs/index.js";
</script>

<Tabs.Root value="account" class="w-[400px]">
  <Tabs.List>
    <Tabs.Trigger value="account">Account</Tabs.Trigger>
    <Tabs.Trigger value="password">Password</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="account">
    Make changes to your account here.
  </Tabs.Content>
  <Tabs.Content value="password">
    Change your password here.
  </Tabs.Content>
</Tabs.Root>
```

## Examples

### With Cards

```svelte
<script lang="ts">
  import * as Tabs from "$lib/components/ui/tabs/index.js";
  import * as Card from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>

<Tabs.Root value="account">
  <Tabs.List>
    <Tabs.Trigger value="account">Account</Tabs.Trigger>
    <Tabs.Trigger value="password">Password</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="account">
    <Card.Root>
      <Card.Header>
        <Card.Title>Account</Card.Title>
        <Card.Description>
          Make changes to your account here. Click save when you're done.
        </Card.Description>
      </Card.Header>
      <Card.Content class="grid gap-6">
        <div class="grid gap-3">
          <Label for="name">Name</Label>
          <Input id="name" value="Pedro Duarte" />
        </div>
        <div class="grid gap-3">
          <Label for="username">Username</Label>
          <Input id="username" value="@peduarte" />
        </div>
      </Card.Content>
      <Card.Footer>
        <Button>Save changes</Button>
      </Card.Footer>
    </Card.Root>
  </Tabs.Content>
  <Tabs.Content value="password">
    <Card.Root>
      <Card.Header>
        <Card.Title>Password</Card.Title>
        <Card.Description>
          Change your password here. After saving, you'll be logged out.
        </Card.Description>
      </Card.Header>
      <Card.Content class="grid gap-6">
        <div class="grid gap-3">
          <Label for="current">Current password</Label>
          <Input id="current" type="password" />
        </div>
        <div class="grid gap-3">
          <Label for="new">New password</Label>
          <Input id="new" type="password" />
        </div>
      </Card.Content>
      <Card.Footer>
        <Button>Save password</Button>
      </Card.Footer>
    </Card.Root>
  </Tabs.Content>
</Tabs.Root>
```

## Components

- **Tabs.Root** - Container with value state
- **Tabs.List** - Tab trigger container
- **Tabs.Trigger** - Clickable tab button
- **Tabs.Content** - Tab panel content

## API

Built on [Bits UI Tabs](https://bits-ui.com/docs/components/tabs).

### Props

#### Tabs.Root

- `value` - Currently active tab
- `onValueChange` - Callback when tab changes

#### Tabs.Trigger

- `value` - Tab identifier (matches content)
- `disabled` - Whether the tab is disabled

#### Tabs.Content

- `value` - Tab identifier (matches trigger)
