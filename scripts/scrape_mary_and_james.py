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

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

def parse_gospel_of_mary():
    url = "http://gnosis.org/library/marygosp.htm"
    req = urllib.request.Request(url, headers=headers)
    html_bytes = urllib.request.urlopen(req).read()
    html_str = html_bytes.decode('utf-8', errors='ignore')

    # Remove existing files in GospelOfMary directory
    out_dir = "08-NagHammadi/GospelOfMary"
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir):
            os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)

    # Chapters 4, 5, 8, 9
    chap_blocks = re.split(r'Chapter\s+(\d+):?', html_str, flags=re.IGNORECASE)
    
    # chap_blocks[0] is intro HTML, followed by chap_num, chap_content pairs
    for idx in range(1, len(chap_blocks), 2):
        chap_num = chap_blocks[idx]
        raw_content = chap_blocks[idx+1]

        # Stop if we hit footer navigation
        raw_content = raw_content.split("Archive Notes:")[0].split("The Gospel of Mary")[0]

        # Extract verses (numbers followed by right paren like 22) or lines)
        verses = re.findall(r'(\d+)\)\s*([\s\S]*?)(?=(?:\d+\)|Chapter|$))', raw_content)

        chap_dir = os.path.join(out_dir, f"Chapter-{chap_num}")
        os.makedirs(chap_dir, exist_ok=True)

        if verses:
            for v_num, v_text in verses:
                clean_v_text = strip_tags(v_text).strip()
                clean_v_text = re.sub(r'\s+', ' ', clean_v_text)
                if not clean_v_text: continue

                v_file = os.path.join(chap_dir, f"{chap_num}-{v_num}.md")
                yaml = f"""---
canon: Nag-Hammadi
source_type: Gnostic-Codex
id: MARY-{chap_num}-{v_num}
book: Gospel of Mary
chapter: {chap_num}
verse: {v_num}
---

{clean_v_text}
"""
                with open(v_file, 'w', encoding='utf-8') as f:
                    f.write(yaml)
        else:
            # Chapter summary fallback
            clean_chap = strip_tags(raw_content).strip()
            v_file = os.path.join(chap_dir, f"{chap_num}-1.md")
            yaml = f"""---
canon: Nag-Hammadi
source_type: Gnostic-Codex
id: MARY-{chap_num}-1
book: Gospel of Mary
chapter: {chap_num}
verse: 1
---

{clean_chap}
"""
            with open(v_file, 'w', encoding='utf-8') as f:
                f.write(yaml)

    print("Parsed Gospel of Mary into structured Chapters & Verses.")

def fetch_james_texts():
    texts = [
        {"url": "http://gnosis.org/naghamm/1ja.html", "dir": "08-NagHammadi/1stApocalypseOfJames", "id": "1APOCJAM", "title": "First Apocalypse of James"},
        {"url": "http://gnosis.org/naghamm/2ja.html", "dir": "08-NagHammadi/2ndApocalypseOfJames", "id": "2APOCJAM", "title": "Second Apocalypse of James"},
        {"url": "http://gnosis.org/naghamm/jam-meyer.html", "dir": "08-NagHammadi/ApocryphonOfJames", "id": "APOCJAM", "title": "Apocryphon of James"}
    ]

    for item in texts:
        os.makedirs(item["dir"], exist_ok=True)
        req = urllib.request.Request(item["url"], headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching {item['url']}: {e}")
            continue

        raw_text = strip_tags(html_str)
        # Clean header/footer boilerplate
        lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
        cleaned = [line for line in lines if "Gnostic Society Library" not in line and "Return to" not in line and "Archive" not in line]

        full_content = "\n\n".join(cleaned)

        file_name = os.path.join(item["dir"], "Section-1.md")
        yaml = f"""---
canon: Nag-Hammadi
source_type: Gnostic-Codex
id: {item['id']}-1
title: "{item['title']}"
---

# {item['title']}

{full_content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)
        print(f"Ingested {item['title']} to {item['dir']}")

if __name__ == "__main__":
    parse_gospel_of_mary()
    fetch_james_texts()
