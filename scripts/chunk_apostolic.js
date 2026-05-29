const fs = require('fs');
const path = require('path');

const inputFile = '+ resources/apostolic_constitutions.txt';
const outputDir = 'bible-obsidian/07-EthiopicApocrypha/72-ApostolicConstitutions';

function parseApostolicConstitutions() {
    if (!fs.existsSync(inputFile)) {
        console.error("Input file not found at " + inputFile);
        return;
    }
    let content = fs.readFileSync(inputFile, 'utf-8');
    
    // Normalize newlines
    content = content.replace(/\r\n/g, '\n');

    // Split by Book
    const bookParts = content.split(/(?:^|\n)BOOK\s+([IVXLCDM]+)\n/);
    
    if (bookParts.length < 2) {
        console.error("No books found.");
        return;
    }

    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    let totalVerses = 0;

    // bookParts[0] is intro text before first BOOK
    for (let i = 1; i < bookParts.length; i += 2) {
        const bookNum = bookParts[i];
        let bookContent = bookParts[i+1];
        
        console.log(`Processing Book ${bookNum}...`);

        // We can ignore the "SEC. X.—TITLE" stuff and just split by CHAPTER
        // Or we can parse it if we want. But the ID structure APCON-BOOK-CHAP-VERSE is simpler.
        const chapterRegex = /(?:^|\n)CHAPTER\s+(\d+|[IVXLCDM]+)\n/g;
        let match;
        let chapters = [];
        let lastIndex = 0;

        while ((match = chapterRegex.exec(bookContent)) !== null) {
            if (chapters.length > 0) {
                chapters[chapters.length - 1].content = bookContent.substring(lastIndex, match.index).trim();
            }
            chapters.push({
                num: match[1],
                content: ''
            });
            lastIndex = match.index + match[0].length;
        }

        if (chapters.length > 0) {
            chapters[chapters.length - 1].content = bookContent.substring(lastIndex).trim();
        }

        for (const ch of chapters) {
            // Convert roman numeral chapters to decimal if needed, but keeping original might be fine.
            // Verse pattern: usually starts with a number.
            const verseRegex = /(?:^|\n)(\d+)\s+/g;
            let vMatch;
            let verses = [];
            let vLastIndex = 0;

            while ((vMatch = verseRegex.exec(ch.content)) !== null) {
                if (verses.length > 0) {
                    verses[verses.length - 1].text = ch.content.substring(vLastIndex, vMatch.index).trim();
                }
                verses.push({
                    num: vMatch[1],
                    text: ''
                });
                vLastIndex = vMatch.index + vMatch[0].length;
            }

            if (verses.length > 0) {
                verses[verses.length - 1].text = ch.content.substring(vLastIndex).trim();
            } else if (ch.content.length > 0) {
                // If no verse numbers, treat whole chapter as verse 1
                verses.push({ num: '1', text: ch.content });
            }

            for (const v of verses) {
                let cleanText = v.text.replace(/\n/g, ' ').replace(/\s+/g, ' ').trim();
                if (cleanText.length < 2) continue;

                const verseDir = path.join(outputDir, `Book ${bookNum}`, `Chapter ${ch.num}`);
                if (!fs.existsSync(verseDir)) {
                    fs.mkdirSync(verseDir, { recursive: true });
                }

                const verseFile = path.join(verseDir, `${ch.num}-${v.num}.md`);
                
                const yaml = `---
id: APCON-${bookNum}-${ch.num}-${v.num}
canon: Ethiopic-81
canon_tier: broader
book: Apostolic Constitutions
chapter: ${ch.num}
verse: ${v.num}
source_type: Scripture
category: Church Law
---

${cleanText}
`;
                fs.writeFileSync(verseFile, yaml);
                totalVerses++;
            }
        }
    }
    console.log(`Done parsing Apostolic Constitutions. Total verses: ${totalVerses}`);
}

parseApostolicConstitutions();
