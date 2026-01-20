#!/usr/bin/env python3
"""Download shadcn-svelte documentation from llms.txt."""

import re
import sys
import urllib.request
from pathlib import Path
from urllib.parse import urlparse

LLMS_TXT_URL = "https://www.shadcn-svelte.com/llms.txt"
BASE_URL = "https://www.shadcn-svelte.com"


def download_file(url: str) -> str | None:
    """Download a file and return its content."""
    try:
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "Mozilla/5.0 (compatible; shadcn-svelte-skill/1.0)"},
        )
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.read().decode("utf-8")
    except Exception as e:
        print(f"  ❌ Failed to download {url}: {e}")
        return None


def extract_urls(content: str) -> list[str]:
    """Extract all URLs from llms.txt content."""
    # Match URLs that end in .md
    url_pattern = r"https?://[^\s\)>\]]+\.md"
    urls = re.findall(url_pattern, content)
    return sorted(set(urls))


def url_to_filepath(url: str, output_dir: Path) -> Path:
    """Convert a URL to a local file path."""
    parsed = urlparse(url)
    # Remove /docs/ prefix and .md suffix to get the path
    path = parsed.path
    if path.startswith("/docs/"):
        path = path[6:]  # Remove /docs/

    # Handle the file path
    if path.endswith(".md"):
        filepath = output_dir / path
    else:
        filepath = output_dir / f"{path}.md"

    return filepath


def download_docs(output_dir: Path) -> int:
    """Download all documentation files."""
    print(f"📥 Downloading llms.txt from {LLMS_TXT_URL}")

    content = download_file(LLMS_TXT_URL)
    if not content:
        print("❌ Failed to download llms.txt")
        return 1

    urls = extract_urls(content)
    print(f"📋 Found {len(urls)} .md files to download\n")

    # Clear existing references (except keeping directory structure)
    if output_dir.exists():
        for md_file in output_dir.rglob("*.md"):
            md_file.unlink()

    success_count = 0
    fail_count = 0

    for url in urls:
        filepath = url_to_filepath(url, output_dir)

        # Create parent directories
        filepath.parent.mkdir(parents=True, exist_ok=True)

        print(f"  Downloading: {filepath.relative_to(output_dir)}")

        content = download_file(url)
        if content:
            filepath.write_text(content)
            success_count += 1
        else:
            fail_count += 1

    print()
    print(f"✅ Downloaded {success_count} files")
    if fail_count:
        print(f"❌ Failed to download {fail_count} files")

    return 0 if fail_count == 0 else 1


def main() -> int:
    # Determine output directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    output_dir = repo_root / "source" / "docs"

    # Allow override via command line
    if len(sys.argv) > 1:
        output_dir = Path(sys.argv[1])

    print(f"📁 Output directory: {output_dir}\n")

    return download_docs(output_dir)


if __name__ == "__main__":
    sys.exit(main())
