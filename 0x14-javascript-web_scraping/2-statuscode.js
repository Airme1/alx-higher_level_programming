#!/usr/bin/node
//Script to display status code of GET request
const request = require('request');
const url = process.argv[2];

request.get(url, (error, response) => {
  if (error) {
    console.log(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});