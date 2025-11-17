# LeetCode Problem: 1437. Check if All 1's are at Least Length K Places Away
# https://leetcode.com/problems/check-if-all-1s-are-at-least-length-k-places-away/

from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zeros = k
        
        for num in nums:
            if num == 1:
                if zeros < k: 
                    return False
                zeros = 0  
            else:
                zeros += 1 
        
        return True         
                
