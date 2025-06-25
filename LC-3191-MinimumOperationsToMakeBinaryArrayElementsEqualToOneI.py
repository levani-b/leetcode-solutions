# LeetCode Problem: 3191. Minimum Operations to Make Binary Array Elements Equal to One I
# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/

from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        operations = 0

        arr = nums[:]
        for i in range(n - 2): 
            if arr[i] == 0:  
                arr[i] = 1 - arr[i]    
                arr[i + 1] = 1 - arr[i + 1] 
                arr[i + 2] = 1 - arr[i + 2]  
                operations += 1
        

        if arr[n-1] == 0 or arr[n-2] == 0:
            return -1
        
        return operations