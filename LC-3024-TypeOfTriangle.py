# LeetCode Problem: 3024. Type Of Triangle
# https://leetcode.com/problems/type-of-triangle/

from typing import List


class Solution:
    def triangleType(self, nums: List[int]) -> str:
        if nums[0] == nums[1] and nums[1] == nums[2]:
            return 'equilateral'
            
        if(nums[0] + nums[1] > nums[2] 
        and nums[0] + nums[2] > nums[1]
        and nums[1] + nums[2] > nums[0]):
            if nums[0] == nums[1] or nums[0] == nums[2] or nums[1] == nums[2]:
                return 'isosceles'
            else:
                return 'scalene'
        else:
            return 'none' 