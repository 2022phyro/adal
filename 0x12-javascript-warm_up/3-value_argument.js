#!/usr/bin/node
process = require('node:process');
const a = process.argv.length;
if (a === 2) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
