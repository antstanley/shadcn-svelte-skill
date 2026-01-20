# Chart

Beautiful charts. Built using LayerChart. Copy and paste into your apps.

## About

Charts are built using [LayerChart v2](https://layerchart.com) (pre-release). You build your charts using LayerChart components and only bring in custom components like `ChartTooltip` when needed.

> **Note:** LayerChart v2 is still in pre-release and is actively evolving. Only use if you're comfortable with potential breaking changes before stable v2.

## Installation

```bash
pnpm dlx shadcn-svelte@latest add chart
```

```bash
npx shadcn-svelte@latest add chart
```

```bash
bun x shadcn-svelte@latest add chart
```

## Configuration

Charts use a config object that holds labels, icons, and colors:

```ts
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "var(--chart-1)",
  },
  mobile: {
    label: "Mobile",
    color: "var(--chart-2)",
  },
};
```

## Theming

### CSS Variables (Recommended)

```css
:root {
  --chart-1: oklch(0.646 0.222 41.116);
  --chart-2: oklch(0.6 0.118 184.704);
  --chart-3: oklch(0.398 0.07 227.392);
  --chart-4: oklch(0.828 0.189 84.429);
  --chart-5: oklch(0.769 0.188 70.08);
}
```

### Direct Values

```ts
const chartConfig = {
  desktop: {
    label: "Desktop",
    color: "#2563eb",
  },
};
```

### Theme Object

```ts
const chartConfig = {
  desktop: {
    label: "Desktop",
    theme: {
      light: "#2563eb",
      dark: "#dc2626",
    },
  },
};
```

## Tooltip

The `Chart.Tooltip` component provides configurable tooltips:

```svelte
<Chart.Tooltip>
  <Chart.TooltipContent
    hideLabel={false}
    hideIndicator={false}
    indicator="dot"
  />
</Chart.Tooltip>
```

### Indicator Options

- `dot` - Circle indicator
- `line` - Line indicator
- `dashed` - Dashed line indicator

## Usage Pattern

```svelte
<script lang="ts">
  import { BarChart } from "layerchart";
  import * as Chart from "$lib/components/ui/chart/index.js";

  const data = [...];
  const chartConfig = {...};
</script>

<Chart.Root config={chartConfig}>
  <BarChart {data} x="month" y="value">
    <!-- LayerChart components -->
  </BarChart>
  <Chart.Tooltip>
    <Chart.TooltipContent />
  </Chart.Tooltip>
</Chart.Root>
```

Colors are automatically referenced from the chart config.
