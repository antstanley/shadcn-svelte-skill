# Button

Displays a button or a component that looks like a button.

[API Reference](https://bits-ui.com/docs/components/button#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

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

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add button
```

```bash
npx shadcn-svelte@latest add button
```

```bash
bun x shadcn-svelte@latest add button
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="outline">Button</Button>
```

## [Cursor](#cursor)

Tailwind v4 [switched](https://tailwindcss.com/docs/upgrade-guide#buttons-use-the-default-cursor) from `cursor: pointer` to `cursor: default` for the button component.

If you want to keep the `cursor: pointer` behavior, add the following code to your CSS file:

app.css

```css
@layer base {
  button:not(:disabled),
  [role="button"]:not(:disabled) {
    cursor: pointer;
  }
}
```

## [Size](#size)

Use the `size` prop to change the size of the button.

```svelte
<script lang="ts">
  import ArrowUpRightIcon from "@lucide/svelte/icons/arrow-up-right";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex flex-col items-start gap-8 sm:flex-row">
  <div class="flex items-start gap-2">
    <Button size="xs" variant="outline">Extra Small</Button>
    <Button size="icon-xs" aria-label="Submit" variant="outline">
      <ArrowUpRightIcon />
    </Button>
  </div>
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

View Code

## [Default](#default)

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button>Button</Button>
```

View Code

## [Outline](#outline)

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="outline">Outline</Button>
```

View Code

## [Secondary](#secondary)

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="secondary">Secondary</Button>
```

View Code

## [Ghost](#ghost)

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="ghost">Ghost</Button>
```

View Code

## [Destructive](#destructive)

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="destructive">Destructive</Button>
```

View Code

## [Link](#link)

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="link">Link</Button>
```

View Code

## [Icon](#icon)

```svelte
<script lang="ts">
  import CircleFadingArrowUpIcon from "@lucide/svelte/icons/circle-fading-arrow-up";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button variant="outline" size="icon" aria-label="Submit">
  <CircleFadingArrowUpIcon />
</Button>
```

View Code

## [With Icon](#with-icon)

Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the icon for the correct spacing.

```svelte
<script lang="ts">
  import IconGitBranch from "@tabler/icons-svelte/icons/git-branch";
  import IconGitFork from "@tabler/icons-svelte/icons/git-fork";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex gap-2">
  <Button variant="outline">
    <IconGitBranch data-icon="inline-start" /> New Branch
  </Button>
  <Button variant="outline">
    Fork
    <IconGitFork data-icon="inline-end" />
  </Button>
</div>
```

View Code

## [Rounded](#rounded)

Use the `rounded-full` class to make the button rounded.

```svelte
<script lang="ts">
  import ArrowUpIcon from "@lucide/svelte/icons/arrow-up";
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<div class="flex gap-2">
  <Button class="rounded-full">Get Started</Button>
  <Button variant="outline" size="icon" class="rounded-full">
    <ArrowUpIcon />
  </Button>
</div>
```

View Code

## [Spinner](#spinner)

Render a `<Spinner />` component inside the button to show a loading state. Remember to add the `data-icon="inline-start"` or `data-icon="inline-end"` attribute to the spinner for the correct spacing.

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
  import { Spinner } from "$lib/components/ui/spinner/index.js";
</script>
<div class="flex gap-2">
  <Button variant="outline" disabled>
    <Spinner data-icon="inline-start" />
    Generating
  </Button>
  <Button variant="secondary" disabled>
    Downloading
    <Spinner data-icon="inline-end" />
  </Button>
</div>
```

View Code

## [Button Group](#button-group)

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
  import * as ButtonGroup from "$lib/components/ui/button-group/index.js";
  import * as DropdownMenu from "$lib/components/ui/dropdown-menu/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  let label = $state("personal");
</script>
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
      <DropdownMenu.Content align="end" class="w-40">
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
                <DropdownMenu.RadioItem value="personal"
                  >Personal</DropdownMenu.RadioItem
                >
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
          <DropdownMenu.Item variant="destructive">
            <Trash2 />
            Trash
          </DropdownMenu.Item>
        </DropdownMenu.Group>
      </DropdownMenu.Content>
    </DropdownMenu.Root>
  </ButtonGroup.Root>
</ButtonGroup.Root>
```

View Code

## [As Link](#as-link)

Pass an `href` prop to `<Button />` to render it as an `<a>` element that looks like a button. You can also use the `buttonVariants` helper to make any other element look like a button.

```svelte
<script lang="ts">
  import { Button } from "$lib/components/ui/button/index.js";
</script>
<Button href="#" variant="secondary" size="sm">Login</Button>
```

View Code