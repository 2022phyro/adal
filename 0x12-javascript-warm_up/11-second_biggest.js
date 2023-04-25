#!/usr/bin/node
const lenght = process.argv.length;
if (lenght <= 3) {
  console.log(0);
} else {
  const numbers = [];
  for (let i = 2; i < lenght; i++) {
    const x = parseInt(process.argv[i], 10);
    numbers.push(x);
  }
  numbers.sort(function (a, b) { return b - a; });
  console.log(numbers[1]);
}
