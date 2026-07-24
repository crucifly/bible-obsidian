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
    # Strip page indicators
    raw_text = re.sub(r'p\.\s*\d+', '', raw_text)
    raw_text = re.sub(r'\|\s*\d+\.\s*', '', raw_text)

    lines = [line.strip() for line in raw_text.split('\n') if line.strip()]
    cleaned = []
    for line in lines:
        if "The Gnostic Society Library" in line or "Return to" in line or "Archive" in line or "Next:" in line or "Previous" in line or "Index" in line:
            continue
        if "Sacred Texts" in line or "Internet Sacred Text Archive" in line or "itemListElement" in line or "BreadcrumbList" in line:
            continue
        cleaned.append(line)

    content = "\n\n".join(cleaned)
    content = re.sub(r'\n{3,}', '\n\n', content).strip()
    return content

# 1. Scrape All Remaining Nag Hammadi Codices
def scrape_remaining_nag_hammadi():
    codices = [
        {"url": "http://gnosis.org/naghamm/hypostas.html", "dir": "08-NagHammadi/HypostasisOfTheArchons", "id": "HYPOSTAS", "title": "Hypostasis of the Archons"},
        {"url": "http://gnosis.org/naghamm/origin.html", "dir": "08-NagHammadi/OriginOfTheWorld", "id": "ORIGIN", "title": "On the Origin of the World"},
        {"url": "http://gnosis.org/naghamm/sjc.html", "dir": "08-NagHammadi/SophiaOfJesusChrist", "id": "SJC", "title": "Sophia of Jesus Christ"},
        {"url": "http://gnosis.org/naghamm/dialog.html", "dir": "08-NagHammadi/DialogueOfTheSavior", "id": "DIALOG", "title": "Dialogue of the Savior"},
        {"url": "http://gnosis.org/naghamm/tripart.htm", "dir": "08-NagHammadi/TripartiteTractate", "id": "TRIPART", "title": "Tripartite Tractate"},
        {"url": "http://gnosis.org/naghamm/trimorph.html", "dir": "08-NagHammadi/TrimorphicProtennoia", "id": "TRIMORPH", "title": "Trimorphic Protennoia"},
        {"url": "http://gnosis.org/naghamm/2seth.html", "dir": "08-NagHammadi/SecondDiscourseGreatSeth", "id": "2SETH", "title": "Second Discourse of Great Seth"},
        {"url": "http://gnosis.org/naghamm/exe.html", "dir": "08-NagHammadi/ExegesisOnTheSoul", "id": "EXESOUL", "title": "Exegesis on the Soul"},
        {"url": "http://gnosis.org/naghamm/autho.html", "dir": "08-NagHammadi/AuthoritativeTeaching", "id": "AUTHO", "title": "Authoritative Teaching"},
        {"url": "http://gnosis.org/naghamm/cgp.html", "dir": "08-NagHammadi/GreatPower", "id": "GREATPOW", "title": "Concept of Our Great Power"},
        {"url": "http://gnosis.org/naghamm/thunder.html", "dir": "08-NagHammadi/ThunderPerfectMind", "id": "THUNDER", "title": "Thunder, Perfect Mind"},
        {"url": "http://gnosis.org/naghamm/allogenes.html", "dir": "08-NagHammadi/Allogenes", "id": "ALLOGENES", "title": "Allogenes"},
        {"url": "http://gnosis.org/naghamm/zostr.html", "dir": "08-NagHammadi/Zostrianos", "id": "ZOST", "title": "Zostrianos"}
    ]

    print("Scraping remaining 13 Nag Hammadi codices...")

    for item in codices:
        out_dir = item["dir"]
        if os.path.exists(out_dir):
            for f in os.listdir(out_dir): os.remove(os.path.join(out_dir, f))
        os.makedirs(out_dir, exist_ok=True)

        req = urllib.request.Request(item["url"], headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching {item['url']}: {e}")
            continue

        content = clean_text_block(html_str)

        file_name = os.path.join(out_dir, "Section-01.md")
        yaml = f"""---
canon: Nag-Hammadi
source_type: Gnostic-Codex
id: {item['id']}-01
title: "{item['title']}"
---

# {item['title']}

{content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)

        print(f"Successfully scraped & cleaned {item['title']} -> {file_name}")

# 2. Scrape Full Book of Jasher (91 Chapters)
def scrape_full_book_of_jasher():
    out_dir = "09-Pseudepigrapha/BookOfJasher"
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir): os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)

    print("Scraping all 91 chapters of the Book of Jasher from sacred-texts...")

    success = 0
    for ch in range(1, 92):
        ch_padded = f"{ch:02d}"
        url = f"https://sacred-texts.com/chr/apo/jasher/jasher{ch:02d}.htm"
        req = urllib.request.Request(url, headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching Jasher chapter {ch}: {e}")
            continue

        content = clean_text_block(html_str)
        if len(content) < 50: continue

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

    print(f"Completed Book of Jasher: {success} chapters generated.")

if __name__ == "__main__":
    scrape_remaining_nag_hammadi()
    scrape_full_book_of_jasher()
