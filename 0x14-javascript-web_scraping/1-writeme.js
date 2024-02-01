#!/usr/bin/node
// Writing string to a file
const file = process.argv[2]
let fs = require('fs');
let content = process.argv[3]

fs.writeFile(file, content, "utf-8", (error) =>
	{
	if (error){
		console.log(error);
	}});
