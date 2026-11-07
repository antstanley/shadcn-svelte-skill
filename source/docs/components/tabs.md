# Tabs

A set of layered sections of contentknown as tab panelsthat are displayed one at a time.

[Docs](https://bits-ui.com/docs/components/tabs)

[API Reference](https://bits-ui.com/docs/components/tabs#api-reference)

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

```svelte
<script lang="ts">
 import * as Card from "$lib/components/ui/card/index.js";
 import * as Tabs from "$lib/components/ui/tabs/index.js";
 const tabs = [
  {
   value: "overview",
   title: "Overview",
   description:
    "View your key metrics and recent project activity. Track progress across all your active projects.",
   content: "You have 12 active projects and 3 pending tasks.",
  },
  {
   value: "analytics",
   title: "Analytics",
   description:
    "Track performance and user engagement metrics. Monitor trends and identify growth opportunities.",
   content: "Page views are up 25% compared to last month.",
  },
  {
   value: "reports",
   title: "Reports",
   description:
    "Generate and download your detailed reports. Export data in multiple formats for analysis.",
   content: "You have 5 reports ready and available to export.",
  },
  {
   value: "settings",
   title: "Settings",
   description:
    "Manage your account preferences and options. Customize your experience to fit your needs.",
   content: "Configure notifications, security, and themes.",
  },
];
</script>
<Tabs.Root value="overview" class="w-[400px]">
 <Tabs.List>
  {#each tabs as tab (tab.value)}
   <Tabs.Trigger value={tab.value}>{tab.title}</Tabs.Trigger>
  {/each}
 </Tabs.List>
 {#each tabs as tab (tab.value)}
  <Tabs.Content value={tab.value}>
   <Card.Root>
    <Card.Header>
     <Card.Title>{tab.title}</Card.Title>
     <Card.Description>{tab.description}</Card.Description>
    </Card.Header>
    <Card.Content class="text-sm text-muted-foreground">{tab.content}</Card.Content>
   </Card.Root>
  </Tabs.Content>
 {/each}
</Tabs.Root>
```

View Code

## [Installation](#installation)

```bash
pnpm dlx shadcn-svelte@latest add tabs
```

```bash
npx shadcn-svelte@latest add tabs
```

```bash
bun x shadcn-svelte@latest add tabs
```

## [Usage](#usage)

```svelte
<script lang="ts">
  import * as Tabs from "$lib/components/ui/tabs/index.js";
</script>
```

```svelte
<Tabs.Root value="account" class="w-[400px]">
  <Tabs.List>
    <Tabs.Trigger value="account">Account</Tabs.Trigger>
    <Tabs.Trigger value="password">Password</Tabs.Trigger>
  </Tabs.List>
  <Tabs.Content value="account">
    Make changes to your account here.
  </Tabs.Content>
  <Tabs.Content value="password">Change your password here.</Tabs.Content>
</Tabs.Root>
```

## [Line](#line)

Use the `variant="line"` prop on `Tabs.List` for a line style.

```svelte
<script lang="ts">
 import * as Tabs from "$lib/components/ui/tabs/index.js";
</script>
<Tabs.Root value="overview">
 <Tabs.List variant="line">
  <Tabs.Trigger value="overview">Overview</Tabs.Trigger>
  <Tabs.Trigger value="analytics">Analytics</Tabs.Trigger>
  <Tabs.Trigger value="reports">Reports</Tabs.Trigger>
 </Tabs.List>
</Tabs.Root>
```

View Code

## [Vertical](#vertical)

Use `orientation="vertical"` for vertical tabs.

```svelte
<script lang="ts">
 import * as Tabs from "$lib/components/ui/tabs/index.js";
</script>
<Tabs.Root value="account" orientation="vertical">
 <Tabs.List>
  <Tabs.Trigger value="account">Account</Tabs.Trigger>
  <Tabs.Trigger value="password">Password</Tabs.Trigger>
  <Tabs.Trigger value="notifications">Notifications</Tabs.Trigger>
 </Tabs.List>
</Tabs.Root>
```

View Code

## [Disabled](#disabled)

```svelte
<script lang="ts">
 import * as Tabs from "$lib/components/ui/tabs/index.js";
</script>
<Tabs.Root value="home">
 <Tabs.List>
  <Tabs.Trigger value="home">Home</Tabs.Trigger>
  <Tabs.Trigger value="settings" disabled>Disabled</Tabs.Trigger>
 </Tabs.List>
</Tabs.Root>
```

View Code

## [Icons](#icons)

```svelte
<script lang="ts">
 import AppWindowIcon from "@lucide/svelte/icons/app-window";
 import CodeIcon from "@lucide/svelte/icons/code";
 import * as Tabs from "$lib/components/ui/tabs/index.js";
</script>
<Tabs.Root value="preview">
 <Tabs.List>
  <Tabs.Trigger value="preview">
   <AppWindowIcon />
   Preview
  </Tabs.Trigger>
  <Tabs.Trigger value="code">
   <CodeIcon />
   Code
  </Tabs.Trigger>
 </Tabs.List>
</Tabs.Root>
```

View Code