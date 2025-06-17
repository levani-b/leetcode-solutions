# LeetCode Problem: 454. 4sum II
# https://leetcode.com/problems/4sum-ii/

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_map = {}
        
        for n1 in nums1:
            for n2 in nums2:
                sum1 = n1 + n2
                if sum1 in sum_map:
                    sum_map[sum1] += 1
                else:
                    sum_map[sum1] = 1
        
        count = 0

        for n3 in nums3:
            for n4 in nums4:
                sum2 = n3 + n4
                target = -sum2
                if target in sum_map:
                    count += sum_map[target]
        
        return count