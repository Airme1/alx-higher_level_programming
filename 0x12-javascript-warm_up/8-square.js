#!/usr/bin/node

const {argv} = require('node:process');

if(!parseInt(argv[2])){
	console.log("Missing size");
}else{
	let num = parseInt(argv[2]);
	//Printing a square of X's
	for(let i = 0; i < num.length; i++){
		for(let j = 0; j < num.length; j++){
			console.log("X");
		}
	}
}
