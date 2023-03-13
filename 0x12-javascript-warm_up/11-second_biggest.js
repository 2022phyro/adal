#!/usr/bin/node
process = require('node:process');
lenght = process.argv.length;
// function max(array) {
//   let maxx = array[0];
//   for (let i = 0; i < array.length; i++) {
//     if (array[i] > maxx) {
//         maxx = array[i];
//     }
//   }
//   return (maxx)
// }
if (lenght < 3) {
  console.log(0);
} else {
  const numbers = [];
  for (let i = 2; i < lenght; i++) {
    x = parseInt(process.argv[i], 10);
    numbers.push(x);
  }
  numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
}
