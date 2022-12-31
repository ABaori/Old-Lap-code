console.log('lets begin');
const age = 65;

//IF ELSE

if(age==19){
    console.log('age is 19');
}
else{
    console.log('age is not 19');
}
//'==' used for comparison

//  IF ELSE IF

if(age!=19){
    console.log('age is not 19');
}
else if(age==65){
    console.log('age is 65');
}
else{
    console.log('age is not 19');
}
//'!=' means not same

let vari = 15
if(typeof vari != undefined){
    console.log('vari is defined');
}
else{
    console.log('vari is undefined');
}

let doesdrive = false;
if(typeof doesdrive == true && age>18){
    console.log('you can drive');
}
else{
    console.log('you cant drive');
}
//&& and opertaor
if(typeof doesdrive == true || age>18){
    console.log('you can drive');
}
else{
    console.log('you cant drive');
}
//|| or operator

//ternary operator
console.log(age==65? 'age is 65' : 'age is not 65');
// frist true condition then false condition

switch (age) {
    case 18:
        console.log('your 18');
        break;
    case 28:
    console.log('your 28');
        break;
    case 65:
        console.log('your 65');
        break;
    default:
        console.log('Your human');
        break;
}