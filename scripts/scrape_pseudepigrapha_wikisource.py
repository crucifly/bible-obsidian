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

# 1. Ingest All 91 Chapters of Book of Jasher from Wikisource
def fetch_jasher_wikisource():
    out_dir = "09-Pseudepigrapha/BookOfJasher"
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir): os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)

    print("Scraping all 91 chapters of Book of Jasher from Wikisource...")

    success = 0
    for ch in range(1, 92):
        ch_padded = f"{ch:02d}"
        url = f"https://en.wikisource.org/wiki/Book_of_Jasher/Chapter_{ch}"
        req = urllib.request.Request(url, headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching Jasher chapter {ch}: {e}")
            continue

        # Extract text inside main content body
        body_match = re.search(r'<div class="mw-parser-output">([\s\S]*?)</div>\s*<!--', html_str)
        raw_html = body_match.group(1) if body_match else html_str

        text = strip_tags(raw_html)
        lines = [l.strip() for l in text.split('\n') if l.strip()]
        cleaned = [l for l in lines if "Wikisource" not in l and "Jump to" not in l and "Navigation" not in l]

        content = "\n\n".join(cleaned)
        content = re.sub(r'\n{3,}', '\n\n', content).strip()

        file_name = os.path.join(out_dir, f"Chapter-{ch_padded}.md")
        yaml = f"""---
canon: Pseudepigrapha
source_type: Scripture
id: JASH-{ch_padded}
chapter: {ch}
title: "Book of Jasher - Chapter {ch}"
---

# Book of Jasher - Chapter {ch}

{content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)
        success += 1

    print(f"Completed Book of Jasher: {success} chapters generated!")

# 2. Ingest Testaments of Twelve Patriarchs from EarlyChristianWritings
def fetch_patriarchs():
    out_dir = "09-Pseudepigrapha/Testaments12Patriarchs"
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir): os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)

    url = "http://www.earlychristianwritings.com/text/patriarchs.html"
    req = urllib.request.Request(url, headers=headers)
    html_bytes = urllib.request.urlopen(req).read()
    html_str = html_bytes.decode('utf-8', errors='ignore')

    # Split by Patriarch testament headings
    parts = re.split(r'(THE TESTAMENT OF [A-Z]+)', html_str)
    
    pat_count = 0
    for idx in range(1, len(parts), 2):
        title = parts[idx].strip()
        raw_body = parts[idx+1]

        pat_name = title.replace("THE TESTAMENT OF ", "").title()
        pat_count += 1
        pat_padded = f"{pat_count:02d}"

        body_text = strip_tags(raw_body)
        lines = [l.strip() for l in body_text.split('\n') if l.strip()]
        cleaned = [l for l in lines if "Early Christian Writings" not in l and "Buy the CD" not in l]

        content = "\n\n".join(cleaned)

        file_name = os.path.join(out_dir, f"Testament-{pat_padded}-{pat_name}.md")
        yaml = f"""---
canon: Pseudepigrapha
source_type: Scripture
id: T12PAT-{pat_padded}
patriarch: "{pat_name}"
title: "{title}"
---

# {title}

{content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)

    print(f"Completed Testaments of Twelve Patriarchs: {pat_count} testaments generated!")

if __name__ == "__main__":
    fetch_jasher_wikisource()
    fetch_patriarchs()
