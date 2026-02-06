# LeetCode Problem: 3634. Minimum Removals to Balance Array
# https://leetcode.com/problems/minimum-removals-to-balance-array/

class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        max_to_keep = 0

        for r in range(len(nums)):
            
            while nums[r] > nums[l] * k:
                l += 1
            
            max_to_keep = max(max_to_keep, r - l + 1)
        
        return len(nums) - max_to_keep