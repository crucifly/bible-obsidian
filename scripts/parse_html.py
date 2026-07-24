import sys
import os
import re
import argparse
from html.parser import HTMLParser

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs = True
        self.text = []
    def handle_data(self, d):
        self.text.append(d)
    def get_data(self):
        return ''.join(self.text)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def parse_html_file(file_path, output_dir, book_id, title, canon, source_type, translation):
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            html_str = f.read()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return
        
    text = strip_tags(html_str)
    
    # Clean up excessive newlines
    text = re.sub(r'\n{3,}', '\n\n', text).strip()
    
    os.makedirs(output_dir, exist_ok=True)
    
    filename = os.path.join(output_dir, f"{book_id}-1-1.md")
    
    frontmatter = f"""---
canon: {canon}
source_type: {source_type}
translation: {translation}
id: {book_id}
title: "{title}"
---

{text}
"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(frontmatter)
    
    print(f"Saved {title} to {filename}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--canon", default="Nag-Hammadi")
    parser.add_argument("--source_type", default="Gnostic-Codex")
    parser.add_argument("--translation", default="Unknown")
    
    args = parser.parse_args()
    parse_html_file(args.file, args.out, args.id, args.title, args.canon, args.source_type, args.translation)
