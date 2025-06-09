import fs from 'fs';
import path from 'path';

export default function SlokaGuru() {
  const dataPath = path.resolve('src/gurus/slokas_database.json');
  const slokas = JSON.parse(fs.readFileSync(dataPath, 'utf-8'));

  return slokas.map((sloka, index) => {
    return `Sloka ${index + 1}:\n${sloka.sanskrit}\n${sloka.translation}\n`;
  }).join('\n');
}
