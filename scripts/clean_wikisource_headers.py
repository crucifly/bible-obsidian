import os
import re

def clean_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        return

    frontmatter = parts[1]
    body = parts[2]

    body_no_titles = re.sub(r'^#+\s+.*', '', body, flags=re.MULTILINE)

    lines = body_no_titles.split('\n')
    start_idx = 0
    for idx, line in enumerate(lines):
        l = line.strip()
        if re.match(r'^(CHAPTER\s+[IVXLCDM\d]+|BOOK\s+[IVXLCDM\d]+|1\s+[A-Z]|1\.\s+[A-Z]|ספר|THE BOOK|THIS IS)', l, re.I):
            start_idx = idx
            break

    lines = lines[start_idx:]
    cleaned_lines = []

    for line in lines:
        l = line.strip()
        if not l:
            cleaned_lines.append("")
            continue

        if any(w == l for w in ["English", "Read", "Edit", "Tools", "Actions", "General", "Discussion", "Source", "Download", "Appearance", "Search"]):
            continue
        if any(w in l for w in ["Wikisource", "Main menu", "Display Options", "Print/export", "Add languages", "View history", "What links here", "Personal tools", "Jump to content", "Create account", "Donate", "Log in", "Special pages", "Random author", "Community portal", "Recent changes", "move to sidebar", "hide", "Add links", "Printable version"]):
            continue

        l_clean = re.sub(r'<link[^>]*>', '', l)
        l_clean = re.sub(r'<span class="wst-verse[^>]*><sup>(\d+)</sup></span>', r'\1 ', l_clean)
        l_clean = re.sub(r'</?span[^>]*>', '', l_clean)
        l_clean = re.sub(r'</?[a-z1-6]+[^>]*>', '', l_clean)
        l_clean = re.sub(r'\s+', ' ', l_clean).strip()

        if l_clean and len(l_clean) > 2 and not l_clean.startswith("}]"):
            cleaned_lines.append(l_clean)

    clean_body = "\n\n".join(cleaned_lines)
    clean_body = re.sub(r'\n{3,}', '\n\n', clean_body).strip()

    title_match = re.search(r'title:\s*"([^"]+)"', frontmatter)
    title = title_match.group(1) if title_match else ""

    new_content = f"---{frontmatter}---\n\n# {title}\n\n{clean_body}\n"

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def clean_all_directories():
    target_dirs = ["08-NagHammadi", "09-Pseudepigrapha"]
    count = 0
    for base in target_dirs:
        if not os.path.exists(base): continue
        for root, dirs, files in os.walk(base):
            for file in files:
                if file.endswith(".md") and file != "README.md":
                    fp = os.path.join(root, file)
                    clean_file(fp)
                    count += 1

    print(f"Purified text across {count} markdown files!")

if __name__ == "__main__":
    clean_all_directories()
