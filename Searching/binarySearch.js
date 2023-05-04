function binarySearch(arr, num){
    let lo = 0;
    let hi = arr.length;
    do {
        const mid = Math.floor(lo +(hi - lo)/2);
        const val = arr[mid];

        if(val === num){
            return true;
        }else if(val > num){
            hi = mid;
        }else{
            lo = mid + 1;
        }
    } while (lo <hi);
    return false;
}