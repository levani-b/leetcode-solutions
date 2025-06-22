# LeetCode Problem: 2138. Divide a String Into Groups of Size K
# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/

from typing import List


class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n = len(s)
        if n % k != 0:
            s += (k -(n % k)) * fill
        
        res = []
        for i in range(0,len(s),k):
            res.append(s[i:i+k])

        return res