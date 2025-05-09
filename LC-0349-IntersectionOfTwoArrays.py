# LeetCode Problem: 349. Intersection Of Two Arrays
# https://leetcode.com/problems/intersection-of-two-arrays/

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        for num in nums1:
            if num in nums2 and num not in res:
                res.append(num)
            
        return res