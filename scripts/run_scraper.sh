#!/bin/bash

# Setup directories
mkdir -p "08-NagHammadi/PistisSophia"
mkdir -p "09-Pseudepigrapha"
mkdir -p "tmp_html"

fetch_and_parse() {
    URL="$1"
    OUT_DIR="$2"
    ID="$3"
    TITLE="$4"
    TMP_FILE="tmp_html/${ID}.html"
    
    echo "Fetching $URL..."
    curl -sL -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" -H "Accept: text/html" "$URL" -o "$TMP_FILE"
    
    python3 scripts/parse_html.py --file "$TMP_FILE" --out "$OUT_DIR" --id "$ID" --title "$TITLE"
}

# Nag Hammadi & Gnostic Texts
fetch_and_parse "http://gnosis.org/naghamm/apocjn-meyer.html" "08-NagHammadi/ApocryphonOfJohn" "APOCJN" "Apocryphon of John"
fetch_and_parse "http://gnosis.org/library/marygosp.htm" "08-NagHammadi/GospelOfMary" "MARY" "Gospel of Mary"
fetch_and_parse "http://gnosis.org/naghamm/thunder.html" "08-NagHammadi/ThunderPerfectMind" "THUNDER" "Thunder Perfect Mind"
fetch_and_parse "http://gnosis.org/library/gjudas.html" "08-NagHammadi/GospelOfJudas" "JUDAS" "Gospel of Judas"

# Pistis Sophia
fetch_and_parse "http://gnosis.org/library/pistis-sophia/index.htm" "08-NagHammadi/PistisSophia" "PISTIS" "Pistis Sophia"

# Pseudepigrapha (Updated URLs based on common structures for these)
fetch_and_parse "https://sacred-texts.com/bib/fbe/fbe275.htm" "09-Pseudepigrapha/AscensionOfIsaiah" "ASCISA" "Ascension of Isaiah"
fetch_and_parse "https://sacred-texts.com/bib/fbe/fbe280.htm" "09-Pseudepigrapha/3Enoch" "3ENOCH" "3 Enoch"
fetch_and_parse "https://sacred-texts.com/bib/fbe/fbe290.htm" "09-Pseudepigrapha/ApocalypseOfAbraham" "APABR" "Apocalypse of Abraham"
fetch_and_parse "https://sacred-texts.com/bib/fbe/fbe266.htm" "09-Pseudepigrapha/SibyllineOracles" "SIB" "Sibylline Oracles"
fetch_and_parse "https://sacred-texts.com/bib/fbe/fbe250.htm" "09-Pseudepigrapha/Testaments12Patriarchs" "T12PAT" "Testaments of the Twelve Patriarchs"
fetch_and_parse "https://sacred-texts.com/bib/fbe/fbe005.htm" "09-Pseudepigrapha/AdamAndEve" "ADAMEVE" "Life of Adam and Eve"
fetch_and_parse "https://sacred-texts.com/chr/apo/jasher/index.htm" "09-Pseudepigrapha/BookOfJasher" "JASH" "Book of Jasher"
fetch_and_parse "https://sacred-texts.com/bib/fbe/fbe260.htm" "09-Pseudepigrapha/2Baruch" "2BAR" "2 Baruch"

rm -rf tmp_html
echo "Scraping complete."
