# LeetCode Problem: 219. Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}
        for index, value in enumerate(nums):
            if value in hashmap and index - hashmap[value] <= k:
                return True
            else:
                hashmap[value] = index
        return False
