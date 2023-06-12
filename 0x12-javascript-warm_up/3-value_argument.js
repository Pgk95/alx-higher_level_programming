#!/usr/bin/node

const firstArgument = process.argv[2];

if (!firstArgument) {
  console.log('No argument');
} else if (process.argv.length === 3) {
  console.log(firstArgument);
}
