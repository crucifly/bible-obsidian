import os
import re
import shutil

def fix_gospel_of_mary():
    mary_dir = "08-NagHammadi/GospelOfMary"
    if not os.path.exists(mary_dir):
        return

    # Add explanatory README about historical manuscript gaps
    readme_content = """# Gospel of Mary (Berlin Gnostic Codex 8502)

## Manuscript Integrity & Historical Gaps

The *Gospel of Mary* is preserved primarily in the 5th-century Coptic **Berlin Gnostic Codex (Papyrus Berolinensis 8502)**. 

### Why Chapters 1–3 and Verses 4:1–21 are Missing:
- **Pages 1 to 6** of the manuscript were lost in antiquity before its discovery in Akhmim, Egypt in 1896. These missing pages contained Chapters 1, 2, 3, and the first 21 verses of Chapter 4.
- The extant Coptic manuscript text begins abruptly on **page 7**, in the middle of a sentence at **Chapter 4, Verse 22**.
- **Pages 11 to 14** were also lost, creating a gap between the end of Chapter 5 and Chapter 8.

All scholarly translations (including Dr. Karen King and MacRae/Wilson) maintain this standard chapter and verse numbering scheme to preserve academic cross-referencing.
"""
    with open(os.path.join(mary_dir, "README.md"), 'w', encoding='utf-8') as f:
        f.write(readme_content)

    # Rename chapter folders and verse files to zero-padded format
    for item in os.listdir(mary_dir):
        item_path = os.path.join(mary_dir, item)
        if os.path.isdir(item_path) and item.startswith("Chapter-"):
            chap_num = item.replace("Chapter-", "")
            padded_chap_num = f"{int(chap_num):02d}"
            new_chap_dir = os.path.join(mary_dir, f"Chapter-{padded_chap_num}")
            
            if item_path != new_chap_dir:
                if os.path.exists(new_chap_dir):
                    shutil.rmtree(new_chap_dir)
                os.rename(item_path, new_chap_dir)
            
            # Now rename files inside
            for vf in os.listdir(new_chap_dir):
                if vf.endswith(".md"):
                    m = re.match(r'(\d+)-(\d+)\.md', vf)
                    if m:
                        c, v = m.groups()
                        padded_c = f"{int(c):02d}"
                        padded_v = f"{int(v):02d}"
                        new_vf_name = f"{padded_c}-{padded_v}.md"
                        old_vf_path = os.path.join(new_chap_dir, vf)
                        new_vf_path = os.path.join(new_chap_dir, new_vf_name)
                        if old_vf_path != new_vf_path:
                            os.rename(old_vf_path, new_vf_path)

    print("Fixed Gospel of Mary zero-padding and created README.md.")

def fix_section_zero_padding():
    base_dirs = ["08-NagHammadi", "09-Pseudepigrapha"]
    for base in base_dirs:
        if not os.path.exists(base): continue
        for book in os.listdir(base):
            book_dir = os.path.join(base, book)
            if not os.path.isdir(book_dir): continue
            
            for file in os.listdir(book_dir):
                if file.startswith("Section-") and file.endswith(".md"):
                    m = re.match(r'Section-(\d+)\.md', file)
                    if m:
                        num = int(m.group(1))
                        padded_num = f"{num:02d}"
                        new_file = f"Section-{padded_num}.md"
                        old_path = os.path.join(book_dir, file)
                        new_path = os.path.join(book_dir, new_file)
                        if old_path != new_path:
                            os.rename(old_path, new_path)

                elif file.startswith("Chapter-") and file.endswith(".md"):
                    m = re.match(r'Chapter-(\d+)\.md', file)
                    if m:
                        num = int(m.group(1))
                        padded_num = f"{num:02d}"
                        new_file = f"Chapter-{padded_num}.md"
                        old_path = os.path.join(book_dir, file)
                        new_path = os.path.join(book_dir, new_file)
                        if old_path != new_path:
                            os.rename(old_path, new_path)

    print("Fixed zero-padding across Section-XX.md and Chapter-XX.md files.")

if __name__ == "__main__":
    fix_gospel_of_mary()
    fix_section_zero_padding()
