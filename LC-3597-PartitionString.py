# LeetCode Problem: 3597. Partition String
# https://leetcode.com/problems/partition-string/

from typing import List


class Solution:
    def partitionString(self, s: str) -> List[str]:
        res = []
        seen = set()
        curr = ''

        for char in s:
            curr += char
            if curr not in seen:
                res.append(curr)
                seen.add(curr)
                curr = ''
            
        return res

