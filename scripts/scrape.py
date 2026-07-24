import urllib.request
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

def scrape_text(url, output_dir, book_id, title, canon, source_type, translation):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html_bytes = urllib.request.urlopen(req).read()
        html_str = html_bytes.decode('utf-8', errors='ignore')
    except Exception as e:
        print(f"Error fetching {url}: {e}")
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
    parser.add_argument("--url", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--id", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--canon", default="Nag-Hammadi")
    parser.add_argument("--source_type", default="Gnostic-Codex")
    parser.add_argument("--translation", default="Unknown")
    
    args = parser.parse_args()
    scrape_text(args.url, args.out, args.id, args.title, args.canon, args.source_type, args.translation)
