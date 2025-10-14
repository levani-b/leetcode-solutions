# LeetCode Problem: 3349. Adjacent Increasing Subarrays Detection I
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def is_increasing(start, length):
            for j in range(start, start + length - 1):
                if nums[j] >= nums[j + 1]:
                    return False
            return True
        
        for i in range(len(nums) - 2*k + 1):
            if is_increasing(i, k) and is_increasing(i+k,k):
                return True
        return False