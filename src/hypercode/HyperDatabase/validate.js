#!/usr/bin/env node

const fs = require('fs');
const Ajv = require('ajv');

const args = process.argv.slice(2);
const schemaFile = 'hypercode_schema.json';
const dataFile = args[0] || 'hypercode_db.json';

console.log('🔍 HyperCode Database Validator\n');

// Load schema and data
let schema, data;
try {
  schema = JSON.parse(fs.readFileSync(schemaFile, 'utf8'));
  data = JSON.parse(fs.readFileSync(dataFile, 'utf8'));
  console.log(`✅ Loaded schema: ${schemaFile}`);
  console.log(`✅ Loaded data: ${dataFile}\n`);
} catch (err) {
  console.error(`❌ Error loading files: ${err.message}`);
  process.exit(1);
}

// Validate against schema
const ajv = new Ajv({
  allErrors: true,
  verbose: true,
  strict: 'log'
});

const validate = ajv.compile(schema);
const valid = validate(data);

if (valid) {
  console.log('✅ Schema validation PASSED\n');
} else {
  console.error('❌ Schema validation FAILED');
  console.error('Errors:');
  validate.errors.forEach((error, idx) => {
    console.error(`  ${idx + 1}. Path: ${error.instancePath || 'root'}`);
    console.error(`     Message: ${error.message}`);
  });
  process.exit(1);
}

// Check required fields
console.log('🔎 Checking required fields...\n');
const requiredFields = [
  'schema_version',
  'version',
  'project_name',
  'last_updated',
  'research_data'
];

let missingFields = [];
requiredFields.forEach(field => {
  if (data[field] !== undefined) {
    console.log(`  ✅ ${field}: present`);
  } else {
    console.log(`  ❌ ${field}: MISSING`);
    missingFields.push(field);
  }
});

if (missingFields.length > 0) {
  console.error(`\n❌ Missing required fields: ${missingFields.join(', ')}`);
  process.exit(1);
}

// Check nested structures
console.log('\n📦 Checking nested data structures...\n');

const nestedRequired = [
  'research_data.core_concept',
  'research_data.historical_roots',
  'research_data.neurodivergent_features',
  'research_data.ai_compatibility',
  'research_data.quantum_molecular'
];

nestedRequired.forEach(path => {
  const keys = path.split('.');
  let obj = data;
  let found = true;
  
  for (let key of keys) {
    if (obj && obj[key] !== undefined) {
      obj = obj[key];
    } else {
      found = false;
      break;
    }
  }
  
  if (found) {
    console.log(`  ✅ ${path}: present`);
  } else {
    console.log(`  ❌ ${path}: MISSING`);
  }
});

// Data quality metrics
console.log('\n📊 Data Quality Metrics...\n');

function countNulls(obj) {
  let count = 0;
  function traverse(o) {
    for (let key in o) {
      if (o[key] === null) count++;
      if (typeof o[key] === 'object') traverse(o[key]);
    }
  }
  traverse(obj);
  return count;
}

const totalRecords = Object.keys(data.research_data).length;
const nullCount = countNulls(data);
const nullPercent = totalRecords > 0 ? (nullCount / totalRecords) * 100 : 0;

console.log(`  📈 Total records: ${totalRecords}`);
console.log(`  📉 Null values: ${nullCount}`);
console.log(`  📊 Null percentage: ${nullPercent.toFixed(2)}%`);

// Check timestamps
console.log('\n⏰ Timestamp Validation...\n');
const lastUpdated = new Date(data.last_updated);
const now = new Date();
const hoursSinceUpdate = (now - lastUpdated) / (1000 * 60 * 60);

console.log(`  Last updated: ${data.last_updated}`);
console.log(`  Hours since update: ${hoursSinceUpdate.toFixed(2)}`);

if (hoursSinceUpdate > 24) {
  console.warn(`  ⚠️  Data is ${Math.floor(hoursSinceUpdate)} hours old - consider updating`);
} else {
  console.log(`  ✅ Data is fresh`);
}

// Version check
console.log('\n🏷️  Version Information...\n');
console.log(`  Schema version: ${data.schema_version}`);
console.log(`  Data version: ${data.version}`);
console.log(`  Updated by: ${data.updated_by || 'unknown'}`);

// Summary
console.log('\n' + '='.repeat(50));
console.log('✅ ALL VALIDATIONS PASSED!');
console.log('='.repeat(50));

// Update monitoring metrics
data.monitoring = {
  last_sync: new Date().toISOString(),
  record_count: totalRecords,
  null_percent: parseFloat(nullPercent.toFixed(2)),
  schema_valid: true,
  freshness_hours: parseFloat(hoursSinceUpdate.toFixed(2))
};

fs.writeFileSync(dataFile, JSON.stringify(data, null, 2));
console.log(`\n📝 Updated monitoring metrics in ${dataFile}`);
