# LeetCode Problem: 1007. Minimum Domino Rotations For Equal Row
# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

from typing import List


def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rotate_top, rotate_bottom = 0, 0
            for i in range(len(tops)):
                if tops[i] !=x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rotate_top += 1
                elif bottoms[i] != x:
                    rotate_bottom += 1
            return min(rotate_bottom,rotate_top)
        
        for x in range(1,7):
            res = check(x)
            if res != -1:
                return res
        return -1