#!/usr/bin/node

const {argv} = require('node:process');

if (! parseInt(argv[2])){
	console.log("Missing number of occurrences");
} else{
	let num = parseInt(argv[2]);
	for(let i = 0; i < num.length; i++){
		console.log("C is fun");
	}
}
