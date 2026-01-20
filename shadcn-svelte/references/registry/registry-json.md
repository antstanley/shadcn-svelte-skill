# registry.json

Schema reference for the registry.json file.

## Overview

The `registry.json` file defines your custom component registry metadata and configuration.

## Schema

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry.json",
  "name": "my-registry",
  "homepage": "https://my-registry.com",
  "items": []
}
```

## Properties

### $schema

Points to the schema definition:

```json
{
  "$schema": "https://shadcn-svelte.com/schema/registry.json"
}
```

### name

Identifies your registry for metadata and data attributes:

```json
{
  "name": "my-registry"
}
```

### homepage

References your registry's web location:

```json
{
  "homepage": "https://my-registry.com"
}
```

### items

Contains registry entries following the registry-item specification:

```json
{
  "items": [
    {
      "name": "hello-world",
      "type": "registry:block",
      "title": "Hello World",
      "description": "A hello world component",
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

### aliases

Maps internal import paths to transformation targets:

```json
{
  "aliases": {
    "lib": "$lib/registry/lib",
    "ui": "$lib/registry/ui",
    "components": "$lib/registry/components",
    "utils": "$lib/utils",
    "hooks": "$lib/registry/hooks"
  }
}
```

Custom aliases should mirror your actual import structure.

### overrideDependencies

Force specific dependency versions:

```json
{
  "overrideDependencies": {
    "bits-ui": "1.0.0-next.50"
  }
}
```

**Warning:** This can lead to version conflicts if not carefully managed. Use sparingly.
