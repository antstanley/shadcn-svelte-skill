# Card

Displays a card with header, content, and footer.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<Card.Root class="-my-4 w-full max-w-sm">
  <Card.Header>
    <Card.Title>Login to your account</Card.Title>
    <Card.Description
      >Enter your email below to login to your account</Card.Description
    >
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
          <div class="flex items-center">
            <Label for="password">Password</Label>
            <a
              href="##"
              class="ms-auto inline-block text-sm underline-offset-4 hover:underline"
            >
              Forgot your password?
            </a>
          </div>
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

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add card
```

```bash
npx shadcn-svelte@latest add card
```

```bash
bun x shadcn-svelte@latest add card
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
</script>
```

```svelte
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

## [Examples](#examples)

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
</script>
<Card.Root class="-my-4 w-full max-w-sm">
  <Card.Header>
    <Card.Title>Login to your account</Card.Title>
    <Card.Description
      >Enter your email below to login to your account</Card.Description
    >
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
          <div class="flex items-center">
            <Label for="password">Password</Label>
            <a
              href="##"
              class="ms-auto inline-block text-sm underline-offset-4 hover:underline"
            >
              Forgot your password?
            </a>
          </div>
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

View Code

### [Spacing](#spacing)

In addition to the `size` prop, you can use the `--card-spacing` CSS variable to control the spacing between sections and the inset of card parts.

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import * as ToggleGroup from "$lib/components/ui/toggle-group/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  const spacingOptions = [
    {
      className: "[--card-spacing:--spacing(4)]",
      label: "16px",
      value: "4"
    },
    {
      className: "[--card-spacing:--spacing(5)]",
      label: "20px",
      value: "5"
    },
    {
      className: "[--card-spacing:--spacing(6)]",
      label: "24px",
      value: "6"
    },
    {
      className: "[--card-spacing:--spacing(8)]",
      label: "32px",
      value: "8"
    }
  ];
  let spacing = $state("4");
  let selectedSpacing = $derived(
    spacingOptions.find((option) => option.value === spacing)
  );
</script>
<div class="mx-auto grid w-full max-w-sm gap-4">
  <ToggleGroup.Root
    type="single"
    bind:value={spacing}
    variant="outline"
    size="sm"
    class="justify-center"
  >
    {#each spacingOptions as option (option.value)}
      <ToggleGroup.Item value={option.value}>{option.label}</ToggleGroup.Item>
    {/each}
  </ToggleGroup.Root>
  <Card.Root class={selectedSpacing?.className}>
    <Card.Header>
      <Card.Title>Login to your account</Card.Title>
      <Card.Description
        >Enter your email below to login to your account</Card.Description
      >
      <Card.Action>
        <Button variant="link">Sign Up</Button>
      </Card.Action>
    </Card.Header>
    <Card.Content>
      <form>
        <div class="flex flex-col gap-6">
          <div class="grid gap-2">
            <Label for="email-spacing">Email</Label>
            <Input
              id="email-spacing"
              type="email"
              placeholder="m@example.com"
              required
            />
          </div>
          <div class="grid gap-2">
            <div class="flex items-center">
              <Label for="password-spacing">Password</Label>
              <a
                href="##"
                class="ml-auto inline-block text-sm underline-offset-4 hover:underline"
              >
                Forgot your password?
              </a>
            </div>
            <Input id="password-spacing" type="password" required />
          </div>
        </div>
      </form>
    </Card.Content>
    <Card.Footer class="flex-col gap-2">
      <Button type="submit" class="w-full">Login</Button>
      <Button variant="outline" class="w-full">Login with Google</Button>
    </Card.Footer>
  </Card.Root>
</div>
```

View Code

Use negative margins with `-mx-(--card-spacing)` to make content go edge to edge while keeping it aligned with the card inset. When the edge-to-edge content sits above a footer, use `-mb-(--card-spacing)` on `CardContent` to remove the section gap.

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Card.Root class="mx-auto w-full max-w-sm">
  <Card.Header>
    <Card.Title>Terms of Service</Card.Title>
    <Card.Description
      >Review the terms before accepting the agreement.</Card.Description
    >
  </Card.Header>
  <Card.Content class="-mb-(--card-spacing)">
    <div
      class="-mx-(--card-spacing) max-h-48 space-y-4 overflow-y-scroll border-t bg-muted/50 px-(--card-spacing) py-4 text-sm leading-relaxed"
    >
      <p>
        These terms govern your use of the workspace, including access to shared
        documents, project files, and collaboration tools.
      </p>
      <p>
        You are responsible for the content you upload and for ensuring that
        your team has the appropriate permissions to view or edit it.
      </p>
      <p>
        We may update features or limits as the service evolves. When those
        changes materially affect your workflow, we will notify your workspace
        administrators.
      </p>
      <p>
        By continuing, you agree to keep your account credentials secure and to
        follow your organization's acceptable use policies.
      </p>
    </div>
  </Card.Content>
  <Card.Footer class="justify-end gap-2">
    <Button variant="outline">Decline</Button>
    <Button>Accept</Button>
  </Card.Footer>
</Card.Root>
```

View Code

### [Image](#image)

Add an image before the card header to create a card with an image.

```svelte
<script lang="ts">
  import * as Card from "$lib/components/ui/card/index.js";
  import { Badge } from "$lib/components/ui/badge/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Card.Root class="relative mx-auto w-full max-w-sm pt-0">
  <div class="absolute inset-0 z-30 aspect-video bg-black/35"></div>
  <img
    src="https://avatar.vercel.sh/shadcn1"
    alt="Event cover"
    class="relative z-20 aspect-video w-full object-cover brightness-60 grayscale dark:brightness-40"
  />
  <Card.Header>
    <Card.Action>
      <Badge variant="secondary">Featured</Badge>
    </Card.Action>
    <Card.Title>Design systems meetup</Card.Title>
    <Card.Description>
      A practical talk on component APIs, accessibility, and shipping faster.
    </Card.Description>
  </Card.Header>
  <Card.Footer>
    <Button class="w-full">View Event</Button>
  </Card.Footer>
</Card.Root>
```

View Code