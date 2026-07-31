# Astro

Adding dark mode to your Astro site.

### [Epicenter](https://github.com/EpicenterHQ/epicenter)

[Local-first, open source apps](https://github.com/EpicenterHQ/epicenter)

[Special Sponsor](https://github.com/EpicenterHQ/epicenter)

Just like in regular Svelte, we use the `class` strategy from Tailwind CSS to support dark mode toggling. See the [Tailwind CSS documentation](https://tailwindcss.com/docs/dark-mode#toggling-dark-mode-manually) for more information.

How you add the `dark` class to the `html` element is up to you. In this guide, we'll take a look at enabling dark mode toggling with [mode-watcher](https://github.com/svecosystem/mode-watcher).

## [Usage](#usage)

### [Create an inline theme script](#create-an-inline-theme-script)

This script will, in part, keep and track the dark mode value in `localStorage` and prevent [FUOC](https://en.wikipedia.org/wiki/Flash_of_unstyled_content).

src/pages/index.astro

```astro
---
import "../styles/global.css";
---
<script is:inline>
  const isBrowser = typeof localStorage !== 'undefined';
  const getThemePreference = () => {
    if (isBrowser && localStorage.getItem('theme')) {
      return localStorage.getItem('theme');
    }
    return window.matchMedia('(prefers-color-scheme: dark)').matches
      ? 'dark' : 'light';
  };
  const isDark = getThemePreference() === 'dark';
  document.documentElement.classList[isDark ? 'add' : 'remove']('dark');
  if (isBrowser) {
    const observer = new MutationObserver(() => {
      const isDark = document.documentElement.classList.contains('dark');
      localStorage.setItem('theme', isDark ? 'dark' : 'light');
    });
    observer.observe(document.documentElement, {
      attributes: true,
      attributeFilter: ['class']
    });
  }
</script>
<html lang="en">
 <body>
      <h1>Astro</h1>
 </body>
</html>
</script>
```

### [Install mode-watcher](#install-mode-watcher)

```bash
pnpm i mode-watcher@0.5.1
```

```bash
npm i mode-watcher@0.5.1
```

```bash
bun install mode-watcher@0.5.1
```

### [Add the ModeWatcher component](#add-the-modewatcher-component)

Import the `ModeWatcher` component and use it in your page with the `client:load` directive:

src/pages/index.astro

```astro
---
import "../styles/global.css";
import { ModeWatcher } from "mode-watcher";
---

<html lang="en">
 <body>
      <h1>Astro</h1>
      <ModeWatcher client:load />
 </body>
</html>
```

### [Create a mode toggle](#create-a-mode-toggle)

Create a mode toggle on your site to toggle between light and dark mode:

#### [Light switch](#light-switch)

View Code

#### [Dropdown menu](#dropdown-menu)

View Code

### [Add mode toggle to page](#add-mode-toggle-to-page)

Add the mode toggle to the page (also with the `client:load` directive):

src/pages/index.astro

```astro
---
import "../styles/global.css";
import { ModeWatcher } from "mode-watcher";
import ModeToggle from "$lib/components/mode-toggle.svelte";
---

<html lang="en">
 <body>
      <h1>Astro</h1>
      <ModeWatcher client:load />
      <ModeToggle client:load />
 </body>
</html>
```