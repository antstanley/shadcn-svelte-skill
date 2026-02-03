# Button

Displays a button or a component that looks like a button.

[API Reference](https://bits-ui.com/docs/components/button#api-reference)

**Updated:** We have updated the button component to add new sizes: `icon-sm` and `icon-lg`. See the [changelog](https://shadcn-svelte.com/docs/components/button#changelog) for more details. Follow the instructions to update your project.

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex flex-wrap items-center gap-2 md:flex-row">
  <Button variant="outline">Button</Button>
  <Button variant="outline" size="icon" aria-label="Submit">
    <ArrowUpIcon />
  </Button>
</div>
```

```svelte
<Button variant="outline">Button</Button>
<Button variant="outline" size="icon" aria-label="Submit">
  <ArrowUpIcon />
</Button>
```

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
<Button variant="outline">Button</Button>
```

## Examples

### Size

```svelte
<script lang="ts">
  import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex flex-col items-start gap-8 sm:flex-row">
  <div class="flex items-start gap-2">
    <Button size="sm" variant="outline">Small</Button>
    <Button size="icon-sm" aria-label="Submit" variant="outline">
      <ArrowUpRightIcon />
    </Button>
  </div>
  <div class="flex items-start gap-2">
    <Button variant="outline">Default</Button>
    <Button size="icon" aria-label="Submit" variant="outline">
      <ArrowUpRightIcon />
    </Button>
  </div>
  <div class="flex items-start gap-2">
    <Button variant="outline" size="lg">Large</Button>
    <Button size="icon-lg" aria-label="Submit" variant="outline">
      <ArrowUpRightIcon />
    </Button>
  </div>
</div>
```

```svelte

<Button size="sm" variant="outline">Small</Button>
<Button size="icon-sm" aria-label="Submit" variant="outline">
  <ArrowUpRightIcon />
</Button>

<Button variant="outline">Default</Button>
<Button size="icon" aria-label="Submit" variant="outline">
  <ArrowUpRightIcon />
</Button>

<Button size="lg" variant="outline">Large</Button>
<Button size="icon-lg" aria-label="Submit" variant="outline">
  <ArrowUpRightIcon />
</Button>
```

### Default

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button>Button</Button>
```

```svelte
<Button>Button</Button>
```

### Outline

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="outline">Outline</Button>
```

```svelte
<Button variant="outline">Outline</Button>
```

### Secondary

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="secondary">Secondary</Button>
```

```svelte
<Button variant="secondary">Secondary</Button>
```

### Ghost

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="ghost">Ghost</Button>
```

```svelte
<Button variant="ghost">Ghost</Button>
```

### Destructive

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="destructive">Destructive</Button>
```

```svelte
<Button variant="destructive">Destructive</Button>
```

### Link

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="link">Link</Button>
```

```svelte
<Button variant="link">Link</Button>
```

### Icon

```svelte
<script lang="ts">
  import CircleFadingArrowUpIcon from "@lucide/svelte/icons/circle-fading-arrow-up";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="outline" size="icon" aria-label="Submit">
  <CircleFadingArrowUpIcon />
</Button>
```

```svelte
<Button variant="outline" size="icon" aria-label="Submit">
  <CircleFadingArrowUpIcon />
</Button>
```

### With Icon

The spacing between the icon and the text is automatically adjusted based on the size of the button. You do not need any margin on the icon.

```svelte
<script lang="ts">
  import IconGitBranch from "@lucide/svelte/icons/git-branch";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="outline" size="sm">
  <IconGitBranch /> New Branch
</Button>
```

```svelte
<Button variant="outline" size="sm">
  <IconGitBranch /> New Branch
</Button>
```

### Rounded

Use the `rounded-full` class to make the button rounded.

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex flex-col gap-8">
  <Button variant="outline" size="icon" class="rounded-full">
    <ArrowUpIcon />
  </Button>
</div>
```

```svelte
<Button variant="outline" size="icon" className="rounded-full">
  <ArrowUpRightIcon />
</Button>
```

### Spinner

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<Button size="sm" variant="outline" disabled>
  <Spinner />
  Submit
</Button>
```

```svelte
<Button size="sm" variant="outline" disabled>
  <Spinner />
  Submit
</Button>
```

### Button Group

To create a button group, use the `ButtonGroup` component. See the [Button Group](https://shadcn-svelte.com/docs/components/button-group) documentation for more details.

```svelte
<script lang="ts">
  import Archive from "@lucide/svelte/icons/archive";
  import ArrowLeft from "@lucide/svelte/icons/arrow-left";
  import CalendarPlus from "@lucide/svelte/icons/calendar-plus";
  import Clock from "@lucide/svelte/icons/clock";
  import ListFilter from "@lucide/svelte/icons/list-filter";
  import MailCheck from "@lucide/svelte/icons/mail-check";
  import MoreHorizontal from "@lucide/svelte/icons/more-horizontal";
  import Tag from "@lucide/svelte/icons/tag";
  import Trash2 from "@lucide/svelte/icons/trash-2";
  import { Button } from "$lib/components/ui/button/index.js";
  import * as ButtonGroup from "$lib/components/ui/button-group/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  let label = $state("personal");
</script>
<ButtonGroup.Root>
  <ButtonGroup.Root class="hidden sm:flex">
    <Button variant="outline" size="icon-sm" aria-label="Go Back">
      <ArrowLeft />
    </Button>
  </ButtonGroup.Root>
  <ButtonGroup.Root>
    <Button size="sm" variant="outline">Archive</Button>
    <Button size="sm" variant="outline">Report</Button>
  </ButtonGroup.Root>
  <ButtonGroup.Root>
    <Button size="sm" variant="outline">Snooze</Button>
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>
        {#snippet child({ props })}
          <Button
            {...props}
            variant="outline"
            size="icon-sm"
            aria-label="More Options"
          >
            <MoreHorizontal />
          </Button>
        {/snippet}
      </DropdownMenu.Trigger>
      <DropdownMenu.Content align="end" class="w-52">
        <DropdownMenu.Group>
          <DropdownMenu.Item>
            <MailCheck />
            Mark as Read
          </DropdownMenu.Item>
          <DropdownMenu.Item>
            <Archive />
            Archive
          </DropdownMenu.Item>
        </DropdownMenu.Group>
        <DropdownMenu.Separator />
        <DropdownMenu.Group>
          <DropdownMenu.Item>
            <Clock />
            Snooze
          </DropdownMenu.Item>
          <DropdownMenu.Item>
            <CalendarPlus />
            Add to Calendar
          </DropdownMenu.Item>
          <DropdownMenu.Item>
            <ListFilter />
            Add to List
          </DropdownMenu.Item>
          <DropdownMenu.Sub>
            <DropdownMenu.SubTrigger>
              <Tag />
              Label As...
            </DropdownMenu.SubTrigger>
            <DropdownMenu.SubContent>
              <DropdownMenu.RadioGroup bind:value={label}>
                <DropdownMenu.RadioItem value="personal">
                  Personal
                </DropdownMenu.RadioItem>
                <DropdownMenu.RadioItem value="work"
                  >Work</DropdownMenu.RadioItem
                >
                <DropdownMenu.RadioItem value="other"
                  >Other</DropdownMenu.RadioItem
                >
              </DropdownMenu.RadioGroup>
            </DropdownMenu.SubContent>
          </DropdownMenu.Sub>
        </DropdownMenu.Group>
        <DropdownMenu.Separator />
        <DropdownMenu.Group>
          <DropdownMenu.Item class="text-destructive focus:text-destructive">
            <Trash2 />
            Trash
          </DropdownMenu.Item>
        </DropdownMenu.Group>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </ButtonGroup.Root>
</ButtonGroup.Root>
```

```svelte
<ButtonGroup.Root>
  <ButtonGroup.Root class="hidden sm:flex">
    <Button variant="outline" size="icon" aria-label="Go Back">
      <ArrowLeft />
    </Button>
  </ButtonGroup.Root>
  <ButtonGroup.Root>
    <Button variant="outline">Archive</Button>
    <Button variant="outline">Report</Button>
  </ButtonGroup.Root>
  <ButtonGroup.Root>
    <Button variant="outline">Snooze</Button>
    <DropdownMenu.Root>
      <DropdownMenu.Trigger>
        {#snippet child({ props })}
          <Button
            {...props}
            variant="outline"
            size="icon"
            aria-label="More Options"
          >
            <MoreHorizontal />
          </Button>
        {/snippet}
      </DropdownMenu.Trigger>
      <DropdownMenu.Content align="end" class="w-52">
        <DropdownMenu.Group>
          <DropdownMenu.Item>
            <MailCheck />
            Mark as Read
          </DropdownMenu.Item>
          <DropdownMenu.Item>
            <Archive />
            Archive
          </DropdownMenu.Item>
        </DropdownMenu.Group>
        <DropdownMenu.Separator />
        <DropdownMenu.Group>
          <DropdownMenu.Item>
            <Clock />
            Snooze
          </DropdownMenu.Item>
          <DropdownMenu.Item>
            <CalendarPlus />
            Add to Calendar
          </DropdownMenu.Item>
          <DropdownMenu.Item>
            <ListFilter />
            Add to List
          </DropdownMenu.Item>
          <DropdownMenu.Sub>
            <DropdownMenu.SubTrigger>
              <Tag />
              Label As...
            </DropdownMenu.SubTrigger>
            <DropdownMenu.SubContent>
              <DropdownMenu.RadioGroup bind:value={label}>
                <DropdownMenu.RadioItem value="personal">
                  Personal
                </DropdownMenu.RadioItem>
                <DropdownMenu.RadioItem value="work"
                  >Work</DropdownMenu.RadioItem
                >
                <DropdownMenu.RadioItem value="other"
                  >Other</DropdownMenu.RadioItem
                >
              </DropdownMenu.RadioGroup>
            </DropdownMenu.SubContent>
          </DropdownMenu.Sub>
        </DropdownMenu.Group>
        <DropdownMenu.Separator />
        <DropdownMenu.Group>
          <DropdownMenu.Item class="text-destructive focus:text-destructive">
            <Trash2 />
            Trash
          </DropdownMenu.Item>
        </DropdownMenu.Group>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </ButtonGroup.Root>
</ButtonGroup.Root>
```

### Link

You can convert the `<button>` into an `<a>` element by simply passing an `href` as a prop.

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button href="/dashboard">Dashboard</Button>
```

Alternatively, you can use the `buttonVariants` helper to create a link that looks like a button.

```svelte
<script lang="ts">
  import { buttonVariants } from "$lib/components/ui/button";
</script>
<a href="/dashboard" class={buttonVariants({ variant: "outline" })}>
  Dashboard
</a>
```

## Changelog

### 2025-09-24 New sizes

We have added two new sizes to the button component: `icon-sm` and `icon-lg`. These sizes are used to create icon buttons. To add them, edit `button.svelte` and add the following code under `size` in `buttonVariants`:

components/ui/button.svelte

```ts
export const buttonVariants = tv({
  // ...
  variants: {
    // ...
    size: {
      // ...
      icon: "size-9",
      "icon-sm": "size-8",
      "icon-lg": "size-10",
    },
  },
});
```