#!/usr/bin/env python3
"""Package a skill directory into a distributable .skill file."""

import sys
import zipfile
from pathlib import Path

# Import validation from sibling module
from validate_skill import validate_skill


def package_skill(skill_path: Path, output_dir: Path) -> Path | None:
    """Package a skill into a .skill file (zip archive)."""

    # Validate first
    print(f"📦 Packaging skill: {skill_path}")
    print(f"   Output directory: {output_dir}")
    print()
    print("🔍 Validating skill...")

    if not validate_skill(skill_path):
        return None

    print()

    # Create output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Get skill name from directory
    skill_name = skill_path.name
    output_file = output_dir / f"{skill_name}.skill"

    # Create zip archive
    with zipfile.ZipFile(output_file, "w", zipfile.ZIP_DEFLATED) as zf:
        for file_path in sorted(skill_path.rglob("*")):
            if file_path.is_file():
                # Skip hidden files and common non-skill files
                if any(part.startswith(".") for part in file_path.parts):
                    continue
                if file_path.suffix in [".pyc", ".pyo"]:
                    continue
                if file_path.name in ["__pycache__", ".DS_Store", "Thumbs.db"]:
                    continue

                # Archive path preserves skill name as root
                archive_path = Path(skill_name) / file_path.relative_to(skill_path)
                zf.write(file_path, archive_path)
                print(f"  Added: {archive_path}")

    print()
    print(f"✅ Successfully packaged skill to: {output_file}")
    return output_file


def main() -> int:
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <skill-directory> [output-directory]")
        return 1

    skill_path = Path(sys.argv[1])
    if not skill_path.is_dir():
        print(f"Error: '{skill_path}' is not a directory")
        return 1

    output_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(".")

    result = package_skill(skill_path, output_dir)
    return 0 if result else 1


if __name__ == "__main__":
    sys.exit(main())
