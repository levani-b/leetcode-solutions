# LeetCode Problem: 3745. Maximize Expression of Three Elements
# https://leetcode.com/problems/maximize-expression-of-three-elements/

from typing import List


class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:
        max_a = float('-inf')
        max_b = float('-inf')
        min_c = float('inf')

        for num in nums:
            if num < min_c:
                min_c = num
                
            if num > max_a:
                max_b = max_a
                max_a = num
            elif num > max_b:
                max_b = num
        return max_a + max_b - min_c