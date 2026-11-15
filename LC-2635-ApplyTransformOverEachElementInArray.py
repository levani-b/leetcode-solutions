# LeetCode Problem: 2635. Apply Transform Over Each Element in Array
# https://leetcode.com/problems/apply-transform-over-each-element-in-array/

/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var map = function(arr, fn) {
    new_arr = []
    for(let i = 0; i < arr.length; i++){
        new_arr.push(fn(arr[i], i))
    }
    return new_arr
};
