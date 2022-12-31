console.log('lets begin');

// Gneral looops : fro , while , do while
// for (let index = 0; index < array.length; index++) {
//     const element = array[index];
    
// }

// for(let i=0;i<=10 ; i++){
//     console.log(i);
// }

// while (condition) {
    
// }
let j= 0;
while(j<10){
    
    console.log(j+1);
 j+=1;
}

// do {
    
// } while (condition);
let k = 0
do{
    console.log(k+1);
    k+=1;
    if(k==5){
        break;
    }
}while(k<10)
// break and continue

let arr = [1,2,3,4,5,6,7,8];
for(let i =0 ; i<arr.length ; i++){
    const element = arr[i];
    console.log(element);
}

//another method

arr.forEach(function(element){
    console.log(element);
})

let obj ={
    name: "aarav",
    age: 15,
    class: 11,
    likes: "maths"
}
for(let key in obj){
    console.log(`the ${key} of object is ${obj[key]}`);
}