#!/usr/bin/node
process = require('node:process');
a = parseInt(process.argv[2], 10);
if (isNaN(a)) {
  console.log('Missing number of occurences');
} else if (a > 0) {
  for (let i = 0; i < a; i++) {
    console.log('C is fun');
  }
}
