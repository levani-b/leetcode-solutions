# LeetCode Problem: 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        l = 0
        r = len(nums) - 1
        pos = len(nums) - 1

        while l <= r:
            if nums[l] ** 2 > nums[r] ** 2:
                res[pos] = nums[l] ** 2
                l += 1
            else:
                res[pos] = nums[r] ** 2
                r -= 1
            pos -= 1

        return res
    
    
# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         res = []
#         l = 0
#         r = len(nums) - 1

#         while l <= r:
#             if nums[l] ** 2 > nums[r] ** 2:
#                 res.append(nums[l] ** 2)
#                 l += 1
#             else:
#                 res.append(nums[r] ** 2)
#                 r -= 1
        
#         return res[::-1]
