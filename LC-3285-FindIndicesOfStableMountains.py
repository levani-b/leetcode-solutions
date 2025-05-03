# LeetCode Problem: 3285. Find Indices Of Stable Mountains
# https://leetcode.com/problems/find-indices-of-stable-mountains/

from typing import List


def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        res = []
        for i in range(1,len(height)):
            if height[i-1]>threshold:
                res.append(i)
        return res