# LeetCode Problem: 1441. Build an Array With Stack Operations
# https://leetcode.com/problems/build-an-array-with-stack-operations/

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        result = []
        current = 1 
        target_idx = 0  
        
        while target_idx < len(target):
            result.append("Push")
            
            if current == target[target_idx]:
                target_idx += 1
            else:
                result.append("Pop")
            
            current += 1
        
        return result