# LeetCode Problem: 453. Minimum Moves To Equal Array Elements
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

class Solution:
    def minMoves(self, nums: list[int]) -> int:
        min_num = min(nums)
        moves = 0
        for num in nums:
            moves += num - min_num
        
        return moves

