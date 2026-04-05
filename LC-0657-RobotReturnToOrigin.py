# LeetCode Problem: 657. Robot Return To Origin
# https://leetcode.com/problems/robot-return-to-origin/

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        starter = [0,0]

        for move in moves:
            if move == 'U':
                starter[1] += 1
            elif move == 'D':
                starter[1] -= 1
            elif move == 'R':
                starter[0] += 1
            else:
                starter[0] -= 1
        
        return starter == [0,0]