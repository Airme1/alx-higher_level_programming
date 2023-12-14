#!/usr/bin/node
const { argv } = require('process');

function add (a, b) {
  a = parseInt(a);
  b = parseInt(b);
  const sum = a + b;
  console.log(sum);
}

add(argv[2], argv[3]);
