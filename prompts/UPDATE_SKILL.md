# Update shadcn-svelte Skill

You are tasked with updating the shadcn-svelte Claude Code skill based on the latest documentation.

## Context

This repository contains a Claude Code skill for shadcn-svelte. The skill helps Claude assist users with the shadcn-svelte component library (a Svelte 5 port of shadcn/ui).

## Repository Structure

```
.
├── source/                    # Downloaded documentation (source of truth)
│   ├── llms.txt              # Index of all documentation with local paths
│   └── docs/                 # All .md documentation files
│       ├── about.md
│       ├── components/       # 54+ component docs
│       ├── installation/     # Setup guides
│       ├── dark-mode/        # Dark mode setup
│       ├── migration/        # Migration guides
│       └── registry/         # Custom registry docs
├── shadcn-svelte/            # The actual skill
│   ├── SKILL.md              # Main skill file (instructions + frontmatter)
│   └── references/           # Reference docs loaded on-demand
├── scripts/
│   ├── download_docs.py      # Downloads latest docs from shadcn-svelte.com
│   ├── validate_skill.py     # Validates skill structure
│   └── package_skill.py      # Packages skill into .skill file
```

## Skill Creator Guidelines

Follow the skill creation guidelines from the Anthropic skill-creator:
https://github.com/anthropics/skills/tree/main/skills/skill-creator

Key principles:
1. **Concise is Key** - Only add context Claude doesn't already have
2. **Progressive Disclosure** - Keep SKILL.md lean, use references/ for detailed docs
3. **Set Appropriate Degrees of Freedom** - Match specificity to task fragility

### SKILL.md Structure

The SKILL.md must have:
- **YAML Frontmatter** with `name` and `description` (description is the trigger mechanism)
- **Body** with essential instructions, patterns, and references to detailed docs

### References Organization

Place detailed documentation in `references/` organized by topic:
- Component docs go in `references/components/`
- Installation guides in `references/installation/`
- Keep only essential patterns in SKILL.md

## Your Task

1. **Review Source Documentation**
   - Read `source/llms.txt` for an overview of all available documentation
   - Check `source/docs/` for any new or updated content

2. **Compare with Current Skill**
   - Read `shadcn-svelte/SKILL.md` for current instructions
   - Check `shadcn-svelte/references/` for current reference docs

3. **Update the Skill**

   If source documentation has changed:

   a. **Update References**
      - Copy updated docs from `source/docs/` to `shadcn-svelte/references/`
      - Maintain the same directory structure
      - Remove any docs that no longer exist in source

   b. **Update SKILL.md** (if needed)
      - Update the description if new components or features were added
      - Update quick start examples if patterns changed
      - Update the reference documentation section if new categories added
      - Keep it concise - detailed info belongs in references/

4. **Validate the Skill**
   ```bash
   python scripts/validate_skill.py shadcn-svelte
   ```

5. **Test Packaging**
   ```bash
   python scripts/package_skill.py shadcn-svelte dist
   ```

## Example Updates

### New Component Added
If a new component (e.g., `stepper.md`) was added:
1. Copy `source/docs/components/stepper.md` → `shadcn-svelte/references/components/stepper.md`
2. No SKILL.md change needed (references are discovered automatically)

### Breaking API Change
If a component's API changed significantly:
1. Update the reference file in `shadcn-svelte/references/components/`
2. If it affects common patterns in SKILL.md, update those examples

### New Feature Category
If a new category was added (e.g., `animations/`):
1. Copy all files from `source/docs/animations/` → `shadcn-svelte/references/animations/`
2. Update SKILL.md's "Reference Documentation" section to list the new category

## Output

After completing the update:
1. Summarize what changed in the source documentation
2. List all files updated in the skill
3. Confirm validation passed
4. Note any manual review needed

## Important Notes

- Do NOT add README.md, CHANGELOG.md, or other auxiliary files to the skill
- Do NOT duplicate information between SKILL.md and references
- Keep SKILL.md under 500 lines
- The skill is for Claude, not humans - include only what helps Claude assist users
