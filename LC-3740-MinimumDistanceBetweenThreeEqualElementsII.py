# LeetCode Problem: 3740. Minimum Distance Between Three Equal Elements II
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-ii/

from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashmap = {}
        
        for index, number in enumerate(nums):
            if number not in hashmap:
                hashmap[number] = []
            hashmap[number].append(index)
        
        min_distance = float('inf')
        
        for indices in hashmap.values():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    k = i + 2
                    distance = 2 * (indices[k] - indices[i])
                    min_distance = min(distance, min_distance)
        
        return min_distance if min_distance != float('inf') else -1