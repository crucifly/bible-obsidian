const fs = require('fs');
const path = require('path');

/**
 * Universal Chunker for scraped monolithic notes in Nag Hammadi and Pseudepigrapha.
 * Converts single files like 08-NagHammadi/ApocryphonOfJohn/APOCJN-1-1.md
 * into structured notes like Section-1.md, Section-2.md, etc.
 */

const targets = [
    {
        dir: '08-NagHammadi/ApocryphonOfJohn',
        file: 'APOCJN-1-1.md',
        prefix: 'APOCJN',
        canon: 'Nag-Hammadi',
        source_type: 'Gnostic-Codex',
        namingStyle: 'Section' // Section-1.md
    },
    {
        dir: '08-NagHammadi/GospelOfMary',
        file: 'MARY-1-1.md',
        prefix: 'MARY',
        canon: 'Nag-Hammadi',
        source_type: 'Gnostic-Codex',
        namingStyle: 'Section'
    },
    {
        dir: '08-NagHammadi/ThunderPerfectMind',
        file: 'THUNDER-1-1.md',
        prefix: 'THUNDER',
        canon: 'Nag-Hammadi',
        source_type: 'Gnostic-Codex',
        namingStyle: 'Section'
    },
    {
        dir: '08-NagHammadi/GospelOfJudas',
        file: 'JUDAS-1-1.md',
        prefix: 'JUDAS',
        canon: 'Nag-Hammadi',
        source_type: 'Gnostic-Codex',
        namingStyle: 'Section'
    },
    {
        dir: '08-NagHammadi/PistisSophia',
        file: 'PISTIS-1-1.md',
        prefix: 'PISTIS',
        canon: 'Nag-Hammadi',
        source_type: 'Gnostic-Codex',
        namingStyle: 'Section'
    },
    {
        dir: '09-Pseudepigrapha/AscensionOfIsaiah',
        file: 'ASCISA-1-1.md',
        prefix: 'ASCISA',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Chapter'
    },
    {
        dir: '09-Pseudepigrapha/3Enoch',
        file: '3ENOCH-1-1.md',
        prefix: '3ENOCH',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Chapter'
    },
    {
        dir: '09-Pseudepigrapha/ApocalypseOfAbraham',
        file: 'APABR-1-1.md',
        prefix: 'APABR',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Chapter'
    },
    {
        dir: '09-Pseudepigrapha/SibyllineOracles',
        file: 'SIB-1-1.md',
        prefix: 'SIB',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Book'
    },
    {
        dir: '09-Pseudepigrapha/Testaments12Patriarchs',
        file: 'T12PAT-1-1.md',
        prefix: 'T12PAT',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Section'
    },
    {
        dir: '09-Pseudepigrapha/AdamAndEve',
        file: 'ADAMEVE-1-1.md',
        prefix: 'ADAMEVE',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Chapter'
    },
    {
        dir: '09-Pseudepigrapha/BookOfJasher',
        file: 'JASH-1-1.md',
        prefix: 'JASH',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Chapter'
    },
    {
        dir: '09-Pseudepigrapha/2Baruch',
        file: '2BAR-1-1.md',
        prefix: '2BAR',
        canon: 'Pseudepigrapha',
        source_type: 'Scripture',
        namingStyle: 'Chapter'
    }
];

function chunkFile(target) {
    const filePath = path.join(target.dir, target.file);
    if (!fs.existsSync(filePath)) {
        console.log(`Skipping ${filePath} (not found)`);
        return;
    }

    let raw = fs.readFileSync(filePath, 'utf-8');

    // Remove existing YAML frontmatter if present
    raw = raw.replace(/^---[\s\S]*?---\n*/, '');

    // Filter out common web scrape boilerplate header/footer text
    const boilerplatePatterns = [
        /The Nag Hammadi Library/gi,
        /Gnostic Society Library/gi,
        /Non-commercial use/gi,
        /http:\/\/www\.gnosis\.org/gi,
        /http:\/\/www\.sacred-texts\.com/gi,
        /http:\/\/www\.earlychristianwritings\.com/gi,
        /Early Christian Writings/gi,
        /Search Site/gi,
        /Return to Home/gi,
        /Table of Contents/gi
    ];

    // Split text into meaningful sections by paragraphs or headings
    let paragraphs = raw.split(/\n{2,}/)
        .map(p => p.trim())
        .filter(p => {
            if (p.length < 25) return false; // Ignore short lines/nav buttons
            for (let pat of boilerplatePatterns) {
                if (pat.test(p)) return false;
            }
            return true;
        });

    if (paragraphs.length === 0) {
        console.log(`No valid content extracted from ${filePath}`);
        return;
    }

    console.log(`Chunking ${target.prefix}: ${paragraphs.length} sections found.`);

    let count = 0;
    paragraphs.forEach((p, idx) => {
        const secNum = idx + 1;
        const noteName = `${target.namingStyle}-${secNum}.md`;
        const outPath = path.join(target.dir, noteName);

        const yaml = `---
canon: ${target.canon}
source_type: ${target.source_type}
id: ${target.prefix}-${secNum}
section: ${secNum}
---

${p}
`;

        fs.writeFileSync(outPath, yaml, 'utf-8');
        count++;
    });

    // Optionally remove original monolithic file
    fs.unlinkSync(filePath);
    console.log(`Successfully generated ${count} files in ${target.dir}`);
}

function run() {
    targets.forEach(chunkFile);
    console.log("Chunking pipeline complete.");
}

run();
