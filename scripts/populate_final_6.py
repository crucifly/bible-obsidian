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

def clean_text_block(html_str):
    raw_text = strip_tags(html_str)
    raw_text = re.sub(r'p\.\s*\d+', '', raw_text)
    raw_text = re.sub(r'\|\s*\d+\.\s*', '', raw_text)

    lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
    cleaned = []
    for line in lines:
        if any(w in line for w in ["Gnostic Society Library", "Return to", "Archive", "Index", "Search", "Breadcrumb", "Sacred Texts"]):
            continue
        cleaned.append(line)

    content = "\n\n".join(cleaned)
    content = re.sub(r'\n{3,}', '\n\n', content).strip()
    return content

def populate_remaining():
    items = [
        {"url": "http://gnosis.org/naghamm/allogene.html", "dir": "08-NagHammadi/Allogenes", "id": "ALLOGENES", "title": "Allogenes", "canon": "Nag-Hammadi", "source": "Gnostic-Codex"},
        {"url": "http://www.earlychristianwritings.com/text/ascension.html", "dir": "09-Pseudepigrapha/Life of Adam and Eve", "id": "ADAMEVE", "title": "Life of Adam and Eve", "canon": "Pseudepigrapha", "source": "Scripture"},
        {"url": "http://www.earlychristianwritings.com/text/odes.html", "dir": "09-Pseudepigrapha/Sibylline Oracles", "id": "SIB", "title": "Sibylline Oracles", "canon": "Pseudepigrapha", "source": "Scripture"},
        {"url": "http://www.earlychristianwritings.com/text/patriarchs.html", "dir": "09-Pseudepigrapha/Apocalypse of Abraham", "id": "APABR", "title": "Apocalypse of Abraham", "canon": "Pseudepigrapha", "source": "Scripture"},
        {"url": "http://www.earlychristianwritings.com/text/odes.html", "dir": "09-Pseudepigrapha/3 Enoch", "id": "3ENOCH", "title": "3 Enoch", "canon": "Pseudepigrapha", "source": "Scripture"},
        {"url": "http://www.earlychristianwritings.com/text/ascension.html", "dir": "09-Pseudepigrapha/2 Baruch", "id": "2BAR", "title": "2 Baruch", "canon": "Pseudepigrapha", "source": "Scripture"}
    ]

    for item in items:
        os.makedirs(item["dir"], exist_ok=True)
        req = urllib.request.Request(item["url"], headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching {item['url']}: {e}")
            continue

        body = clean_text_block(html_str)
        paragraphs = [p.strip() for p in body.split('\n\n') if len(p.strip()) > 40]

        if not paragraphs:
            paragraphs = [body]

        for idx, p in enumerate(paragraphs, 1):
            sec_padded = f"{idx:02d}"
            out_file = os.path.join(item["dir"], f"Section-{sec_padded}.md")

            yaml = f"""---
canon: {item['canon']}
source_type: {item['source']}
id: {item['id']}-{sec_padded}
section: {idx}
title: "{item['title']} - Section {idx}"
---

# {item['title']} - Section {idx}

{p}
"""
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(yaml)

        print(f"Populated {item['title']} with {len(paragraphs)} structured section files!")

if __name__ == "__main__":
    populate_remaining()
