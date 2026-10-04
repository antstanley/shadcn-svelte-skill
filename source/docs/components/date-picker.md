# Date Picker

A date picker component with range and presets.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import {
    DateFormatter,
    type DateValue,
    getLocalTimeZone
  } from "@internationalized/date";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  const df = new DateFormatter("en-US", {
    dateStyle: "long"
  });
  let value = $state<DateValue | undefined>();
</script>
<Popover.Root>
  <Popover.Trigger>
    {#snippet child({ props })}
      <Button
        {...props}
        variant="outline"
        data-empty={!value}
        class="w-[212px] justify-between text-start font-normal data-[empty=true]:text-muted-foreground"
      >
        {value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date"}
        <ChevronDownIcon data-icon="inline-end" />
      </Button>
    {/snippet}
  </Popover.Trigger>
  <Popover.Content class="w-auto p-0" align="start">
    <Calendar type="single" bind:value />
  </Popover.Content>
</Popover.Root>
```

View Code

## [Installation](#installation)

The Date Picker is built using a composition of the `<Popover />` and either the `<Calendar />` or `<RangeCalendar />` components.

See installations instructions for the [Popover](https://shadcn-svelte.com/docs/components/popover#installation), [Calendar](https://shadcn-svelte.com/docs/components/calendar#installation), and [Range Calendar](https://shadcn-svelte.com/docs/components/range-calendar#installation) components.

## [Usage](#usage)

lib/components/example-date-picker.svelte

```svelte
<script lang="ts">
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import {
    type DateValue,
    DateFormatter,
    getLocalTimeZone,
  } from "@internationalized/date";
  import { cn } from "$lib/utils.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  const df = new DateFormatter("en-US", {
    dateStyle: "long",
  });
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

## [Composition](#composition)

A date picker is built from `Popover` and `Calendar` (there is no `DatePicker` root component):

```text
Popover.Root
 Popover.Trigger
 Popover.Content
     Calendar
```

## [Basic](#basic)

A basic date picker component.

```svelte
<script lang="ts">
  import {
    DateFormatter,
    type DateValue,
    getLocalTimeZone
  } from "@internationalized/date";
  import * as Field from "$lib/components/ui/field/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  const df = new DateFormatter("en-US", {
    dateStyle: "long"
  });
  let value = $state<DateValue | undefined>();
</script>
<Field.Field class="mx-auto w-44">
  <Field.Label for="date-picker-simple">Date</Field.Label>
  <Popover.Root>
    <Popover.Trigger id="date-picker-simple">
      {#snippet child({ props })}
        <Button {...props} variant="outline" class="justify-start font-normal">
          {value ? df.format(value.toDate(getLocalTimeZone())) : "Pick a date"}
        </Button>
      {/snippet}
    </Popover.Trigger>
    <Popover.Content class="w-auto p-0" align="start">
      <Calendar type="single" bind:value />
    </Popover.Content>
  </Popover.Root>
</Field.Field>
```

View Code

## [Range Picker](#range-picker)

A date picker component for selecting a range of dates.

```svelte
<script lang="ts">
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import {
    CalendarDate,
    DateFormatter,
    getLocalTimeZone,
    today
  } from "@internationalized/date";
  import * as Field from "$lib/components/ui/field/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { RangeCalendar } from "$lib/components/ui/range-calendar/index.js";
  import type { DateRange } from "bits-ui";
  const df = new DateFormatter("en-US", {
    dateStyle: "medium"
  });
  const year = today(getLocalTimeZone()).year;
  let value = $state<DateRange | undefined>({
    start: new CalendarDate(year, 1, 20),
    end: new CalendarDate(year, 1, 20).add({ days: 20 })
  });
</script>
<Field.Field class="mx-auto w-60">
  <Field.Label for="date-picker-range">Date Picker Range</Field.Label>
  <Popover.Root>
    <Popover.Trigger id="date-picker-range">
      {#snippet child({ props })}
        <Button
          {...props}
          variant="outline"
          class="justify-start px-2.5 font-normal"
        >
          <CalendarIcon data-icon="inline-start" />
          {#if value?.start}
            {#if value.end}
              {df.format(value.start.toDate(getLocalTimeZone()))} - {df.format( value.end.toDate(getLocalTimeZone())
              )}
            {:else}
              {df.format(value.start.toDate(getLocalTimeZone()))}
            {/if}
          {:else}
            <span>Pick a date</span>
          {/if}
        </Button>
      {/snippet}
    </Popover.Trigger>
    <Popover.Content class="w-auto p-0" align="start">
      <RangeCalendar bind:value numberOfMonths={2} />
    </Popover.Content>
  </Popover.Root>
</Field.Field>
```

View Code

## [Date of Birth](#date-of-birth)

A date picker component for selecting a date of birth. This component includes a dropdown caption layout for date and month selection.

```svelte
<script lang="ts">
  import { getLocalTimeZone, type DateValue } from "@internationalized/date";
  import * as Field from "$lib/components/ui/field/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  let open = $state(false);
  let value = $state<DateValue | undefined>();
</script>
<Field.Field class="mx-auto w-44">
  <Field.Label for="date">Date of birth</Field.Label>
  <Popover.Root bind:open>
    <Popover.Trigger id="date">
      {#snippet child({ props })}
        <Button {...props} variant="outline" class="justify-start font-normal">
          {value
            ? value.toDate(getLocalTimeZone()).toLocaleDateString()
            : "Select date"}
        </Button>
      {/snippet}
    </Popover.Trigger>
    <Popover.Content class="w-auto overflow-hidden p-0" align="start">
      <Calendar
        type="single"
        bind:value
        captionLayout="dropdown"
        onValueChange={() => {
          open = false;
        }}
      />
    </Popover.Content>
  </Popover.Root>
</Field.Field>
```

View Code

## [Input](#input)

A date picker component with an input field for selecting a date.

```svelte
<script lang="ts">
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import {
    CalendarDate,
    getLocalTimeZone,
    type DateValue
  } from "@internationalized/date";
  import { untrack } from "svelte";
  import * as Field from "$lib/components/ui/field/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  function formatDate(date: DateValue | undefined) {
    if (!date) return "";
    return date.toDate(getLocalTimeZone()).toLocaleDateString("en-US", {
      day: "2-digit",
      month: "long",
      year: "numeric"
    });
  }
  function isValidDate(date: Date | undefined): date is Date {
    if (!date) return false;
    return !isNaN(date.getTime());
  }
  let open = $state(false);
  let value = $state<DateValue | undefined>(new CalendarDate(2025, 6, 1));
  let month = $state<DateValue | undefined>(untrack(() => value));
  let inputValue = $state(untrack(() => formatDate(value)));
</script>
<Field.Field class="mx-auto w-48">
  <Field.Label for="date-required">Subscription Date</Field.Label>
  <InputGroup.Root>
    <InputGroup.Input
      id="date-required"
      placeholder="June 01, 2025"
      bind:value={
        () => inputValue,
        (v) => {
          inputValue = v;
          const date = new Date(v);
          if (isValidDate(date)) {
            value = new CalendarDate(
              date.getFullYear(),
              date.getMonth() + 1,
              date.getDate()
            );
            month = value;
          }
        }
      }
      onkeydown={(e) => {
        if (e.key === "ArrowDown") {
          e.preventDefault();
          open = true;
        }
      }}
    />
    <InputGroup.Addon align="inline-end">
      <Popover.Root bind:open>
        <Popover.Trigger id="date-picker">
          {#snippet child({ props })}
            <InputGroup.Button
              {...props}
              variant="ghost"
              size="icon-xs"
              aria-label="Select date"
            >
              <CalendarIcon />
              <span class="sr-only">Select date</span>
            </InputGroup.Button>
          {/snippet}
        </Popover.Trigger>
        <Popover.Content
          class="w-auto overflow-hidden p-0"
          align="end"
          alignOffset={-8}
          sideOffset={10}
        >
          <Calendar
            type="single"
            bind:value
            bind:placeholder={month}
            onValueChange={(v) => {
              inputValue = formatDate(v);
              open = false;
            }}
          />
        </Popover.Content>
      </Popover.Root>
    </InputGroup.Addon>
  </InputGroup.Root>
</Field.Field>
```

View Code

## [Time Picker](#time-picker)

A date picker component with a time input field for selecting a time.

```svelte
<script lang="ts">
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import {
    DateFormatter,
    getLocalTimeZone,
    type DateValue
  } from "@internationalized/date";
  import * as Field from "$lib/components/ui/field/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  const df = new DateFormatter("en-US", {
    dateStyle: "long"
  });
  let open = $state(false);
  let value = $state<DateValue | undefined>();
</script>
<Field.Group class="mx-auto max-w-xs flex-row">
  <Field.Field>
    <Field.Label for="date-picker-optional">Date</Field.Label>
    <Popover.Root bind:open>
      <Popover.Trigger id="date-picker-optional">
        {#snippet child({ props })}
          <Button
            {...props}
            variant="outline"
            class="w-32 justify-between font-normal"
          >
            {value
              ? df.format(value.toDate(getLocalTimeZone()))
              : "Select date"}
            <ChevronDownIcon data-icon="inline-end" />
          </Button>
        {/snippet}
      </Popover.Trigger>
      <Popover.Content class="w-auto overflow-hidden p-0" align="start">
        <Calendar
          type="single"
          bind:value
          captionLayout="dropdown"
          onValueChange={() => {
            open = false;
          }}
        />
      </Popover.Content>
    </Popover.Root>
  </Field.Field>
  <Field.Field class="w-32">
    <Field.Label for="time-picker-optional">Time</Field.Label>
    <Input
      type="time"
      id="time-picker-optional"
      step="1"
      value="10:30:00"
      class="appearance-none bg-background [&::-webkit-calendar-picker-indicator]:hidden [&::-webkit-calendar-picker-indicator]:appearance-none"
    />
  </Field.Field>
</Field.Group>
```

View Code

## [Natural Language Picker](#natural-language-picker)

This component uses the `chrono-node` library to parse natural language dates.

```svelte
<script lang="ts">
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import {
    CalendarDate,
    getLocalTimeZone,
    type DateValue
  } from "@internationalized/date";
  import { parseDate } from "chrono-node";
  import { untrack } from "svelte";
  import * as Field from "$lib/components/ui/field/index.js";
  import * as InputGroup from "$lib/components/ui/input-group/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  function formatDate(date: DateValue | undefined) {
    if (!date) return "";
    return date.toDate(getLocalTimeZone()).toLocaleDateString("en-US", {
      day: "2-digit",
      month: "long",
      year: "numeric"
    });
  }
  function toCalendarDate(date: Date) {
    return new CalendarDate(
      date.getFullYear(),
      date.getMonth() + 1,
      date.getDate()
    );
  }
  let open = $state(false);
  let inputValue = $state("In 2 days");
  let value = $state<DateValue | undefined>(
    untrack(() => {
      const date = parseDate(inputValue);
      return date ? toCalendarDate(date) : undefined;
    })
  );
</script>
<Field.Field class="mx-auto max-w-xs">
  <Field.Label for="date-optional">Schedule Date</Field.Label>
  <InputGroup.Root>
    <InputGroup.Input
      id="date-optional"
      placeholder="Tomorrow or next week"
      bind:value={
        () => inputValue,
        (v) => {
          inputValue = v;
          const date = parseDate(v);
          if (date) {
            value = toCalendarDate(date);
          }
        }
      }
      onkeydown={(e) => {
        if (e.key === "ArrowDown") {
          e.preventDefault();
          open = true;
        }
      }}
    />
    <InputGroup.Addon align="inline-end">
      <Popover.Root bind:open>
        <Popover.Trigger id="date-picker">
          {#snippet child({ props })}
            <InputGroup.Button
              {...props}
              variant="ghost"
              size="icon-xs"
              aria-label="Select date"
            >
              <CalendarIcon />
              <span class="sr-only">Select date</span>
            </InputGroup.Button>
          {/snippet}
        </Popover.Trigger>
        <Popover.Content
          class="w-auto overflow-hidden p-0"
          align="end"
          sideOffset={8}
        >
          <Calendar
            type="single"
            bind:value
            captionLayout="dropdown"
            onValueChange={(v) => {
              inputValue = formatDate(v);
              open = false;
            }}
          />
        </Popover.Content>
      </Popover.Root>
    </InputGroup.Addon>
  </InputGroup.Root>
  <div class="px-1 text-sm text-muted-foreground">
    Your post will be published on
    <span class="font-medium">{formatDate(value)}</span>.
  </div>
</Field.Field>
```

View Code