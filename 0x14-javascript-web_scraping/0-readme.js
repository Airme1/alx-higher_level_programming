#!/usr/bin/node
// Script to read and print file 

let fs = require('fs');
const file = process.argv[2];

fs.readFile(file, 'utf-8', (error, data) =>
	{
		if(error){
			console.log(error);
		}
		else{
			console.log(data);
		}
	}
);
