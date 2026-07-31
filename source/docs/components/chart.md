# Chart

Beautiful charts. Built using LayerChart. Copy and paste into your apps.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

**Important:** LayerChart v2 is still in pre-release and is actively evolving. Only use if you're comfortable with potential breaking changes before stable v2.

Your feedback will be invaluable in shaping the release and features. Current development status can be tracked [here](https://github.com/techniq/layerchart/pull/449).

Introducing **Charts**. A collection of chart components that you can copy and paste into your apps.

Charts are designed to look great out of the box. They work well with other components are are fully customizable to fit your project.

[Browse the Charts Library](https://shadcn-svelte.com/charts)

## [Component](#component)

We use [LayerChart](https://next.layerchart.com) under the hood.

We designed the `Chart` component with composition in mind. **You build your charts using LayerChart components and only bring in custom components, such as `ChartTooltip`, when and where you need it**

```svelte
<script lang="ts">
  import * as Chart from "$lib/components/ui/chart/index.js";
  import { BarChart } from "layerchart";
  const data = [
    // ...
 ];
</script>
<Chart.Container>
  <BarChart {data} x="date" y="value">
    {#snippet tooltip()}
      <Chart.Tooltip />
    {/snippet}
  </BarChart>
</Chart.Container>
```

We do not wrap LayerChart. This means you're not locked into an abstraction. When a new LayerChart version is released, you can follow the official upgrade path to upgrade your charts.

**The components are yours**.

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add chart
```

```bash
npx shadcn-svelte@latest add chart
```

```bash
bun x shadcn-svelte@latest add chart
```

## [Your First Chart](#your-first-chart)

Let's build your first chart. We'll build a bar chart with an axis, grid, tooltip, and legend.

### [Start by defining your data](#start-by-defining-your-data)

The following data represents the number of desktop and mobile users for each month.

**Note:** Your data can be in any shape. You are not limited to the shape of the data below. Use the `dataKey` prop to map your data to the chart.

lib/components/example-chart.svelte

```svelte
<script lang="ts">
  const chartData = [
    { month: "January", desktop: 186, mobile: 80 },
    { month: "February", desktop: 305, mobile: 200 },
    { month: "March", desktop: 237, mobile: 120 },
    { month: "April", desktop: 73, mobile: 190 },
    { month: "May", desktop: 209, mobile: 130 },
    { month: "June", desktop: 214, mobile: 140 },
 ];
</script>
```

### [Define your chart config](#define-your-chart-config)

The chart config holds configuration for the chart. This is where you place human-readable strings, such as labels, icons, and color tokens for theming.

lib/components/example-chart.svelte

```svelte
<script lang="ts">
  import * as Chart from "$lib/components/ui/chart/index.js";
  const chartConfig = {
    desktop: {
      label: "Desktop",
      color: "#2563eb",
    },
    mobile: {
      label: "Mobile",
      color: "#60a5fa",
    },
  } satisfies Chart.ChartConfig;
</script>
```

### [Build your chart](#build-your-chart)

You can now build your chart using LayerChart components. We're using the `BarChart` component in this example, which is one of LayerChart's "Simplified Charts".

These components handle a lot of the common chart scaffolding for you, while allowing you to customize them to your liking.

View Code

We now have a group-stacked bar chart with an x axis and a grid.

### [Adjusting the Axis Ticks](#adjusting-the-axis-ticks)

Our bar chart is currently displaying the full month name for each tick on the x axis. Let's shorten it to just the first three letters.

### [Add a custom formatter to the x axis](#add-a-custom-formatter-to-the-x-axis)

The `props` prop is how you can pass custom props to the various components that make up the chart. Here we're passing a custom formatter to the x axis.

```svelte
<Chart.Container config={chartConfig} class="min-h-[200px] w-full">
  <BarChart
    data={chartData}
    xScale={scaleBand().padding(0.25)}
    x="month"
    axis="x"
    tooltipContext={false}
    seriesLayout="group"
    series={[
      {
        key: "desktop",
        label: chartConfig.desktop.label,
        color: chartConfig.desktop.color,
      },
      {
        key: "mobile",
        label: chartConfig.mobile.label,
        color: chartConfig.mobile.color,
      },
   ]}
    props={{
      xAxis: {
        format: (d) => d.slice(0, 3),
      },
    }}
  />
</Chart.Container>
```

View Code

### [Add Tooltip](#add-tooltip)

So far we've only used the `BarChart` component from LayerChart. They look great out of the box thanks to some customizations in the `chart` component.

To add a tooltip, we'll use the custom `Chart.Tooltip` component from `chart`.

### [Add the `Chart.Tooltip` component to the chart](#add-the-charttooltip-component-to-the-chart)

We'll replace the `tooltipContext={false}` prop with the `tooltip` snippet where we'll place the `Chart.Tooltip` component.

```svelte
<Chart.Container config={chartConfig} class="min-h-[200px] w-full">
  <BarChart
    data={chartData}
    xScale={scaleBand().padding(0.25)}
    x="month"
    axis="x"
    seriesLayout="group"
    series={[
      {
        key: "desktop",
        label: chartConfig.desktop.label,
        color: chartConfig.desktop.color,
      },
      {
        key: "mobile",
        label: chartConfig.mobile.label,
        color: chartConfig.mobile.color,
      },
   ]}
    props={{
      xAxis: {
        format: (d) => d.slice(0, 3),
      },
    }}
  >
    {#snippet tooltip()}
      <Chart.Tooltip />
    {/snippet}
  </BarChart>
</Chart.Container>
```

View Code

### [Add Legend](#add-legend)

### [Set the `legend` prop to `true`](#set-the-legend-prop-to-true)

The `legend` prop is used to show a legend for the chart. We are working with LayerChart to add a payload similar to the tooltip so we can more easily create a custom legend.

```svelte
<Chart.Container config={chartConfig} class="min-h-[200px] w-full">
  <BarChart
    data={chartData}
    xScale={scaleBand().padding(0.25)}
    x="month"
    axis="x"
    seriesLayout="group"
    legend
    series={[
      {
        key: "desktop",
        label: chartConfig.desktop.label,
        color: chartConfig.desktop.color,
      },
      {
        key: "mobile",
        label: chartConfig.mobile.label,
        color: chartConfig.mobile.color,
      },
   ]}
    props={{
      xAxis: {
        format: (d) => d.slice(0, 3),
      },
    }}
  >
    {#snippet tooltip()}
      <Chart.Tooltip />
    {/snippet}
  </BarChart>
</Chart.Container>
```

View Code

Done. You've built your first chart! What's next?

- [Themes and Colors](https://shadcn-svelte.com/docs/components/chart#theming)  
- [Tooltip](https://shadcn-svelte.com/docs/components/chart#tooltip) ## [Chart Config](#chart-config)

The chart config is where you define the labels, icons and colors for a chart.

It is intentionally decoupled from chart data.

This allows you to share config and color tokens between charts. It can also works independently for cases where your data or color tokens live remotely or in a different format.

```svelte
<script lang="ts">
  import MonitorIcon from "@lucide/svelte/icons/monitor";
  import * as Chart from "$lib/components/ui/chart/index.js";
  const chartConfig = {
    desktop: {
      label: "Desktop",
      icon: MonitorIcon,
      // A color like 'hsl(220, 98%, 61%)' or 'var(--color-name)'
      color: "#2563eb",
      // OR a theme object with 'light' and 'dark' keys
      theme: {
        light: "#2563eb",
        dark: "#dc2626",
      },
    },
  } satisfies Chart.ChartConfig;
</script>
```

## [Theming](#theming)

Charts has built-in support for theming. You can use css variables (recommended) or color values in any color format, such as hex, hsl, or oklch.

### [CSS Variables](#css-variables)

### [Define your colors in your css file](#define-your-colors-in-your-css-file)

src/routes/layout.css

```css
:root {
  --background: oklch(1 0 0);
  --foreground: oklch(0.145 0 0);
  /* ... */
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
}
.dark {
  --background: oklch(0.145 0 0);
  --foreground: oklch(0.985 0 0);
  /* ... */
  --chart-1: oklch(0.488 0.243 264.376);
  --chart-2: oklch(0.696 0.17 162.48);
}
```

### [Add the color to your `chartConfig`](#add-the-color-to-your-chartconfig)

```svelte
<script lang="ts">
  const chartConfig = {
    desktop: {
      label: "Desktop",
      color: "var(--chart-1)",
    },
    mobile: {
      label: "Mobile",
      color: "var(--chart-2)",
    },
  } satisfies Chart.ChartConfig;
</script>
```

### [hex, hsl or oklch](#hex-hsl-or-oklch)

You can also define your colors directly in the chart config. Use the color format you prefer.

```svelte
<script lang="ts">
  const chartConfig = {
    desktop: {
      label: "Desktop",
      color: "#2563eb",
    },
  } satisfies Chart.ChartConfig;
</script>
```

### [Using Colors](#using-colors)

To use the theme colors in your chart, reference the colors using the format `var(--color-KEY)`.

#### [Components](#components)

```svelte
<Bar fill="var(--color-desktop)" />
```

#### [Chart Data](#chart-data)

```ts
const chartData = [
  { browser: "chrome", visitors: 275, color: "var(--color-chrome)" },
  { browser: "safari", visitors: 200, color: "var(--color-safari)" },];
```

#### [Tailwind](#tailwind)

```svelte
<Label class="fill-(--color-desktop)" />
```

## [Tooltip](#tooltip)

A chart tooltip contains a label, name, indicator and value. You can use a combination of these to customize your tooltip.

You can turn on/off any of these using the `hideLabel`, `hideIndicator` props and customize the indicator style using the `indicator` prop.

Use `labelKey` and `nameKey` to use a custom key for the tooltip label and name.

Chart comes with the `<Chart.Tooltip>` component. You can use this component to add custom tooltips to your chart.

### [Props](#props)

Use the following props to customize the tooltip.

| Prop                            | Type                                                        | Description                                                            |
| :------------------------------------------------------------ | :---------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------ |
| `labelKey`       | string                                                      | The config or data key to use for the label.                           |
| `nameKey`        | string                                                      | The config or data key to use for the name.                            |
| `indicator`      | `dot` `line` or `dashed` | The indicator style for the tooltip.                                   |
| `hideLabel`      | boolean                                                     | Whether to hide the label.                                             |
| `hideIndicator`  | boolean                                                     | Whether to hide the indicator.                                         |
| `label`          | string                                                      | A custom label for the tooltip                                         |
| `labelFormatter` | function                                                    | A function to format the label.                                        |
| `formatter`      | Snippet                                                     | A snippet to provide flexible rendering of the tooltip. |

### [Colors](#colors)

Colors are automatically referenced from the chart config.

### [Custom](#custom)

To use a custom key for tooltip label and names, use the `labelKey` and `nameKey` props.

```svelte
<script lang="ts">
  const chartData = [
    { browser: "chrome", visitors: 187, color: "var(--color-chrome)" },
    { browser: "safari", visitors: 200, color: "var(--color-safari)" },
 ];
  const chartConfig = {
    visitors: {
      label: "Total Visitors",
    },
    chrome: {
      label: "Chrome",
      color: "var(--chart-1)",
    },
    safari: {
      label: "Safari",
      color: "var(--chart-2)",
    },
  } satisfies ChartConfig;
</script>
<Chart.Tooltip labelKey="visitors" nameKey="browser" />
```

This will use `Total Visitors` for label and `Chrome` and `Safari` for the tooltip names.