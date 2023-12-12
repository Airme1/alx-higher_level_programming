#!/usr/bin/node
const {argv} = require('node:process');

function add(a, b){
	a = parseInt(a);
	b = parseInt(b);
	let sum = a + b;
	console.log(sum);
}

add(argv[2], argv[3]);
