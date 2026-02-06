# LeetCode Problem: 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        left = 0
        count = 0
        curr_product = 1
        for right in range(len(nums)):
            curr_product *= nums[right]

            while curr_product >= k:
                curr_product //= nums[left]
                left += 1
            
            count += right - left + 1
        
        return count