#!/usr/bin/node

const { argv } = require('process');

if (!parseInt(argv[2])) {
  console.log('Not a number:');
} else {
  console.log('My number: ' + argv[2]);
}
