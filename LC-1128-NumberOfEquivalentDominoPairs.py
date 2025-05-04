# LeetCode Problem: 1128. Number Of Equivalent Domino Pairs
# https://leetcode.com/problems/number-of-equivalent-domino-pairs/

from typing import List


def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        hashT = {}
        for a,b in dominoes:
            key = tuple(sorted((a,b)))
            if key in hashT:
                hashT[key] += 1
            else:
                hashT[key] = 1
        
        count = 0
        for val in hashT.values():
            count += val*(val-1) // 2
        return count