# LeetCode Problem: 2913. Subarrays Distinct Element Sum Of Squares I
# https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-i/

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        sum_count = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums) + 1):
                sum_count += len(set(nums[i:j])) ** 2
        
        return sum_count
        
        