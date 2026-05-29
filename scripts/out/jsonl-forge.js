"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const fs_1 = __importDefault(require("fs"));
const path_1 = __importDefault(require("path"));
const gray_matter_1 = __importDefault(require("gray-matter"));
const VAULT_PATH = '../bible-obsidian';
const OUTPUT_PATH = '../divine_training_set.jsonl';
async function forge() {
    console.log('🚀 Initializing JSONL Forge...');
    const files = getAllFiles(VAULT_PATH);
    const trainingData = [];
    for (const file of files) {
        if (path_1.default.extname(file) !== '.md')
            continue;
        if (file.includes('00_Schema.md') || file.includes('00_META'))
            continue;
        const content = fs_1.default.readFileSync(file, 'utf8');
        const { data, content: text } = (0, gray_matter_1.default)(content);
        const meta = data;
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
    fs_1.default.writeFileSync(OUTPUT_PATH, jsonlContent);
    console.log(`\n✅ Forge Complete!`);
    console.log(`Processed ${trainingData.length} verses into ${OUTPUT_PATH}`);
}
function getAllFiles(dirPath, arrayOfFiles = []) {
    const files = fs_1.default.readdirSync(dirPath);
    files.forEach(file => {
        const fullPath = path_1.default.join(dirPath, file);
        if (fs_1.default.statSync(fullPath).isDirectory()) {
            getAllFiles(fullPath, arrayOfFiles);
        }
        else {
            arrayOfFiles.push(fullPath);
        }
    });
    return arrayOfFiles;
}
forge().catch(console.error);
