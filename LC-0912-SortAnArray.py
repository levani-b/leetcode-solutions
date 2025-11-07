# LeetCode Problem: 912. Sort an Array
# https://leetcode.com/problems/sort-an-array/

from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge_sort(nums):
            if len(nums) < 2:
                return nums
            
            mid = len(nums) // 2
            left_side = nums[mid:]
            right_side = nums[:mid]

            left_side_merge = merge_sort(left_side)
            right_side_merge = merge_sort(right_side)

            return merge(left_side_merge, right_side_merge)
        
        def merge(left, right):
            sorted_nums = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    sorted_nums.append(left[i])
                    i+= 1 
                else:
                    sorted_nums.append(right[j])
                    j += 1
                
            while i < len(left):
                sorted_nums.append(left[i])
                i += 1
            
            while j < len(right):
                sorted_nums.append(right[j])
                j += 1
            return sorted_nums
        
        result = merge_sort(nums)
        return result