import os
import re

def chunk_single_file_folder(folder_path):
    files = [f for f in os.listdir(folder_path) if f.endswith('.md') and f != 'README.md']
    if len(files) != 1 or files[0] != 'Section-01.md':
        return

    filepath = os.path.join(folder_path, files[0])
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        return

    frontmatter = parts[1]
    body = parts[2]

    # Remove title headings
    body = re.sub(r'#+\s+.*', '', body)

    # Split paragraphs
    paragraphs = [p.strip() for p in body.split('\n\n') if len(p.strip()) > 30]

    if len(paragraphs) <= 1:
        return

    # Extract ID prefix
    id_match = re.search(r'id:\s*([A-Z0-9]+)', frontmatter)
    prefix = id_match.group(1).split('-')[0] if id_match else "SEC"

    # Delete monolithic file
    os.remove(filepath)

    count = 0
    for idx, p in enumerate(paragraphs, 1):
        sec_padded = f"{idx:02d}"
        out_file = os.path.join(folder_path, f"Section-{sec_padded}.md")

        yaml = f"""---
canon: Nag-Hammadi
source_type: Gnostic-Codex
id: {prefix}-{sec_padded}
section: {idx}
---

{p}
"""
        with open(out_file, 'w', encoding='utf-8') as f:
            f.write(yaml)
        count += 1

    print(f"Chunked {folder_path} into {count} section notes!")

def chunk_all():
    target_roots = ["08-NagHammadi", "09-Pseudepigrapha"]
    for root_dir in target_roots:
        if not os.path.exists(root_dir): continue
        for item in os.listdir(root_dir):
            item_path = os.path.join(root_dir, item)
            if os.path.isdir(item_path):
                chunk_single_file_folder(item_path)

if __name__ == "__main__":
    chunk_all()
