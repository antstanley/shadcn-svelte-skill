# Accordion

A vertically stacked set of interactive headings that each reveal a section of content.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add accordion
```

```bash
npx shadcn-svelte@latest add accordion
```

```bash
bun x shadcn-svelte@latest add accordion
```

## Usage

```svelte
<script lang="ts">
  import * as Accordion from "$lib/components/ui/accordion/index.js";
</script>

<Accordion.Root type="single">
  <Accordion.Item value="item-1">
    <Accordion.Trigger>Is it accessible?</Accordion.Trigger>
    <Accordion.Content>
      Yes. It adheres to the WAI-ARIA design pattern.
    </Accordion.Content>
  </Accordion.Item>
</Accordion.Root>
```

## Examples

### Single Accordion

Only one item can be open at a time:

```svelte
<Accordion.Root type="single" class="w-full" value="item-1">
  <Accordion.Item value="item-1">
    <Accordion.Trigger>Product Information</Accordion.Trigger>
    <Accordion.Content>
      Our flagship product combines cutting-edge technology with sleek design.
    </Accordion.Content>
  </Accordion.Item>
  <Accordion.Item value="item-2">
    <Accordion.Trigger>Shipping Details</Accordion.Trigger>
    <Accordion.Content>
      We offer worldwide shipping through trusted courier partners.
    </Accordion.Content>
  </Accordion.Item>
  <Accordion.Item value="item-3">
    <Accordion.Trigger>Return Policy</Accordion.Trigger>
    <Accordion.Content>
      We stand behind our products with a comprehensive 30-day return policy.
    </Accordion.Content>
  </Accordion.Item>
</Accordion.Root>
```

### Multiple Accordion

Multiple items can be open simultaneously:

```svelte
<Accordion.Root type="multiple">
  <Accordion.Item value="item-1">
    <Accordion.Trigger>Section 1</Accordion.Trigger>
    <Accordion.Content>Content for section 1</Accordion.Content>
  </Accordion.Item>
  <Accordion.Item value="item-2">
    <Accordion.Trigger>Section 2</Accordion.Trigger>
    <Accordion.Content>Content for section 2</Accordion.Content>
  </Accordion.Item>
</Accordion.Root>
```

## API

Built on [Bits UI Accordion](https://bits-ui.com/docs/components/accordion).

### Accordion.Root Props

- `type` - "single" or "multiple"
- `value` - Currently open item(s)
- `disabled` - Whether the accordion is disabled
- `collapsible` - Whether items can be collapsed (single mode)

### Accordion.Item Props

- `value` - Unique identifier for the item
- `disabled` - Whether this item is disabled

### Accordion.Trigger Props

- Default trigger styling with chevron icon

### Accordion.Content Props

- Animated content reveal with smooth transitions
