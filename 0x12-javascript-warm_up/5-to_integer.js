#!/usr/bin/node

const firstArgument = process.argv[2];
const parsedInt = parseInt(firstArgument);

if (!isNaN(parsedInt)) {
  console.log(`My number: ${parsedInt}`);
} else {
  console.log('Not a number');
}
