# LeetCode Problem: 3190. Find Minimum Operations To Make All Elements Divisible By Three
# https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

from typing import List


def minimumOperations(nums: List[int]) -> int:
        count = 0 
        for num in nums: 
            if num % 3 != 0: 
                count += 1 
        return count 