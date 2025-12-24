#!/usr/bin/env node

const fs = require('fs');

console.log('⏰ HyperCode Timestamp Update Tool\n');

const dataFile = 'hypercode_db.json';

try {
  const data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
  
  const now = new Date().toISOString();
  
  // Update timestamp
  data.last_updated = now;
  data.updated_by = process.env.USER || 'automated';
  
  if (data.monitoring) {
    data.monitoring.last_sync = now;
  }
  
  // Write back
  fs.writeFileSync(dataFile, JSON.stringify(data, null, 2));
  
  console.log(`✅ Timestamp updated: ${now}`);
  console.log(`🔄 Updated by: ${data.updated_by}`);
  
} catch (err) {
  console.error(`❌ Error: ${err.message}`);
  process.exit(1);
}
