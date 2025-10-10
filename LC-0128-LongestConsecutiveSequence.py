# LeetCode Problem: 128. Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for num in numset:
            if num - 1 not in numset:
                length = 1
                while num + length in numset:
                    length += 1
                longest = max(length, longest)
        return longest
            