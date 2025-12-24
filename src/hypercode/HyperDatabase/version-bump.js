#!/usr/bin/env node

const fs = require('fs');

console.log('🏷️  HyperCode Version Bump Tool\n');

const dataFile = 'hypercode_db.json';

try {
  const data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
  
  // Parse current version
  const [major, minor, patch] = data.version.split('.').map(Number);
  
  // Determine bump type from args
  const bumpType = process.argv[2] || 'patch';
  let newVersion;
  
  switch(bumpType) {
    case 'major':
      newVersion = `${major + 1}.0.0`;
      break;
    case 'minor':
      newVersion = `${major}.${minor + 1}.0`;
      break;
    case 'patch':
    default:
      newVersion = `${major}.${minor}.${patch + 1}`;
  }
  
  // Update data
  data.version = newVersion;
  data.last_updated = new Date().toISOString();
  data.updated_by = process.env.USER || 'automated';
  
  // Write back
  fs.writeFileSync(dataFile, JSON.stringify(data, null, 2));
  
  console.log(`✅ Version bumped: ${data.version}`);
  console.log(`🔄 Updated by: ${data.updated_by}`);
  console.log(`⏰ Updated at: ${data.last_updated}`);
  
} catch (err) {
  console.error(`❌ Error: ${err.message}`);
  process.exit(1);
}
