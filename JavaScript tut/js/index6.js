console.log('lets begin');
let marks = [56,64,69,72,75,80];
let fruits = ['grapes','apples' , 'banana' ,'watermelon'];
let mix = ["str1", 1,2,3, " bots", true];

const arr = new Array(1,2,3,5,"bye", true);
console.log(arr);
console.log(marks[0]);
console.log(fruits.length);
//length is a property 

console.log(Array.isArray(arr));
console.log(Array.isArray('arr'));
//these are method  and not property

fruits[0] = "muskmkelon";
console.log(fruits);
let varr = arr[0];
//we can equate any vriable with array element like this
console.log(marks);
let value = marks.indexOf(64);
console.log(value);
marks.push(57);
console.log(marks);
//push is method used to add an element to array at the end
marks.unshift(0);
console.log(marks);
//unshift is a method used to add element to start of the array

marks.pop();
console.log(marks);
//removes an element fron end of the array

marks.shift();
console.log(marks);
//removes one elemenet from the start

marks.splice(4);
console.log(marks);
marks.splice(-1);
console.log(marks);
marks.splice(1,2);
console.log(marks);
//gives the no. of element asked from the start of the array
let marks2 = [1,2,3,4];
marks = marks.concat(marks2);
console.log(marks);
//joins the given array with the ain array

//making objects
let myobj = {
    Name : 'aarav',
    school: 'apj',
    marks: [1,5,3,6]
}
console.log(myobj);
console.log(myobj.Name);
console.log(myobj['Name']);