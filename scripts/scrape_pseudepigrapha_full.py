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
        if "Sacred Texts" in line or "Internet Sacred Text Archive" in line or "itemListElement" in line or "BreadcrumbList" in line or "Home" in line:
            continue
        cleaned.append(line)

    content = "\n\n".join(cleaned)
    content = re.sub(r'\n{3,}', '\n\n', content).strip()
    return content

# Sibylline Oracles Books 1 through 12
def scrape_sibylline_oracles():
    out_dir = "09-Pseudepigrapha/SibyllineOracles"
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir): os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)

    print("Scraping Sibylline Oracles (Books 1–12) from sacred-texts...")

    for bk in range(1, 13):
        bk_padded = f"{bk:02d}"
        url = f"https://sacred-texts.com/cla/sib/sib{bk_padded}.htm"
        req = urllib.request.Request(url, headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching Sibylline Oracles Book {bk}: {e}")
            continue

        content = clean_text_block(html_str)
        if len(content) < 50: continue

        file_name = os.path.join(out_dir, f"Book-{bk_padded}.md")
        yaml = f"""---
canon: Pseudepigrapha
source_type: Scripture
id: SIB-{bk_padded}
book: {bk}
title: "Sibylline Oracles - Book {bk}"
---

# Sibylline Oracles - Book {bk}

{content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)

    print("Completed Sibylline Oracles ingestion.")

# Testaments of the Twelve Patriarchs (12 Patriarchs)
def scrape_testaments_12_patriarchs():
    out_dir = "09-Pseudepigrapha/Testaments12Patriarchs"
    if os.path.exists(out_dir):
        for f in os.listdir(out_dir): os.remove(os.path.join(out_dir, f))
    os.makedirs(out_dir, exist_ok=True)

    print("Scraping Testaments of the Twelve Patriarchs...")

    patriarchs = ["Reuben", "Simeon", "Levi", "Judah", "Issachar", "Zebulun", "Dan", "Naphtali", "Gad", "Asher", "Joseph", "Benjamin"]

    for idx, pat in enumerate(patriarchs, 1):
        pat_padded = f"{idx:02d}"
        # fbe055.htm through fbe066.htm
        code = 54 + idx
        url = f"https://sacred-texts.com/bib/fbe/fbe{code:03d}.htm"
        req = urllib.request.Request(url, headers=headers)
        try:
            html_bytes = urllib.request.urlopen(req).read()
            html_str = html_bytes.decode('utf-8', errors='ignore')
        except Exception as e:
            print(f"Error fetching Testament of {pat}: {e}")
            continue

        content = clean_text_block(html_str)

        file_name = os.path.join(out_dir, f"Testament-{pat_padded}-{pat}.md")
        yaml = f"""---
canon: Pseudepigrapha
source_type: Scripture
id: T12PAT-{pat_padded}
patriarch: "{pat}"
title: "Testament of {pat}"
---

# Testament of {pat}

{content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)

    print("Completed Testaments of Twelve Patriarchs ingestion.")

# 3 Enoch, Apocalypse of Abraham, 2 Baruch, Adam & Eve, Ascension of Isaiah
def scrape_remaining_pseudepigrapha():
    texts = [
        {"url": "https://sacred-texts.com/bib/fbe/fbe280.htm", "dir": "09-Pseudepigrapha/3Enoch", "id": "3ENOCH", "title": "3 Enoch (Hebrew Book of Enoch)"},
        {"url": "https://sacred-texts.com/bib/fbe/fbe290.htm", "dir": "09-Pseudepigrapha/ApocalypseOfAbraham", "id": "APABR", "title": "Apocalypse of Abraham"},
        {"url": "https://sacred-texts.com/bib/fbe/fbe260.htm", "dir": "09-Pseudepigrapha/2Baruch", "id": "2BAR", "title": "2 Baruch (Syriac Apocalypse)"},
        {"url": "https://sacred-texts.com/bib/fbe/fbe005.htm", "dir": "09-Pseudepigrapha/AdamAndEve", "id": "ADAMEVE", "title": "Life of Adam and Eve"},
        {"url": "https://sacred-texts.com/bib/fbe/fbe275.htm", "dir": "09-Pseudepigrapha/AscensionOfIsaiah", "id": "ASCISA", "title": "Ascension of Isaiah"}
    ]

    for item in texts:
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

        file_name = os.path.join(out_dir, "Chapter-01.md")
        yaml = f"""---
canon: Pseudepigrapha
source_type: Scripture
id: {item['id']}-01
title: "{item['title']}"
---

# {item['title']}

{content}
"""
        with open(file_name, 'w', encoding='utf-8') as f:
            f.write(yaml)
        print(f"Completed {item['title']} -> {file_name}")

if __name__ == "__main__":
    scrape_sibylline_oracles()
    scrape_testaments_12_patriarchs()
    scrape_remaining_pseudepigrapha()
