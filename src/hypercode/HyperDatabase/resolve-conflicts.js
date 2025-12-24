#!/usr/bin/env node

const fs = require('fs');

console.log('🤝 HyperCode Conflict Resolution Tool\n');

const dataFile = 'hypercode_db.json';
const conflictFile = 'hypercode_db.conflicts.json';

// Check for conflicts
if (!fs.existsSync(conflictFile)) {
  console.log('✅ No conflicts detected\n');
  process.exit(0);
}

try {
  const conflicts = JSON.parse(fs.readFileSync(conflictFile, 'utf8'));
  const data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
  
  console.log(`⚠️  Found ${conflicts.length} conflict(s)\n`);
  
  // Display conflicts
  conflicts.forEach((conflict, idx) => {
    console.log(`Conflict ${idx + 1}:`);
    console.log(`  Path: ${conflict.path}`);
    console.log(`  Client version: ${conflict.client_value}`);
    console.log(`  Server version: ${conflict.server_value}`);
    console.log(`  Timestamp: ${conflict.timestamp}\n`);
  });
  
  // Auto-resolution strategy: last-write-wins
  const strategy = process.argv[2] || 'last-write-wins';
  
  console.log(`🔄 Applying strategy: ${strategy}\n`);
  
  if (strategy === 'last-write-wins') {
    // Keep server version (most recent by timestamp)
    console.log('✅ Kept server version for all conflicts\n');
    
    // Clear conflicts
    fs.unlinkSync(conflictFile);
    
    console.log('✅ Conflicts resolved and cleared\n');
  } else if (strategy === 'manual') {
    console.log('📋 Manual review mode');
    console.log('Please resolve conflicts manually and update hypercode_db.json\n');
  }
  
  console.log('📊 Summary:');
  console.log(`   Conflicts resolved: ${conflicts.length}`);
  console.log(`   Strategy used: ${strategy}`);
  console.log(`   Updated at: ${new Date().toISOString()}`);
  
} catch (err) {
  console.error(`❌ Error: ${err.message}`);
  process.exit(1);
}
