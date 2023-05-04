function linear_search(array, num){
    for (let i = 0; i < array.length; i++) {
       if(array[i] === num){
        return true;
        }
    
    }
    return false;
}

const arr1 = [1,2,3,4,5,6];

console.log(linear_search(arr1, 4));
  
console.log(linear_search(arr1, 7));