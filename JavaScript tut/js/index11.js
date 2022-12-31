console.log('lets begin');
let a = document;
a = document.all;
/*Array.from(a).forEach(function(element){
    console.log(element);
});*/


//a is not a array thats why we have to make the values in a as array
//Array.from

a = document.images[0];
a = document.all;
// a.forEach(function(element){
//     console.log(element);
// })
// it  doesnt work since a is not an object
Array.from(a).forEach(function(element){
    console.log(element);
})
a = window;
console.log(typeof a);
