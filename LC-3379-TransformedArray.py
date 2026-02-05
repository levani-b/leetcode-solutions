# LeetCode Problem: 3379. Transformed Array
# https://leetcode.com/problems/transformed-array/

class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        result = [0] * len(nums)

        for i in range(len(nums)):
            if nums[i] > 0:
                step = (i + nums[i]) % len(nums)
                result[i] = nums[step]
            elif nums[i] < 0:
                step = (i - abs(nums[i])) % len(nums)
                result[i] = nums[step]
            else:
                result[i] = nums[i]
        
        return result
            