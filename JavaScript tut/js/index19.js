// console.log('lets begin');
//MY TRY
//  let editable = document.createElement('div');
//  editable.className = 'editable';
//  editable.innerHTML = ` hi`
// document.querySelector('div').appendChild(editable);
// localStorage.setItem(editable , editable.innerHTML)
// editable.addEventListener('click' , function(){
//    let x = document.querySelector('.txtarea').length;
//    if(x==0){
//    let html = editable.innerHTML;
//    editable.innerHTML= `<textarea class=' txtarea form-control'>${html}</textarea>`;
//    }
// })
console.log('This is tutorial 25')
/*
You have to create a div and inject it into the page which contains a heading.
whenever someone clicks on the div, it should be converted into an editable item. whenever user clicks away (blur). save the note into the local storage.

*/

// Create a new element
let divElem = document.createElement('div');

// Add text to that created element
let val = localStorage.getItem('text');
console.log(val);
let text;
if (val == null) {


   text = document.createTextNode('This is my element. click to edit it');
}
else {
   text = document.createTextNode(val);
}
divElem.appendChild(text);
// Give element id, style and class
divElem.setAttribute('id', 'elem');
divElem.setAttribute('class', 'elem');
divElem.setAttribute('style', 'border:2px solid black; width: 154px; margin: 34px; padding:23px;');

// Grab the main container
let container = document.querySelector('.container');
let first = document.getElementById('myfirst');


// Insert the element before element with id first
container.insertBefore(divElem, first);

console.log(divElem, container, first)

// add event listener to the divElem
divElem.addEventListener('click', function () {
   //doubt
   let noTextAreas = document.getElementsByClassName('textarea').length;
   if (noTextAreas == 0) {
      let html = divElem.innerHTML;
      divElem.innerHTML = ` <textarea class="textarea form-control" id="textarea" rows="3"> ${html}</textarea>`;
   }
   //listen for the blur event on textarea
   let textarea = document.getElementById('textarea');
   textarea.addEventListener('blur', function () {
      elem.innerHTML = textarea.value;
      localStorage.setItem('text', textarea.value);
   })
});
console.log("hello")
console.log("hello")
