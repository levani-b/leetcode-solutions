# LeetCode Problem: 3880. Minimum Absolute Difference Between Two Values
# https://leetcode.com/problems/minimum-absolute-difference-between-two-values/

class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        last1 = -1
        last2 = -1
        min_diff = float('inf')
        
        for i, num in enumerate(nums):
            if num == 1:
                last1 = i
                if last2 != -1:
                    min_diff = min(min_diff, abs(last1 - last2))
            elif num == 2:
                last2 = i
                if last1 != -1:
                    min_diff = min(min_diff, abs(last1 - last2))

        if min_diff != float('inf'):
            return min_diff
        else:
            return -1
             