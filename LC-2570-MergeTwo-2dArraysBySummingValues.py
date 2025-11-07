# LeetCode Problem: 2570. Merge Two 2D Arrays By Summing Values
# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/

from typing import List


class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        i = 0
        j = 0
        res = []
        while i < len(nums1) and j < len(nums2):
            sum_val = 0
            if nums1[i][0] == nums2[j][0]:
                sum_val = nums1[i][1] + nums2[j][1]
                res.append([nums1[i][0], sum_val])
                i += 1
                j += 1
            elif nums1[i][0] < nums2[j][0]:
                res.append([nums1[i][0], nums1[i][1]])
                i += 1
            else:
                res.append([nums2[j][0], nums2[j][1]])
                j += 1
        
        while i < len(nums1):
            res.append(nums1[-1])
        
        while j < len(nums2):
            res.append(nums2[-1])
        return res