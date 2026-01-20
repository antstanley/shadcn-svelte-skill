#!/usr/bin/env python3
"""Validate a skill's structure and SKILL.md frontmatter."""

import sys
import re
from pathlib import Path

import yaml


def validate_skill(skill_path: Path) -> bool:
    """Validate a skill directory."""
    errors = []

    # Check SKILL.md exists
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        errors.append("SKILL.md not found")
        print_errors(errors)
        return False

    # Read and parse SKILL.md
    content = skill_md.read_text()

    # Extract YAML frontmatter
    frontmatter_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not frontmatter_match:
        errors.append("SKILL.md missing YAML frontmatter (must start with ---)")
        print_errors(errors)
        return False

    try:
        frontmatter = yaml.safe_load(frontmatter_match.group(1))
    except yaml.YAMLError as e:
        errors.append(f"Invalid YAML frontmatter: {e}")
        print_errors(errors)
        return False

    # Check required fields
    if not frontmatter:
        errors.append("Frontmatter is empty")
    else:
        if "name" not in frontmatter:
            errors.append("Frontmatter missing 'name' field")
        elif not frontmatter["name"]:
            errors.append("Frontmatter 'name' field is empty")

        if "description" not in frontmatter:
            errors.append("Frontmatter missing 'description' field")
        elif not frontmatter["description"]:
            errors.append("Frontmatter 'description' field is empty")
        elif len(frontmatter["description"]) < 50:
            errors.append("Frontmatter 'description' should be at least 50 characters")

    # Check for TODO placeholders
    if "[TODO" in content:
        errors.append("SKILL.md contains unresolved [TODO] placeholders")

    if errors:
        print_errors(errors)
        return False

    print("✅ Skill is valid!")
    return True


def print_errors(errors: list[str]) -> None:
    """Print validation errors."""
    print("❌ Validation failed:")
    for error in errors:
        print(f"   - {error}")


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <skill-directory>")
        return 1

    skill_path = Path(sys.argv[1])
    if not skill_path.is_dir():
        print(f"Error: '{skill_path}' is not a directory")
        return 1

    return 0 if validate_skill(skill_path) else 1


if __name__ == "__main__":
    sys.exit(main())
