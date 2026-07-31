# Calendar

A calendar component that allows users to select dates.

[Docs](https://bits-ui.com/docs/components/calendar)

[API Reference](https://bits-ui.com/docs/components/calendar#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

View Code

## [Blocks](#blocks)

We have built a collection of 30+ calendar blocks that you can use to build your own calendar components.

See call calendar blocks in the [Blocks Library](https://shadcn-svelte.com/blocks/calendar) page.

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

## [About](#about)

The `<Calendar />` component is built on top of the [Bits UI Calendar](https://www.bits-ui.com/docs/components/calendar) component, which uses the [@internationalized/date](https://react-spectrum.adobe.com/internationalized/date/index.html) package to handle dates.

If you're looking for a range calendar, check out the [Range Calendar](https://shadcn-svelte.com/docs/components/range-calendar) component.

## [Date Picker](#date-picker)

You can use the `<Calendar />` component to build a date picker. See the [Date Picker](https://shadcn-svelte.com/docs/components/date-picker) page for more information.

## [Examples](#examples)

### [Range Calendar](#range-calendar)

View Code

### [Month and Year Selector](#month-and-year-selector)

View Code

### [Date of Birth Picker](#date-of-birth-picker)

View Code

### [Date and Time Picker](#date-and-time-picker)

View Code

### [Natural Language Picker](#natural-language-picker)

This component uses the `chrono-node` library to parse natural language dates.

View Code

## [Upgrade Guide](#upgrade-guide)

You can upgrade to the latest version of the `<Calendar />` component by running the following command:

```bash
pnpm dlx shadcn-svelte@latest add calendar
```

```bash
npx shadcn-svelte@latest add calendar
```

```bash
bun x shadcn-svelte@latest add calendar
```

When you're prompted to overwrite the existing files, select `Yes`. **If you have made any changes to the `Calendar` component, you will need to merge your changes with the new version.**

#### [Installing Blocks](#installing-blocks)

After upgrading the `Calendar` component, you can add the new blocks with the following:

```bash
pnpm dlx shadcn-svelte@latest add calendar-02
```

```bash
npx shadcn-svelte@latest add calendar-02
```

```bash
bun x shadcn-svelte@latest add calendar-02
```

This will add the latest version of the calendar blocks.