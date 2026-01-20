# Range Calendar

A calendar component that allows users to select a range of dates.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add range-calendar
```

```bash
npx shadcn-svelte@latest add range-calendar
```

```bash
bun x shadcn-svelte@latest add range-calendar
```

## Usage

```svelte
<script lang="ts">
  import { getLocalTimeZone, today } from "@internationalized/date";
  import { RangeCalendar } from "$lib/components/ui/range-calendar/index.js";

  const start = today(getLocalTimeZone());
  const end = start.add({ days: 7 });

  let value = $state({
    start,
    end,
  });
</script>

<RangeCalendar bind:value class="rounded-md border" />
```

## About

The Range Calendar component is built on top of the Bits Range Calendar component, which uses the `@internationalized/date` package to handle dates.

## Date Handling

This component uses the `@internationalized/date` package for robust date management:

```svelte
<script lang="ts">
  import { CalendarDate, getLocalTimeZone, today } from "@internationalized/date";

  // Get today's date
  const todayDate = today(getLocalTimeZone());

  // Create specific date
  const specificDate = new CalendarDate(2024, 1, 15);

  // Add days to a date
  const futureDate = todayDate.add({ days: 7 });
</script>
```

## Examples

See [Calendar Blocks](/blocks/calendar) for 30+ pre-built calendar examples.
