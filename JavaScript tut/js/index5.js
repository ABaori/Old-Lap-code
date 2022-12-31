console.log("lets begin");
let name = 'Aarav';
let greeting = " Good morning";
console.log(name + ' ,' +greeting);
// html = "<h1> This is heading </h1>
// <p> this is paragraph </p>"
// so this does not work but we can use "+"
let html = "<h1> this is heading </h1>"+ 
"<p> this is paragraph </p>"
//  this becomes leangthy tho
// even concat function can be used

console.log(html);
html = html.concat('this', 'bot');
console.log(html);

// other functions

console.log(html.length);
console.log(html.toLowerCase());
console.log(html.toUpperCase());
//These changeing functions are temporary and only change inside a block

console.log(html[0]);
console.log(html[1]);
// gives the character at that index

console.log(html.indexOf('d'));
console.log(html.indexOf('>'));
console.log(html.indexOf('agiygaeughaegv'));
//gves the first apperence of the string given inside the indexOf  function

console.log(html.lastIndexOf('d'));
console.log(html.lastIndexOf('>'));
console.log(html.lastIndexOf('jyfssufavf'));
//Gives the last appearence of the index

console.log(html.charAt(6));
console.log(html.charAt(57));
//gives the charactr of the string present at the asked index

console.log(html.endsWith('str2'));
console.log(html.endsWith('bot'));
//returns a boolean output verifying whther thee gievn string in the function is with which the string in the variable ends with too

console.log(html.includes("b"));
//returns a boolean output which verifies whether the given character is present in the string of the variable

console.log(html.substring(0,30));
console.log(html.substring(0,10));
//returns the string from the given index to another given index

console.log(html.slice(-4));
console.log(html.slice(0,30));
// same as substring just it gives distinct output on negative values

console.log(html.split(' '));
console.log(html.split('<'));
//removes the character given and splits the string about it with commas

console.log(html.replace("this",'it'));
console.log(html.replace(">",'it'));
//replaces the first occurence of the given string with the desired string to replace it with

let fruit = ['or\'ange' , 'apple']
//backslash need to put single quotes in between
let myHml = `hello ${name}
       <h1>this i's heading</h1>
       <p>You like ${fruit[1]} and ${fruit[2]}          
`
document.body.innerHTML = myHml;
//  doubt in innerHTML
// we can easiy do this with baptix , with single quote we wud need to use concat multiple times. evan we can put single quotes in baptix inside whereas while using single quotes u need to use back slash
// Baptix waas introduced in the latest version of java script ES6
