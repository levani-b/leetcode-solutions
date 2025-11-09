# LeetCode Problem: 3740. Minimum Distance Between Three Equal Elements I
# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/

from typing import List


class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        hashmap = {}
        for index, number in enumerate(nums):
            if number not in hashmap:
                hashmap[number] = []
            hashmap[number].append(index)
        
        min_distance = float('inf')
        
        for num, indices in hashmap.items():
            if len(indices) >= 3:
                for i in range(len(indices) - 2):
                    for j in range(i + 1, len(indices) - 1):
                        for k in range(j + 1, len(indices)):
                            dist1 = abs(indices[i] - indices[j])
                            dist2 = abs(indices[j] - indices[k])
                            dist3 = abs(indices[i] - indices[k])
                            dist = dist1 + dist2 + dist3
                            
                            min_distance = min(min_distance, dist)
        
        return min_distance if min_distance != float('inf') else -1