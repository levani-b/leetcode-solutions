# LeetCode Problem: 1498. Number of Subsequences That Satisfy the Given Sum Condition
# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD = 10**9 + 7
        nums.sort()

        l = 0
        r = len(nums) - 1
        count = 0
        
        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else :
                count = (count + pow(2, r - l, MOD)) % MOD
                l += 1
        return count
             