# LeetCode Problem: 167. Two Sum II  Input Array is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1,r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1