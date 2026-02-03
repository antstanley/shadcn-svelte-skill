# Date Picker

A date picker component with range and presets.

```svelte
<script lang="ts">
  import Calendar from "$lib/components/ui/calendar/calendar.svelte";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import {
    getLocalTimeZone,
    today,
    type CalendarDate
  } from "@internationalized/date";
  const id = $props.id();
  let open = $state(false);
  let value = $state<CalendarDate | undefined>();
</script>
<div class="flex flex-col gap-3">
  <Label for="{id}-date" class="px-1">Date of birth</Label>
  <Popover.Root bind:open>
    <Popover.Trigger id="{id}-date">
      {#snippet child({ props })}
        <Button
          {...props}
          variant="outline"
          class="w-48 justify-between font-normal"
        >
          {value
            ? value.toDate(getLocalTimeZone()).toLocaleDateString()
            : "Select date"}
          <ChevronDownIcon />
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
        maxValue={today(getLocalTimeZone())}
      />
    </Popover.Content>
  </Popover.Root>
</div>
```

## Installation

The Date Picker is built using a composition of the `<Popover />` and either the `<Calendar />` or `<RangeCalendar />` components.

See installations instructions for the [Popover](https://shadcn-svelte.com/docs/components/popover#installation), [Calendar](https://shadcn-svelte.com/docs/components/calendar#installation), and [Range Calendar](https://shadcn-svelte.com/docs/components/range-calendar#installation) components.

## Usage

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

## Examples

### Date of Birth Picker

```svelte
<script lang="ts">
  import Calendar from "$lib/components/ui/calendar/calendar.svelte";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import {
    getLocalTimeZone,
    today,
    type CalendarDate
  } from "@internationalized/date";
  const id = $props.id();
  let open = $state(false);
  let value = $state<CalendarDate | undefined>();
</script>
<div class="flex flex-col gap-3">
  <Label for="{id}-date" class="px-1">Date of birth</Label>
  <Popover.Root bind:open>
    <Popover.Trigger id="{id}-date">
      {#snippet child({ props })}
        <Button
          {...props}
          variant="outline"
          class="w-48 justify-between font-normal"
        >
          {value
            ? value.toDate(getLocalTimeZone()).toLocaleDateString()
            : "Select date"}
          <ChevronDownIcon />
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
        maxValue={today(getLocalTimeZone())}
      />
    </Popover.Content>
  </Popover.Root>
</div>
```

### Picker with Input

### Date and Time Picker

```svelte
<script lang="ts">
  import Calendar from "$lib/components/ui/calendar/calendar.svelte";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Label } from "$lib/components/ui/label/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import ChevronDownIcon from "@lucide/svelte/icons/chevron-down";
  import { getLocalTimeZone } from "@internationalized/date";
  import type { CalendarDate } from "@internationalized/date";
  const id = $props.id();
  let open = $state(false);
  let value = $state<CalendarDate | undefined>();
</script>
<div class="flex gap-4">
  <div class="flex flex-col gap-3">
    <Label for="{id}-date" class="px-1">Date</Label>
    <Popover.Root bind:open>
      <Popover.Trigger id="{id}-date">
        {#snippet child({ props })}
          <Button
            {...props}
            variant="outline"
            class="w-32 justify-between font-normal"
          >
            {value
              ? value.toDate(getLocalTimeZone()).toLocaleDateString()
              : "Select date"}
            <ChevronDownIcon />
          </Button>
        {/snippet}
      </Popover.Trigger>
      <Popover.Content class="w-auto overflow-hidden p-0" align="start">
        <Calendar
          type="single"
          bind:value
          onValueChange={() => {
            open = false;
          }}
          captionLayout="dropdown"
        />
      </Popover.Content>
    </Popover.Root>
  </div>
  <div class="flex flex-col gap-3">
    <Label for="{id}-time" class="px-1">Time</Label>
    <Input
      type="time"
      id="{id}-time"
      step="1"
      value="10:30:00"
      class="bg-background appearance-none [&::-webkit-calendar-picker-indicator]:hidden [&::-webkit-calendar-picker-indicator]:appearance-none"
    />
  </div>
</div>
```

### Natural Language Picker

This component uses the `chrono-node` library to parse natural language dates.

```svelte
<script lang="ts">
  import { Label } from "$lib/components/ui/label/index.js";
  import * as Popover from "$lib/components/ui/popover/index.js";
  import { Button } from "$lib/components/ui/button/index.js";
  import { Calendar } from "$lib/components/ui/calendar/index.js";
  import { Input } from "$lib/components/ui/input/index.js";
  import CalendarIcon from "@lucide/svelte/icons/calendar";
  import { parseDate } from "chrono-node";
  import {
    CalendarDate,
    getLocalTimeZone,
    type DateValue
  } from "@internationalized/date";
  import { untrack } from "svelte";
  function formatDate(date: DateValue | undefined) {
    if (!date) return "";
    return date.toDate(getLocalTimeZone()).toLocaleDateString("en-US", {
      day: "2-digit",
      month: "long",
      year: "numeric"
    });
  }
  const id = $props.id();
  let open = $state(false);
  let inputValue = $state("In 2 days");
  let value = $state<DateValue | undefined>(
    untrack(() => {
      const date = parseDate(inputValue);
      if (date)
        return new CalendarDate(
          date.getFullYear(),
          date.getMonth() + 1,
          date.getDate()
        );
      return undefined;
    })
  );
</script>
<div class="flex flex-col gap-3">
  <Label for="{id}-date" class="px-1">Schedule Date</Label>
  <div class="relative flex gap-2">
    <Input
      id="date"
      bind:value={
        () => inputValue,
        (v) => {
          inputValue = v;
          const date = parseDate(v);
          if (date) {
            value = new CalendarDate(
              date.getFullYear(),
              date.getMonth() + 1,
              date.getDate()
            );
          }
        }
      }
      placeholder="Tomorrow or next week"
      class="bg-background pe-10"
      onkeydown={(e) => {
        if (e.key === "ArrowDown") {
          e.preventDefault();
          open = true;
        }
      }}
    />
    <Popover.Root bind:open>
      <Popover.Trigger id="{id}-date-picker">
        {#snippet child({ props })}
          <Button
            {...props}
            variant="ghost"
            class="absolute end-2 top-1/2 size-6 -translate-y-1/2"
          >
            <CalendarIcon class="size-3.5" />
            <span class="sr-only">Select date</span>
          </Button>
        {/snippet}
      </Popover.Trigger>
      <Popover.Content class="w-auto overflow-hidden p-0" align="end">
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
  </div>
  <div class="text-muted-foreground px-1 text-sm">
    Your post will be published on
    <span class="font-medium">{formatDate(value)}</span>.
  </div>
</div>
```