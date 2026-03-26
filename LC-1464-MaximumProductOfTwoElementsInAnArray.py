# LeetCode Problem: 1464. Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max = float('-inf')
        second_max = float('-inf')

        for num in nums:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        return (first_max - 1) * (second_max - 1)


# class Solution:
#     def maxProduct(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         return (nums[n-1] -1) * (nums[n-2] -1)