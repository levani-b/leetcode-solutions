# LeetCode Problem: 796. Rotate String
# https://leetcode.com/problems/rotate-string/

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        ss = s * 2
        if len(s) == len(goal) and goal in ss:
            return True
        return False

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s == goal:
            return True

        s = list(s)
        goal = list(goal)
        
        for i in range(len(s)):
            s.insert(0, s.pop())
            if s == goal:
                return True
        
        return False