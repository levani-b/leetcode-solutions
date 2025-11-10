# LeetCode Problem: 2215. Find The Difference Of Two Arrays
# https://leetcode.com/problems/find-the-difference-of-two-arrays/

from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        ans2 = []
        num1_set = set(nums1)
        num2_set = set(nums2)

        for num in num1_set:
            if num not in num2_set:
                ans1.append(num)
        
        for num in num2_set:
            if num not in num1_set:
                ans2.append(num)
        
        return [ans1,ans2]

        