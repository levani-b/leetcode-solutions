# LeetCode Problem: 1089. Duplicate Zeros
# https://leetcode.com/problems/duplicate-zeros/

from typing import List


class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        for i in range(len(arr) -1, -1, -1):
            if arr[i] == 0:
                arr.insert(i+1, 0)
                count += 1
        if count > 0:
            arr[:] = arr[:-count]
        
            

       