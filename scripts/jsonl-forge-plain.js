const fs = require('fs');
const path = require('path');

/**
 * JSONL Forge: The bridge from the Divine Vault to Machine Intelligence.
 * 
 * Plain JS version (no dependencies)
 */

function parseFrontmatter(content) {
  const match = content.match(/^---\n([\s\S]*?)\n---\n([\s\S]*)$/);
  if (!match) return null;
  
  const frontmatter = {};
  match[1].split('\n').forEach(line => {
    const colonIndex = line.indexOf(':');
    if (colonIndex !== -1) {
      const key = line.substring(0, colonIndex).trim();
      const value = line.substring(colonIndex + 1).trim();
      frontmatter[key] = value;
    }
  });
  
  return {
    data: frontmatter,
    content: match[2].trim()
  };
}

const VAULT_PATH = '..';
const OUTPUT_PATH = '../divine_training_set.jsonl';

function getAllFiles(dirPath, arrayOfFiles = []) {
  const files = fs.readdirSync(dirPath);

  files.forEach(file => {
    const fullPath = path.join(dirPath, file);
    if (fs.statSync(fullPath).isDirectory()) {
      getAllFiles(fullPath, arrayOfFiles);
    } else {
      arrayOfFiles.push(fullPath);
    }
  });

  return arrayOfFiles;
}

async function forge() {
  console.log('🚀 Initializing JSONL Forge (Plain JS)...');
  
  const files = getAllFiles(VAULT_PATH);
  const trainingData = [];

  for (const file of files) {
    if (path.extname(file) !== '.md') continue;
    if (file.includes('00_Schema.md') || file.includes('00_META') || file.includes('CANON_INVENTORY.md')) continue;

    const content = fs.readFileSync(file, 'utf8');
    const parsed = parseFrontmatter(content);
    
    if (!parsed) continue;
    
    const meta = parsed.data;
    const text = parsed.content;

    // Iron Curtain Validation: Only process files with source_type: Scripture
    if (meta.source_type !== 'Scripture') {
      // console.warn(`⚠️ Skipping non-scripture file: ${file}`);
      continue;
    }

    // Construct the "Thinking" block for canonical reasoning
    let chapter = meta.chapter;
    let verse = meta.verse;
    
    if (!chapter || !verse) {
      // Attempt to parse from ID (format: BOOK-CH-V)
      const idParts = meta.id ? meta.id.split('-') : [];
      if (idParts.length >= 3) {
        chapter = idParts[idParts.length - 2];
        verse = idParts[idParts.length - 1];
      }
    }

    const thinking = `This verse is identified as ID ${meta.id} from the ${meta.canon} canon. ` +
                    `It is located in ${meta.book}, Chapter ${chapter}, Verse ${verse}. ` +
                    `The response must be the verbatim text of the scripture to ensure zero interpretation.`;

    // Construct the instruction/response pair
    const instruction = `Provide the text for ${meta.book} ${chapter}:${verse} from the ${meta.canon} canon.`;
    const response = text.trim();

    trainingData.push({
      instruction,
      thinking,
      context: `Source: ${meta.id} (${meta.canon})`,
      response
    });
  }

  const jsonlContent = trainingData.map(item => JSON.stringify(item)).join('\n');
  fs.writeFileSync(OUTPUT_PATH, jsonlContent + '\n');

  console.log(`\n✅ Forge Complete!`);
  console.log(`Processed ${trainingData.length} verses into ${OUTPUT_PATH}`);
}

forge().catch(console.error);
