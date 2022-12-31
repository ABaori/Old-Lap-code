console.log('lets begin');
let arr = ['bengan','palak','gobi','paneer'];
//u cannot directly diplay array over there

//addin key and vealue in local storage
localStorage.setItem('country' , 'singapore');
localStorage.setItem('country2' , 'india');
localStorage.setItem('sabzi', JSON.stringify(arr));

//retrieving item from local storage
let country = localStorage.getItem('country');

country = localStorage.getItem('sabzi');
console.log(country);
//its still string
country = JSON.parse(localStorage.getItem('sabzi'));
console.log(country);
//Now its an array


//to clear local storage
// localStorage.clear();
// localStorage.removeItem('country');

localStorage.setItem('sessioncountry' , 'singapore');
localStorage.setItem('sessioncountry2' , 'india');
localStorage.setItem('sessionsabzi', JSON.stringify(arr));
//session storage is temporary local storage is permanent.