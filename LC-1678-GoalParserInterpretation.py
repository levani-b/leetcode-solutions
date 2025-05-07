# LeetCode Problem: 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

def interpret(command: str) -> str:
        res = ''
        for i in range(len(command)):
            if command[i] == 'G':
                res += 'G'
            if command[i] == '(' and command[i + 1] ==')':
                res += 'o'
            if command[i] == '(' and command[i + 1] == 'a':
                res += 'al'
                
        return res