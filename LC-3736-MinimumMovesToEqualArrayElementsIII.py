# LeetCode Problem: 3736. Minimum Moves to Equal Array Elements III
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        max_num = max(nums)
        moves = 0
        for num in nums:
            moves += max_num - num
        
        return moves
