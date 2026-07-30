# Svelte

Adding dark mode to your Svelte site.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

## [Install mode-watcher](#install-mode-watcher)

Start by installing `mode-watcher`:

```bash
pnpm i mode-watcher
```

```bash
npm i mode-watcher
```

```bash
bun install mode-watcher
```

## [Add the ModeWatcher component](#add-the-modewatcher-component)

Import the `ModeWatcher` component and use it in your root layout:

src/routes/+layout.svelte

```svelte
<script lang="ts">
  import "../app.css";
  import { ModeWatcher } from "mode-watcher";
  let { children } = $props();
</script>
<ModeWatcher />
{@render children?.()}
```

## [Add a mode toggle](#add-a-mode-toggle)

Place a mode toggle on your site to toggle between light and dark mode.

View Code

View Code