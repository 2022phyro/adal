#!/usr/bin/node
const a = process.argv.length;
console.log(a === 2 ? 'No argument' : process.argv[2]);
