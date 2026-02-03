# LeetCode Problem: 3637. Trionic Array I
# https://leetcode.com/problems/trionic-array-i/

class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        i = 1
        
        while i < len(nums) and nums[i - 1] < nums[i]:
            i += 1
        increasing_end = i

        while i < len(nums) and nums[i - 1] > nums[i]:
           i += 1
        decreasing_end = i

        while i < len(nums) and nums[i - 1] < nums[i]:
            i += 1
        
        return (i == len(nums) and increasing_end > 1 and increasing_end < decreasing_end and i > decreasing_end)