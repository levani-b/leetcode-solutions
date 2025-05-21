# LeetCode Problem: 448. Find All Numbers Disappeared In An Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        res = []
        for num in range(1,n+1):
            if num not in num_set:
                res.append(num)
        return res