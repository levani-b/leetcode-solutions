# LeetCode Problem: 1929. Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums) * 2
        for i in range(len(nums)):
            ans[i] = nums[i]
            ans[i + len(nums)] = nums[i]
        
        return ans



# def getConcatenation(nums):
#         result = []
#         for _ in range(2):
#             for num in nums:
#                 result.append(num)
#         return result