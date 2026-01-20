# Input Group

Display additional information or actions to an input or textarea.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add input-group
```

```bash
npx shadcn-svelte@latest add input-group
```

```bash
bun x shadcn-svelte@latest add input-group
```

## Usage

```svelte
<script lang="ts">
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
</script>

<InputGroup.Root>
  <InputGroup.Input placeholder="Search..." />
  <InputGroup.Addon align="inline-end">
    <InputGroup.Button>
      <SearchIcon />
    </InputGroup.Button>
  </InputGroup.Addon>
</InputGroup.Root>
```

## Components

- **InputGroup.Root** - Container wrapper
- **InputGroup.Input** - Text input field
- **InputGroup.Textarea** - Multi-line text area
- **InputGroup.Addon** - Container for supplementary elements
- **InputGroup.Button** - Action buttons within addons
- **InputGroup.Text** - Static text content

## Addon Alignments

The addon supports multiple alignments:

### inline-end (End of input)

```svelte
<InputGroup.Root>
  <InputGroup.Input placeholder="Search..." />
  <InputGroup.Addon align="inline-end">
    <InputGroup.Text>results</InputGroup.Text>
  </InputGroup.Addon>
</InputGroup.Root>
```

### block-end (Below input)

```svelte
<InputGroup.Root>
  <InputGroup.Input placeholder="Message" />
  <InputGroup.Addon align="block-end">
    <InputGroup.Button>Send</InputGroup.Button>
  </InputGroup.Addon>
</InputGroup.Root>
```

### block-start (Above input)

```svelte
<InputGroup.Root>
  <InputGroup.Addon align="block-start">
    <InputGroup.Text>Label</InputGroup.Text>
  </InputGroup.Addon>
  <InputGroup.Input placeholder="Value" />
</InputGroup.Root>
```

## Common Use Cases

- Search interfaces with result counts and icons
- URL inputs with protocol prefixes and validation indicators
- Chat interfaces combining textarea with action buttons and dropdowns
- Currency/unit displays with prefix and suffix text
- Code editors with language labels and controls
- Accessibility-enhanced inputs with tooltips and labels
- Loading states using spinners during data processing

## Custom Inputs

Use the `data-slot="input-group-control"` attribute to implement custom input styling while maintaining automatic focus state handling:

```svelte
<InputGroup.Root>
  <input data-slot="input-group-control" class="custom-input" />
  <InputGroup.Addon>
    <!-- addon content -->
  </InputGroup.Addon>
</InputGroup.Root>
```
