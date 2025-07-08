# LeetCode Problem: 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
    
        def backtrack(start, current_combo, remaining_target):
            if remaining_target == 0:
                result.append(current_combo[:])
                return
            
            if remaining_target < 0:
                return
            
            for i in range(start, len(candidates)):
                candidate = candidates[i]
                current_combo.append(candidate)
                backtrack(i, current_combo, remaining_target - candidate)
                current_combo.pop()
        
        backtrack(0, [], target)
        return result