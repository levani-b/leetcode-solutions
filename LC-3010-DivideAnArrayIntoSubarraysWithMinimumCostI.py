# LeetCode Problem: 3010. Divide an Array Into Subarrays With Minimum Cost I
# https://leetcode.com/problems/divide-an-array-into-subarrays-with-minimum-cost-i/

class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)
        

        min_sum = nums[0]

        min1 = float('inf')
        min2 = float('inf')

        for i in range(1,len(nums)):
            if nums[i] < min1:
                min2 = min1
                min1 = nums[i]
            elif nums[i] < min2:
                min2 = nums[i]

        return min_sum + min1 + min2