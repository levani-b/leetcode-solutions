# LeetCode Problem: 1502. Can Make Arithmetic Progression From Sequence
# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/

from typing import List


class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return True
        
        min_val = min(arr)
        max_val = max(arr)
        n = len(arr)
        
        if (max_val - min_val) % (n - 1) != 0:
            return False
        
        diff = (max_val - min_val) // (n - 1)
        
        if diff == 0:
            return True
        
        seen = set()
        for num in arr:
            if (num - min_val) % diff != 0:
                return False
            
            if num in seen:
                return False
            seen.add(num)
        
        return True