console.log('lets begin');
let cont = document.querySelector('.container');
console.log(cont.childNodes);
//here we can see that it aso gives us other child of div container which are not elements
// console.log(cont.children);
// console.log(cont.children[2]);
// cont = cont.childNodes[2].nodeName;
let nodetype = cont.childNodes[0].nodeType;
 nodetype = cont.childNodes[1].nodeType;
console.log(nodetype);
/* Types of nodeType
1) element : 1
2)Attribute : 2
3)text : 3
4)comment : 8
5)document : 9
6)docType : 10
*/
console.log(cont.children);
console.log(cont.children[1].children[0].children[4]);
//this is how you can traverse in DOM
console.log(cont.firstChild);
console.log(cont.firstElementChild);
console.log(cont.lastChild);
console.log(cont.lastElementChild);
console.log(cont.childElementCount);
console.log(cont.firstElementChild.parentNode);
console.log(cont.firstElementChild.nextSibling);
console.log(cont.firstElementChild.nextSibling.nextSibling);