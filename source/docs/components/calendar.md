# Calendar

A calendar component that allows users to select a date or a range of dates.

[Docs](https://bits-ui.com/docs/components/calendar)

[API Reference](https://bits-ui.com/docs/components/calendar#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import { getLocalTimeZone, today, type CalendarDate } from "@internationalized/date";
 import { Calendar } from "$lib/components/ui/calendar/index.js";
 let value = $state<CalendarDate | undefined>(today(getLocalTimeZone()));
</script>
<Calendar type="single" bind:value class="rounded-lg border" captionLayout="dropdown" />
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add calendar
```

```bash
npx shadcn-svelte@latest add calendar
```

```bash
bun x shadcn-svelte@latest add calendar
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import { getLocalTimeZone, today } from "@internationalized/date";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  let value = $state(today(getLocalTimeZone()));
</script>
```

```svelte
<Calendar type="single" bind:value class="rounded-lg border" />
```

See the [Bits UI Calendar](https://bits-ui.com/docs/components/calendar) documentation for more information.

## [About](#about)

The `<Calendar />` component is built on top of the [Bits UI Calendar](https://bits-ui.com/docs/components/calendar) component, which uses the [@internationalized/date](https://react-spectrum.adobe.com/internationalized/date/index.html) package to handle dates.

## [Date Picker](#date-picker)

You can use the `<Calendar />` component to build a date picker. See the [Date Picker](https://shadcn-svelte.com/docs/components/date-picker) page for more information.

## [Basic](#basic)

A basic calendar component. We used `class="rounded-lg border"` to style the calendar.

```svelte
<script lang="ts">
 import { Calendar } from "$lib/components/ui/calendar/index.js";
</script>
<Calendar type="single" class="rounded-lg border" />
```

View Code

## [Range Calendar](#range-calendar)

Use the [`RangeCalendar`](https://shadcn-svelte.com/docs/components/range-calendar) component to enable range selection.

```svelte
<script lang="ts">
 import { CalendarDate, getLocalTimeZone, today } from "@internationalized/date";
 import * as Card from "$lib/components/ui/card/index.js";
 import { RangeCalendar } from "$lib/components/ui/range-calendar/index.js";
 import type { DateRange } from "bits-ui";
 const start = new CalendarDate(today(getLocalTimeZone()).year, 1, 12);
 let value = $state<DateRange | undefined>({
  start,
  end: start.add({ days: 30 }),
 });
</script>
<Card.Root class="mx-auto w-fit p-0">
 <Card.Content class="p-0">
  <RangeCalendar
   bind:value
   numberOfMonths={2}
   minValue={new CalendarDate(1900, 1, 1)}
   maxValue={today(getLocalTimeZone())}
  />
 </Card.Content>
</Card.Root>
```

View Code

## [Month and Year Selector](#month-and-year-selector)

Use `captionLayout="dropdown"` to show month and year dropdowns.

```svelte
<script lang="ts">
 import { Calendar } from "$lib/components/ui/calendar/index.js";
</script>
<Calendar type="single" captionLayout="dropdown" class="rounded-lg border" />
```

View Code

## [Presets](#presets)

```svelte
<script lang="ts">
 import { CalendarDate, getLocalTimeZone, today } from "@internationalized/date";
 import * as Card from "$lib/components/ui/card/index.js";
 import { Button } from "$lib/components/ui/button/index.js";
 import { Calendar } from "$lib/components/ui/calendar/index.js";
 const presets = [
  { label: "Today", value: 0 },
  { label: "Tomorrow", value: 1 },
  { label: "In 3 days", value: 3 },
  { label: "In a week", value: 7 },
  { label: "In 2 weeks", value: 14 },
];
 let value = $state<CalendarDate | undefined>(
  new CalendarDate(today(getLocalTimeZone()).year, 2, 12)
 );
 let placeholder = $state<CalendarDate>(today(getLocalTimeZone()));
</script>
<Card.Root class="mx-auto w-fit max-w-[300px]" size="sm">
 <Card.Content>
  <Calendar
   type="single"
   bind:value
   bind:placeholder
   fixedWeeks
   class="p-0 [--cell-size:--spacing(9.5)]"
  />
 </Card.Content>
 <Card.Footer class="flex flex-wrap gap-2 border-t">
  {#each presets as preset (preset.value)}
   <Button
    variant="outline"
    size="sm"
    class="flex-1"
    onclick={() => {
     const newDate = today(getLocalTimeZone()).add({ days: preset.value });
     value = newDate;
     placeholder = newDate;
    }}
   >
    {preset.label}
   </Button>
  {/each}
 </Card.Footer>
</Card.Root>
```

View Code

## [Date and Time Picker](#date-and-time-picker)

```svelte
<script lang="ts">
 import Clock2Icon from "@lucide/svelte/icons/clock-2";
 import { CalendarDate, getLocalTimeZone, today } from "@internationalized/date";
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Field from "$lib/components/ui/field/index.js";
 import * as InputGroup from "$lib/components/ui/input-group/index.js";
 import { Calendar } from "$lib/components/ui/calendar/index.js";
 const now = today(getLocalTimeZone());
 let value = $state<CalendarDate | undefined>(new CalendarDate(now.year, now.month, 12));
</script>
<Card.Root size="sm" class="mx-auto w-fit">
 <Card.Content>
  <Calendar type="single" bind:value class="p-0" />
 </Card.Content>
 <Card.Footer class="border-t bg-card">
  <Field.Group>
   <Field.Field>
    <Field.Label for="time-from">Start Time</Field.Label>
    <InputGroup.Root>
     <InputGroup.Input
      id="time-from"
      type="time"
      step="1"
      value="10:30:00"
      class="appearance-none [&::-webkit-calendar-picker-indicator]:hidden [&::-webkit-calendar-picker-indicator]:appearance-none"
     />
     <InputGroup.Addon>
      <Clock2Icon class="text-muted-foreground" />
     </InputGroup.Addon>
    </InputGroup.Root>
   </Field.Field>
   <Field.Field>
    <Field.Label for="time-to">End Time</Field.Label>
    <InputGroup.Root>
     <InputGroup.Input
      id="time-to"
      type="time"
      step="1"
      value="12:30:00"
      class="appearance-none [&::-webkit-calendar-picker-indicator]:hidden [&::-webkit-calendar-picker-indicator]:appearance-none"
     />
     <InputGroup.Addon>
      <Clock2Icon class="text-muted-foreground" />
     </InputGroup.Addon>
    </InputGroup.Root>
   </Field.Field>
  </Field.Group>
 </Card.Footer>
</Card.Root>
```

View Code

## [Booked dates](#booked-dates)

```svelte
<script lang="ts">
 import { CalendarDate, getLocalTimeZone, today, type DateValue } from "@internationalized/date";
 import * as Card from "$lib/components/ui/card/index.js";
 import { Calendar } from "$lib/components/ui/calendar/index.js";
 const year = today(getLocalTimeZone()).year;
 let value = $state<CalendarDate | undefined>(new CalendarDate(year, 2, 3));
 const bookedDates = Array.from({ length: 15 }, (_, i) => new CalendarDate(year, 2, 12 + i));
 function isBooked(date: DateValue) {
  return bookedDates.some((d) => d.compare(date) === 0);
 }
</script>
<Card.Root class="mx-auto w-fit p-0">
 <Card.Content class="p-0">
  <Calendar type="single" bind:value isDateUnavailable={isBooked} />
 </Card.Content>
</Card.Root>
```

View Code

## [Custom Cell Size](#custom-cell-size)

```svelte
<script lang="ts">
 import { CalendarDate, getLocalTimeZone, isWeekend, today } from "@internationalized/date";
 import * as Card from "$lib/components/ui/card/index.js";
 import RangeCalendarDay from "$lib/components/ui/range-calendar/range-calendar-day.svelte";
 import { RangeCalendar } from "$lib/components/ui/range-calendar/index.js";
 import type { DateRange } from "bits-ui";
 const start = new CalendarDate(today(getLocalTimeZone()).year, 12, 8);
 let value = $state<DateRange | undefined>({
  start,
  end: start.add({ days: 10 }),
 });
</script>
<Card.Root class="mx-auto w-fit p-0">
 <Card.Content class="p-0">
  <RangeCalendar
   bind:value
   captionLayout="dropdown"
   monthFormat="long"
   class="[--cell-size:--spacing(10)] md:[--cell-size:--spacing(12)]"
  >
   {#snippet day({ day, outsideMonth })}
    <RangeCalendarDay>
     {day.day}
     {#if !outsideMonth}
      <span>{isWeekend(day, "en-US") ? "$120" : "$100"}</span>
     {/if}
    </RangeCalendarDay>
   {/snippet}
  </RangeCalendar>
 </Card.Content>
</Card.Root>
```

View Code

You can customize the size of calendar cells using the `--cell-size` CSS variable. You can also make it responsive by using breakpoint-specific values:

```svelte
<Calendar
  type="single"
  bind:value
  class="rounded-lg border [--cell-size:--spacing(11)] md:[--cell-size:--spacing(12)]"
/>
```

Or use fixed values:

```svelte
<Calendar
  type="single"
  bind:value
  class="rounded-lg border [--cell-size:2.75rem] md:[--cell-size:3rem]"
/>
```