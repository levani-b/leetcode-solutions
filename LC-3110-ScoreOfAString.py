# LeetCode Problem: 3110. Score Of A String
# https://leetcode.com/problems/score-of-a-string/

def scoreOfString(self, s: str) -> int:
    ascii_arr = []
    for char in s:
        ascii_arr.append(ord(char))
    
    res = 0
    for i in range(len(ascii_arr) -1):
        num = abs(ascii_arr[i] - ascii_arr[i+1])
        res += num
    return res