# LeetCode Problem: 3701. Compute Alternating Sum
# https://leetcode.com/problems/compute-alternating-sum/

class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        alt_sum = 0
        for i in range(len(nums)):
            if i % 2 == 1:
                alt_sum -= nums[i]
            else:
                alt_sum += nums[i]
        
        return alt_sum