#!/usr/bin/node
const { argv } = require('process');

if (argv.length <= 2) {
  console.log('0');
} else {
  let big = 0;
  let bigger = 0;
  for (let i = 2; i < argv.length; i++) {
    if (argv[i] > bigger) {
      bigger = argv[i];
    }
    if (argv[i] > big && argv[i] < bigger) {
      big = argv[i];
    }
  }
  console.log(big);
}
