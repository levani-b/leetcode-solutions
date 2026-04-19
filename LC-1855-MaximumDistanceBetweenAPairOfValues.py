# LeetCode Problem: 1855. Maximum Distance Between A Pair Of Values
# https://leetcode.com/problems/maximum-distance-between-a-pair-of-values/

class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        max_distance = 0

        while i < len(nums1) and j < len(nums2):
            if j < i:
                j = i
            elif nums1[i] <= nums2[j]:
                max_distance = max(max_distance,(j - i))
                j += 1
            elif nums1[i] > nums2[j]:
                i += 1
        
        return max_distance