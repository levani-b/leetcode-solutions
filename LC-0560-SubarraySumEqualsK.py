# LeetCode Problem: 560. Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref_sums = {0 : 1}
        count = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum - k in pref_sums:
                count += pref_sums[curr_sum - k]
            
            if curr_sum in pref_sums:
                pref_sums[curr_sum] += 1
            else:
                pref_sums[curr_sum] = 1
        
        return count