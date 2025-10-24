# LeetCode Problem: 1913. Maximum Product Difference Between Two Pairs
# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        max1 = max2 = 0
        min1 = min2 = float('inf')

        for num in nums:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
            if num < min1:
                min1, min2 = num, min1
            elif num < min2:
                min2 = num

        return (max1 * max2) - (min1 * min2)