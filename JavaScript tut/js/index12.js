console.log('lets begin');
let a = window;
console.log(a);

console.log('crawler ex 1 soln');
let b = "code";
a = document.links;
let href;
Array.from(a).forEach(function(element) {
    href = element.href;
    if(href.includes(b)){
        console.log(href);
    }
});