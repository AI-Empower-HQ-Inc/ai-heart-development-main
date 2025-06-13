import fs from 'fs';
import path from 'path';

export function buildPrompt({ basePrompt, question, context }) {
  return `${basePrompt}

Question: ${question}
Context: ${context}

Please provide guidance that is:
1. Practical and applicable
2. Deeply transformative
3. Rooted in genuine spiritual wisdom
4. Compassionate yet direct
`;
}

export function buildSlokaPrompt(index = 0) {
  const dataPath = path.resolve('src/gurus/slokas_database.json');
  const slokas = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));

  const sloka = slokas[index];
  return `
🕉️ Sanskrit: ${sloka.sanskrit}
🔤 Transliteration: ${sloka.transliteration}
🌱 Meaning: ${sloka.meaning}
📖 Context: ${sloka.context}
🧘 Reflection Question: ${sloka.reflection_questions.join('\n')}
`;
}
