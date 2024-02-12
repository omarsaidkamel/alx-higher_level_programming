#!/usr/bin/node
// script that searches the second biggest integer in the list of arguments
const omar = process.argv;
if (omar.length <= 3) {
  console.log(0);
} else {
  console.log(omar.sort((x, y) => y - x).slice(3)[0]);
}i
