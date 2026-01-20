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


def url_to_local_path(url: str) -> str:
    """Convert a URL to a local relative path."""
    parsed = urlparse(url)
    path = parsed.path
    if path.startswith("/docs/"):
        path = path[6:]  # Remove /docs/
    return f"docs/{path}"


def url_to_filepath(url: str, docs_dir: Path) -> Path:
    """Convert a URL to a local file path."""
    parsed = urlparse(url)
    path = parsed.path
    if path.startswith("/docs/"):
        path = path[6:]  # Remove /docs/

    if path.endswith(".md"):
        filepath = docs_dir / path
    else:
        filepath = docs_dir / f"{path}.md"

    return filepath


def update_llms_txt(content: str, urls: list[str]) -> str:
    """Update llms.txt content to use local file paths."""
    updated_content = content
    for url in urls:
        local_path = url_to_local_path(url)
        updated_content = updated_content.replace(url, local_path)
    return updated_content


def download_docs(source_dir: Path) -> int:
    """Download all documentation files and update llms.txt."""
    docs_dir = source_dir / "docs"

    print(f"📥 Downloading llms.txt from {LLMS_TXT_URL}")

    content = download_file(LLMS_TXT_URL)
    if not content:
        print("❌ Failed to download llms.txt")
        return 1

    urls = extract_urls(content)
    print(f"📋 Found {len(urls)} .md files to download\n")

    # Clear existing docs (except keeping directory structure)
    if docs_dir.exists():
        for md_file in docs_dir.rglob("*.md"):
            md_file.unlink()

    # Ensure directories exist
    source_dir.mkdir(parents=True, exist_ok=True)
    docs_dir.mkdir(parents=True, exist_ok=True)

    success_count = 0
    fail_count = 0

    for url in urls:
        filepath = url_to_filepath(url, docs_dir)

        # Create parent directories
        filepath.parent.mkdir(parents=True, exist_ok=True)

        print(f"  Downloading: {filepath.relative_to(docs_dir)}")

        file_content = download_file(url)
        if file_content:
            filepath.write_text(file_content)
            success_count += 1
        else:
            fail_count += 1

    # Update llms.txt with local paths and save
    print(f"\n📝 Updating llms.txt with local paths...")
    updated_llms = update_llms_txt(content, urls)
    llms_path = source_dir / "llms.txt"
    llms_path.write_text(updated_llms)
    print(f"  Saved: {llms_path}")

    print()
    print(f"✅ Downloaded {success_count} files")
    if fail_count:
        print(f"❌ Failed to download {fail_count} files")

    return 0 if fail_count == 0 else 1


def main() -> int:
    # Determine output directory
    script_dir = Path(__file__).parent
    repo_root = script_dir.parent
    source_dir = repo_root / "source"

    # Allow override via command line
    if len(sys.argv) > 1:
        source_dir = Path(sys.argv[1])

    print(f"📁 Source directory: {source_dir}\n")

    return download_docs(source_dir)


if __name__ == "__main__":
    sys.exit(main())
