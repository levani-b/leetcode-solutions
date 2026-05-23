# LeetCode Problem: 1752. Check if Array Is Sorted and Rotated
# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/

from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                count += 1
                if count == 2:
                    return False
            
        if nums[-1] > nums[0]:
            count += 1

        return count <= 1
    

class Solution:
    def check(self, nums: List[int]) -> bool:
        nums_sorted = sorted(nums)

        res = []
        for i in range(len(nums)-1):
            if nums[i] > nums[i + 1]:
                res += nums[i+1:]
                break
        
        for num in nums:
            res.append(num)
            if res == nums_sorted:
                return True
        
        return False