# LeetCode Problem: 925. Long Pressed Name
# https://leetcode.com/problems/long-pressed-name/

class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if not name or not typed:
            return name == typed
        
        if name[-1] != typed[-1]:
            return False
        
        n = 0
        t = 0

        while n < len(name) and t < len(typed):
            if name[n] == typed[t]:
                t += 1
                n += 1
            elif t > 0 and typed[t] == typed[t - 1]:
                t += 1
            else:
                return False
        
        if n < len(name):
            return False
        
        while t < len(typed):
            if typed[t] != typed[t - 1]:
                return False
            t += 1
        return True
