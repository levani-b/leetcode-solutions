function addUptToSecond(n){
    return n*(n+1)/2;
}

//more slower couse of many operations(depends on n);
//if n grows it need more time;
function addUpToFirst(n){
    let sum = 0;
    for (let i = 0; i < n; i++) {
        sum += 1;
    }
    return sum;
}

