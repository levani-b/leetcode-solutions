# LeetCode Problem: 1528. Shuffle String
# https://leetcode.com/problems/shuffle-string/

from typing import List


def restoreString(self, s: str, indices: List[int]) -> str:
        res = [''] * len(s)
        for i in range(0, len(s)):
            res[indices[i]] = s[i]
        return ''.join(res)