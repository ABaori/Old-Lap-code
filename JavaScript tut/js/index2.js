/* var,let,const
var is for criable and vraible in javascript is like a container in which we can fil something using console log.
*/
var name = 'harry';
console.log(name)
console.log('hi');
//variables can be initialised
var ciy;
console.log(name,ciy);
/* rules 
1) cannot start with no.
2) can start with letter,number, _ or $
3) are case sensitive
*/
name = 'arrav';
console.log(name);

const owner = 'aarav';
//owner = 'sahil';
//cant do that
//local and global variable

{
    let name = 'sahil';
    console.log(name);
    //here name is loval variable and let is block level function
}
{
    let owner = 'sahil';
    console.log(owner);
}
{
    //var owner = 'sahil';
    //not working
}
