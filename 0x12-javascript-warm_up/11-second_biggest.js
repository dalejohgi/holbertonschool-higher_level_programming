#!/usr/bin/node
/*
Prints the second higher int argument
*/
let arguments = process.argv.slice(2);
if (arguments.length > 1){
  for(let i = 0; i < arguments.length; i++){
    arguments[i] = parseInt(arguments[i]);
  }
  arguments = arguments.sort();
  console.log(arguments.slice(-2)[0]);
} else {
  console.log(0)
}
