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

def clean_and_pad_pistis_sophia():
    out_dir = "08-NagHammadi/PistisSophia"
    
    # Remove old unpadded files
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir):
            os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)
    
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }

    print("Re-fetching and cleaning all 144 chapters of Pistis Sophia with 3-digit zero-padding...")

    for i in range(5, 149):
        chap_num_raw = i - 4
        chap_num_str = f"{chap_num_raw:03d}" # 3-digit padding (001, 002, ..., 144)

        url = f"http://gnosis.org/library/pistis-sophia/ps{i:03d}.htm"
        req = urllib.request.Request(url, headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            continue

        raw_text = strip_tags(html_str)

        # 1. Strip page indicators like "p. 8", "p. 100", "p. 5"
        raw_text = re.sub(r'p\.\s*\d+', '', raw_text)
        # 2. Strip margin footnote numbers like "|2.", "|3."
        raw_text = re.sub(r'\|\s*\d+\.\s*', '', raw_text)

        # 3. Clean up navigation boilerplate
        lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
        cleaned_lines = []
        for line in lines:
            if "The Gnostic Society Library" in line or "Return to" in line or "Next:" in line or "Previous" in line or "Index" in line:
                continue
            if re.match(r'^Pistis Sophia:.*', line) or re.match(r'^translated by.*', line):
                continue
            cleaned_lines.append(line)

        # Re-join paragraphs cleanly
        content = "\n\n".join(cleaned_lines)
        content = re.sub(r'\n{3,}', '\n\n', content).strip()

        file_name = os.path.join(out_dir, f"Chapter-{chap_num_str}.md")
        yaml = f"""---
canon: Nag-Hammadi
source_type: Gnostic-Codex
id: PISTIS-{chap_num_str}
chapter: {chap_num_raw}
title: "Pistis Sophia - Chapter {chap_num_raw}"
translation: G.R.S. Mead
---

# Pistis Sophia - Chapter {chap_num_raw}

{content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)

    print("Completed Pistis Sophia cleaning and 3-digit zero-padding!")

if __name__ == "__main__":
    clean_and_pad_pistis_sophia()
