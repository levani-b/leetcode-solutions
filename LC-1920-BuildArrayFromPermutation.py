# LeetCode Problem: 1920. Build Array From Permutation
# https://leetcode.com/problems/build-array-from-permutation/

from typing import List


def buildArray(nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            res.append(nums[nums[i]])
        return res