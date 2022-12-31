console.log('lets begin');
let element = document.createElement('li');
console.log(element);
let text = document.createTextNode('I am a text node');
//Adding classname to li
element.className = 'childul';
element.id = 'createdLi';
element.setAttribute('title' , 'myTiltle');
// element.innerHTML = '<b>this is text</b>';
let ul = document.querySelector('ul.this');
console.log(ul)
ul.appendChild(element);
element.appendChild(text);

// let elem2 = document.createElement('h3');
// elem2.id = 'elem2';
// elem2.className = 'elem2';
// let Tnode = document.createTextNode('this is a text node');
// elem2.appendChild(Tnode);
// element.replaceWith(elem2);

let myul = document.getElementById('myul');
console.log(myul);
myul.replaceChild(element, document.getElementById('fui'));
myul.removeChild(element);

// element.removeAttribute('id');
// element.removeAttribute('class');
let pr = element.hasAttribute('class');
console.log(pr);
//excersise
let elem3 = document.createElement('h1')
elem3.innerText = 'Go to codewithharry.com';
console.log(elem3);
let x = document.querySelector('div.container');
x.appendChild(elem3);
let a = document.createElement('a')
a.setAttribute('href' ,'//codewithharry.com');
a.innerText = 'www.codewithharry.com';
x.appendChild(a);