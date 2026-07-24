import urllib.request
import os
import re
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

def fetch_pistis_sophia():
    out_dir = "08-NagHammadi/PistisSophia"
    os.makedirs(out_dir, exist_ok=True)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    # ps005.htm is Chapter 1, ps148.htm is Chapter 148
    # We will loop through ps005 to ps148
    chap_count = 0
    for i in range(5, 149):
        url = f"http://gnosis.org/library/pistis-sophia/ps{i:03d}.htm"
        req = urllib.request.Request(url, headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue

        # Extract Chapter Number from TITLE or HTML body
        chap_match = re.search(r'CHAPTER\s+(\d+)', html_str, re.IGNORECASE)
        chap_num = chap_match.group(1) if chap_match else str(i - 4)

        # Extract main text between <HR></CENTER> and <HR>
        text = strip_tags(html_str)

        # Clean noise
        lines = [line.strip() for line in text.split('\n') if line.strip()]
        cleaned_lines = []
        skip = False
        for line in lines:
            if "The Gnostic Society Library" in line or "Return to" in line or "Next:" in line or "Previous" in line:
                continue
            cleaned_lines.append(line)

        clean_content = "\n\n".join(cleaned_lines)

        file_name = os.path.join(out_dir, f"Chapter-{chap_num}.md")
        yaml = f"""---
canon: Nag-Hammadi
source_type: Gnostic-Codex
id: PISTIS-{chap_num}
chapter: {chap_num}
title: "Pistis Sophia - Chapter {chap_num}"
translation: G.R.S. Mead
---

# Pistis Sophia - Chapter {chap_num}

{clean_content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)
        
        chap_count += 1
        if chap_count % 10 == 0:
            print(f"Ingested {chap_count} chapters of Pistis Sophia...")

    print(f"Completed Pistis Sophia ingestion: {chap_count} chapters generated.")

if __name__ == "__main__":
    fetch_pistis_sophia()
