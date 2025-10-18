# LeetCode Problem: 896. Monotonic Array
# https://leetcode.com/problems/monotonic-array/

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = False
        if nums[0] < nums[-1]:
            increasing = True
        
        if increasing:
            for i in range(len(nums) - 1):
                if nums[i] > nums[i + 1]:
                    return False
            return True
        else:
            for i in range(len(nums) -1):
                if nums[i] < nums[i+1]:
                    return False
            return True