# LeetCode Problem: 1652. Defuse the Bomb
# https://leetcode.com/problems/defuse-the-bomb/

from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        res = [0] * n
        
        if k == 0:
            return res
        
        if k > 0:
            win_sum = sum(code[1:k+1])
            res[0] = win_sum
            for i in range(1, n):
                win_sum -= code[i]
                win_sum += code[(i + k) % n]
                res[i] = win_sum

        if k < 0:
            k = abs(k)
            win_sum = sum(code[-k:])
            res[0] = win_sum
            for i in range(1,n):
                win_sum -= code[(i-1-k+n) % n]
                win_sum += code[i-1]
                res[i] = win_sum
        return res