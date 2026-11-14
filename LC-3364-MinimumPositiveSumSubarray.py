# LeetCode Problem: 3364. Minimum Positive Sum Subarray
# https://leetcode.com/problems/minimum-positive-sum-subarray/

class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        min_sum = float('inf')

        for size in range(l, r + 1):
            for i in range(len(nums) - size + 1):
                subarray_sum = sum(nums[i:i + size])

                if 0 < subarray_sum < min_sum:
                    min_sum = subarray_sum

        return min_sum if min_sum != float('inf') else -1
