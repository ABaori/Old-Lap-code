//TYPR CONVERSION

console.log('lets begin');
let myVr = 34
console.log(myVr,typeof myVr);
myVr = String(34);
console.log(myVr,typeof myVr);

let booleanVr = true;
console.log(booleanVr , typeof booleanVr);
booleanVr = String(true);
console.log(booleanVr,typeof booleanVr);

let date = new Date();
console.log(date , typeof date);
date = String(new Date());
console.log(date, typeof date);

let arr = [1,2,3,4,'a',5];
console.log(arr , typeof arr);
console.log(arr.length);
arr = String([1,2,3,4,'a',5]);
console.log(arr , typeof arr);
console.log(arr.length);

let a = 1;
console.log(a.toString());
console.log(a,typeof a)

let str1 = "729";
console.log(str1 , typeof str1);
str1 = Number("729");
console.log(str1, typeof str1);
str1 = Number(true);
console.log(str1 , typeof str1);


let str2;
str2 = '69.69';
console.log(str2,typeof str2);
str2 = Number('69.69');
console.log(str2 , typeof str2);
str2 = Number('69.69abc');
console.log(str2 , typeof str2);
str2 = parseFloat('69.69aaaa');
console.log(str2);

console.log(str2.toFixed(4) , typeof str2);

//TYPE COERCION

let num1;
let num2;
num1 = "648";
num2 = 34;
console.log(num1+num2);
//so in this case js converts the number into string and then joins it
num1 = Number("648");
console.log(num1 + num2);
