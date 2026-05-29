const fs = require('fs');
const path = require('path');

const inputFile = '+ resources/didascalia.txt';
const outputDir = 'bible-obsidian/07-EthiopicApocrypha/73-Didascalia';

function parseDidascalia() {
    if (!fs.existsSync(inputFile)) {
        console.error("Input file not found at " + inputFile);
        return;
    }
    let content = fs.readFileSync(inputFile, 'utf-8');
    
    // Normalize newlines
    content = content.replace(/\r\n/g, '\n');

    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    let totalVerses = 0;

    const chapterRegex = /(?:^|\n)CHAPTER\s+(\d+|[IVXLCDM]+)\n/g;
    let match;
    let chapters = [];
    let lastIndex = 0;

    while ((match = chapterRegex.exec(content)) !== null) {
        if (chapters.length > 0) {
            chapters[chapters.length - 1].content = content.substring(lastIndex, match.index).trim();
        }
        chapters.push({
            num: match[1],
            content: ''
        });
        lastIndex = match.index + match[0].length;
    }

    if (chapters.length > 0) {
        chapters[chapters.length - 1].content = content.substring(lastIndex).trim();
    }

    for (const ch of chapters) {
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

            const chapterDir = path.join(outputDir, `Chapter ${ch.num}`);
            if (!fs.existsSync(chapterDir)) {
                fs.mkdirSync(chapterDir, { recursive: true });
            }

            const verseFile = path.join(chapterDir, `${ch.num}-${v.num}.md`);
            
            const yaml = `---
id: DIDAS-${ch.num}-${v.num}
canon: Ethiopic-81
canon_tier: broader
book: Didascalia
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
    console.log(`Done parsing Didascalia. Total verses: ${totalVerses}`);
}

parseDidascalia();
