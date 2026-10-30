# LeetCode Problem: 442. Find All Duplicates In An Array
# https://leetcode.com/problems/find-all-duplicates-in-an-array/

class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        res = []
        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                res.append(idx + 1)
            else:
                nums[idx] = -abs(nums[idx])
        
        return res
