# Date Picker

A date picker component with range and presets.

## Installation

The Date Picker is built using a composition of the `<Popover />` and either the `<Calendar />` or `<RangeCalendar />` components.

See installation instructions for the [Popover](/docs/components/popover#installation), [Calendar](/docs/components/calendar#installation), and [Range Calendar](/docs/components/range-calendar#installation) components.

## Usage

```svelte
<script lang="ts">
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import { type DateValue, DateFormatter, getLocalTimeZone } from "@internationalized/date";
  import { cn } from "$lib/utils.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";

  const df = new DateFormatter("en-US", { dateStyle: "long" });
  let value = $state<DateValue>();
</script>

<Popover.Root>
  <Popover.Trigger>
    {#snippet child({ props })}
      <Button
        variant="outline"
        class={cn(
          "w-[280px] justify-start text-start font-normal",
          !value && "text-muted-foreground"
        )}
        {...props}
      >
        <CalendarIcon class="me-2 size-4" />
        {value ? df.format(value.toDate(getLocalTimeZone())) : "Select a date"}
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-auto p-0">
    <Calendar bind:value type="single" initialFocus captionLayout="dropdown" />
  </Popover.Content>
</Popover.Root>
```

## Examples

### Date of Birth Picker

```svelte
<script lang="ts">
  import Calendar from "$lib/components/ui/calendar/calendar.svelte";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { getLocalTimeZone, today, type CalendarDate } from "@internationalized/date";

  let open = $state(false);
  let value = $state<CalendarDate | undefined>();
</script>

<div class="flex flex-col gap-3">
  <Label for="date" class="px-1">Date of birth</Label>
  <Popover.Root bind:open>
    <Popover.Trigger id="date">
      {#snippet child({ props })}
        <Button {...props} variant="outline" class="w-48 justify-between font-normal">
          {value ? value.toDate(getLocalTimeZone()).toLocaleDateString() : "Select date"}
          <ChevronDownIcon />
        </Button>
      {/snippet}
    </Popover.Trigger>
    <Popover.Content class="w-auto overflow-hidden p-0" align="start">
      <Calendar
        type="single"
        bind:value
        captionLayout="dropdown"
        onValueChange={() => { open = false; }}
        maxValue={today(getLocalTimeZone())}
      />
    </Popover.Content>
  </Popover.Root>
</div>
```

### Date and Time Picker

```svelte
<div class="flex gap-4">
  <div class="flex flex-col gap-3">
    <Label for="date" class="px-1">Date</Label>
    <Popover.Root bind:open>
      <Popover.Trigger id="date">
        {#snippet child({ props })}
          <Button {...props} variant="outline" class="w-32 justify-between font-normal">
            {value ? value.toDate(getLocalTimeZone()).toLocaleDateString() : "Select date"}
            <ChevronDownIcon />
          </Button>
        {/snippet}
      </Popover.Trigger>
      <Popover.Content class="w-auto overflow-hidden p-0" align="start">
        <Calendar type="single" bind:value captionLayout="dropdown" />
      </Popover.Content>
    </Popover.Root>
  </div>
  <div class="flex flex-col gap-3">
    <Label for="time" class="px-1">Time</Label>
    <Input type="time" id="time" step="1" value="10:30:00" />
  </div>
</div>
```

### Natural Language Picker

Uses the `chrono-node` library to parse natural language dates like "In 2 days", "Tomorrow", or "Next week".

```svelte
<script lang="ts">
  import { parseDate } from "chrono-node";
  import { CalendarDate, getLocalTimeZone, type DateValue } from "@internationalized/date";

  let inputValue = $state("In 2 days");
  let value = $state<DateValue | undefined>();

  // Parse input and convert to CalendarDate
  $effect(() => {
    const date = parseDate(inputValue);
    if (date) {
      value = new CalendarDate(
        date.getFullYear(),
        date.getMonth() + 1,
        date.getDate()
      );
    }
  });
</script>

<Input
  bind:value={inputValue}
  placeholder="Tomorrow or next week"
/>
```
