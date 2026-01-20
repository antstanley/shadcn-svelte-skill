# Getting Started

How to create and publish a custom component registry.

## Overview

Create a custom component registry to distribute your components, blocks, and themes.

## Setup

### 1. Create registry.json

Create a `registry.json` file at your project root:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry.json",
  "name": "my-registry",
  "homepage": "https://my-registry.com",
  "items": []
}
```

### 2. Organize Components

Store components in a structured directory:

```
registry/
├── hello-world/
│   ├── hello-world.svelte
│   └── index.ts
├── my-button/
│   ├── my-button.svelte
│   └── index.ts
```

You can place components anywhere in your project as long as you set the correct path in the `registry.json` file.

### 3. Define Registry Entry

Add component metadata to `registry.json`:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry.json",
  "name": "my-registry",
  "homepage": "https://my-registry.com",
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A simple hello world component",
      "files": [
        {
          "path": "registry/hello-world/hello-world.svelte",
          "type": "registry:component"
        }
      ]
    }
  ]
}
```

## Build and Deploy

### Install CLI

```bash
pnpm add -D shadcn-svelte
```

### Add Build Script

```json
{
  "scripts": {
    "build:registry": "shadcn-svelte build"
  }
}
```

### Run Build

```bash
pnpm build:registry
```

This generates JSON files in `static/r/` by default.

### Development

Registry items are accessible at:

```
http://localhost:5173/r/[component-name].json
```

### Production

Deploy to a public URL to share your registry. Users can install:

```bash
pnpm dlx shadcn-svelte@latest add https://my-registry.com/r/hello-world.json
```

## Security

Authentication isn't built-in. For private registries:

- Implement token-based validation
- Use query parameters: `?token=[SECURE_TOKEN]`
- Encrypt and expire all tokens
