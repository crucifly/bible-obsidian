import fs from 'fs';
import path from 'path';
import matter from 'gray-matter';
import * as readline from 'readline';

/**
 * JSONL Forge: The bridge from the Divine Vault to Machine Intelligence.
 * 
 * This script transforms Obsidian Markdown files into a JSONL format 
 * optimized for Gemma 4 E4B's instruction tuning, incorporating 
 * "thinking" blocks for canonical reasoning.
 */

interface VerseMetadata {
  id: string;
  canon: string;
  book: string;
  chapter: string;
  verse: string;
  source_type: string;
}

interface Gemma4JSONL {
  instruction: string;
  thinking: string;
  context: string;
  response: string;
}

const VAULT_PATH = '../bible-obsidian';
const OUTPUT_PATH = '../divine_training_set.jsonl';

async function forge() {
  console.log('🚀 Initializing JSONL Forge...');
  
  const files = getAllFiles(VAULT_PATH);
  const trainingData: Gemma4JSONL[] = [];

  for (const file of files) {
    if (path.extname(file) !== '.md') continue;
    if (file.includes('00_Schema.md') || file.includes('00_META')) continue;

    const content = fs.readFileSync(file, 'utf8');
    const { data, content: text } = matter(content);
    const meta = data as VerseMetadata;

    // Iron Curtain Validation: Only process files with source_type: Scripture
    if (meta.source_type !== 'Scripture') {
      console.warn(`⚠️ Skipping non-scripture file: ${file}`);
      continue;
    }

    // Construct the "Thinking" block for canonical reasoning
    const thinking = `This verse is identified as ID ${meta.id} from the ${meta.canon} canon. ` +
                    `It is located in ${meta.book}, Chapter ${meta.chapter}, Verse ${meta.verse}. ` +
                    `The response must be the verbatim text of the scripture to ensure zero interpretation.`;

    // Construct the instruction/response pair
    const instruction = `Provide the text for ${meta.book} ${meta.chapter}:${meta.verse} from the ${meta.canon} canon.`;
    const response = text.trim();

    trainingData.push({
      instruction,
      thinking,
      context: `Source: ${meta.id} (${meta.canon})`,
      response
    });
  }

  const jsonlContent = trainingData.map(item => JSON.stringify(item)).join('\n');
  fs.writeFileSync(OUTPUT_PATH, jsonlContent);

  console.log(`\n✅ Forge Complete!`);
  console.log(`Processed ${trainingData.length} verses into ${OUTPUT_PATH}`);
}

function getAllFiles(dirPath: string, arrayOfFiles: string[] = []) {
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

forge().catch(console.error);
