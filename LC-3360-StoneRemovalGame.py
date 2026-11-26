# LeetCode Problem: 3360. Stone Removal Game
# https://leetcode.com/problems/stone-removal-game/

class Solution:
    def canAliceWin(self, n: int) -> bool:
        if n < 10:
            return False
        n = n - 10
        stones = 9
        a = 1
        b = 0
        while n >= stones:
            n -= stones
            stones -= 1
            if a != b:
                b += 1
            else:
                a += 1
        
        return a != b
