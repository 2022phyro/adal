#!/usr/bin/node
const a = parseInt(process.argv[2], 10);
if (isNaN(a)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + a);
}
