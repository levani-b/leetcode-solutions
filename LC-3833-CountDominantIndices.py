# LeetCode Problem: 3833. Count Dominant Indices
# https://leetcode.com/problems/count-dominant-indices/

class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        
        for i in range(n - 1):
            right_sum = sum(nums[i + 1:])
            right_count = n - i - 1
            
            if nums[i] * right_count > right_sum:
                count += 1
        
        return count

