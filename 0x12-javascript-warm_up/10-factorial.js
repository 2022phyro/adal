#!/usr/bin/node
process = require('node:process');
a = parseInt(process.argv[2], 10);
function factorial (n) {
  if (n == 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
if (isNaN(a)) {
  console.log('1');
} else {
  console.log(factorial(a));
}
