# LeetCode Problem: 3131. Find The Integer Added To Array I
# https://leetcode.com/problems/find-the-integer-added-to-array-i/

from typing import List


def addedInteger(nums1: List[int], nums2: List[int]) -> int:
    n = len(nums1)
    sum1 = 0
    sum2 = 0

    for num in nums1:
        sum1 += num

    for num in nums2:
        sum2 += num
    
    return (sum2-sum1)//n