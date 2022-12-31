console.log('lets begin');
/* DOM selectors
1) single element selector
2) multi element selector
*/
let element = document.getElementById("myfirst");
// element = element.className;
// element = element.childNodes;
// element = element.parentNode;
// element.style.color = 'blue';
// element.innerText = 'aarav is smart';
element.innerHTML = '<form type = "text"></form>';
console.log(element);

let sel = document.querySelector("#myfirst");
 sel = document.querySelector(".child");
 sel = document.querySelector("div")
 //its not seleceting the dummy div


console.log(sel);

//2)Multi element seelctor
let elems = document.getElementsByClassName('child');
console.log(elems[0]);
console.log(elems[1]);
console.log(elems[3]);

elems = document.getElementsByClassName('container');
console.log(elems[0].getElementsByClassName('red'));

elems = document.getElementsByTagName('div');
console.log(elems[1]);
console.log(elems[2]);
console.log(elems[3]);
console.log(elems[4]);
console.log(elems[5]);

Array.from(elems).forEach(function(element){
    console.log(element);
    element.style.color = 'red';
})
// for ease of work for each loop can be used


