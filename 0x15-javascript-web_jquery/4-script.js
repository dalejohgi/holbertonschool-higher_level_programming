#!/usr/bin/node
/*
updates the text color of the HTML tag HEADER
*/
$('#toggle_header').click(function () {
  $('header').toggleClass('red'); // remove or add the class depending on if the class exist or not
  $('header').toggleClass('green');
});
