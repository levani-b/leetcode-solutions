# LeetCode Problem: 724. Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = 0
        left_sum = 0

        for num in nums:
            total += num
        
        for i, num in enumerate(nums):
            right_sum = total - left_sum - num
            if left_sum == right_sum:
                return i
            left_sum += num
        
        return -1