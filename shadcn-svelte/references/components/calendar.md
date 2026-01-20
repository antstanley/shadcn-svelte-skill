# Calendar

A calendar component that allows users to select dates.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add calendar
```

```bash
npx shadcn-svelte@latest add calendar
```

```bash
bun x shadcn-svelte@latest add calendar
```

## About

The Calendar component is built on top of the [Bits UI Calendar](https://bits-ui.com/docs/components/calendar) component, which uses the [@internationalized/date](https://react-spectrum.adobe.com/internationalized/date/index.html) package to handle dates.

## Usage

```svelte
<script lang="ts">
  import { Calendar } from "$lib/components/ui/calendar/index.js";
</script>

<Calendar />
```

The Calendar can be used as a controlled or uncontrolled component. Use the `value` prop for controlled state:

```svelte
<script lang="ts">
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import type { DateValue } from "@internationalized/date";

  let value = $state<DateValue | undefined>();
</script>

<Calendar bind:value type="single" />
```

## Examples

### Multiple Months

Display multiple months using the `numberOfMonths` prop:

```svelte
<Calendar numberOfMonths={2} />
```

### Month and Year Selector

Use the `captionLayout` prop for dropdown selectors:

```svelte
<Calendar captionLayout="dropdown" />
```

Options: `"dropdown"`, `"month"`, `"year"`

### Date of Birth Picker

Combine with Popover for a date picker with constraints:

```svelte
<script lang="ts">
  import Calendar from "$lib/components/ui/calendar/calendar.svelte";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { getLocalTimeZone, today, type CalendarDate } from "@internationalized/date";

  let open = $state(false);
  let value = $state<CalendarDate | undefined>();
</script>

<Popover.Root bind:open>
  <Popover.Trigger>
    <Button variant="outline">
      {value ? value.toDate(getLocalTimeZone()).toLocaleDateString() : "Select date"}
    </Button>
  </Popover.Trigger>
  <Popover.Content class="w-auto p-0">
    <Calendar
      type="single"
      bind:value
      captionLayout="dropdown"
      maxValue={today(getLocalTimeZone())}
      onValueChange={() => { open = false; }}
    />
  </Popover.Content>
</Popover.Root>
```

### Date and Time

Pair calendar selection with time input:

```svelte
<div class="flex gap-4">
  <Calendar type="single" bind:value />
  <Input type="time" step="1" />
</div>
```

### Natural Language Input

Use `chrono-node` to parse conversational date entries like "In 2 days":

```svelte
<script lang="ts">
  import { parseDate } from "chrono-node";
  import { CalendarDate } from "@internationalized/date";

  let inputValue = $state("In 2 days");
  // Parse and convert to CalendarDate
</script>
```

## Related

- [Range Calendar](/docs/components/range-calendar) - For date range selection
- [Date Picker](/docs/components/date-picker) - For specialized date selection
- [Calendar Blocks](https://shadcn-svelte.com/blocks/calendar) - 30+ pre-built calendar variations
