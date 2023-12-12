#!/usr/bin/node

const { argv } = require('node:process');

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  const sum = a + b;
  console.log(sum);
}

if (!argv[2] && !argv[3]) {
  console.log('NaN');
} else {
  add(argv[2], argv[3]);
}
