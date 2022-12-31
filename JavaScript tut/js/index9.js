console.log('lets begin');
let name = 'aarav';
// console.log(`“A wish for ${name} on your birthday, whatever you ask may you receive, whatever you seek may you find, whatever you wish may it be fulfilled on your birthday and always. Happy birthday!”`);
let name2 = 'satvik';
// console.log(`“A wish for ${name2} on your birthday, whatever you ask may you receive, whatever you seek may you find, whatever you wish may it be fulfilled on your birthday and always. Happy birthday!”`);
//this just gets lengthy

// FUNCTIONS 2 WAYS
function greet(name , Thank = 'Thank you'){
    console.log(`“A wish for ${name} on your birthday, whatever you ask may you receive, whatever you seek may you find, whatever you wish may it be fulfilled on your birthday and always. ${Thank}!”`);
  
}

const mygreeting = function(name , Thank){
    console.log(`“A wish for ${name} on your birthday, whatever you ask may you receive, whatever you seek may you find, whatever you wish may it be fulfilled on your birthday and always. ${Thank}!”`); 
}
// Function defiined
 greet(name);
 mygreeting(name,'thank you');
//Function called

//function statement
/* function name(params) {
     console.log()
 }*/

 function greeting(name){
    let msg = `“A wish for ${name} on your birthday, whatever you ask may you receive, whatever you seek may you find, whatever you wish may it be fulfilled on your birthday and always. Happy birthday!”`;
  return msg;
}

let val = greeting(name);
console.log(val);

const myobj = {
    name: 'aarav',
    age: 1,
    game: function(){
return "GTA";
    }
}
console.log(myobj.game());

arr = ['furits','vegetables','apple'];
arr.forEach(function(element,index,array){
console.log(element,index,array);
    
});
function ui(name){
    let i = 9;
    console.log(i);
return `this is a ${name} ui`;
}
