# LeetCode Problem: 462. Minimum Moves To Equal Array Elements II
# https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/


class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        sorted_num = sorted(nums)
        mid = sorted_num[len(nums)// 2]
        moves = 0
        for num in nums:
            moves += abs(mid - num)
        return moves
