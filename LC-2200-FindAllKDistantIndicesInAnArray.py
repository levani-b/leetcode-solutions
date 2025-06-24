# LeetCode Problem: 2200. Find All K-Distant Indices in an Array
# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/

from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        right = 0 
        n = len(nums)
        for j in range(n):
            if nums[j] == key:
                left = max(right, j - k)
                right = min(n - 1, j + k) + 1
                for i in range(left, right):
                    res.append(i)
        return res
            