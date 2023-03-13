#!/usr/bin/node
process = require('node:process');
a = parseInt(process.argv[2], 10);
if (isNaN(a)) {
  console.log('Missing size');
} else if (a > 0) {
  for (let i = 0; i < a; i++) {
    let x = '';
    for (let j = 0; j < a; j++) {
      x += 'X';
    }
    console.log(x);
  }
}
