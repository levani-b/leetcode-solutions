# LeetCode Problem: 58. Length Of Last Word
# https://leetcode.com/problems/length-of-last-word/

def lengthOfLastWord(self, s: str) -> int:
    length = 0
    i = len(s) - 1

    while s[i] == ' ':
        i -= 1
    while i >= 0 and s[i] != ' ':
        length += 1
        i -= 1
    return length




# def lengthOfLastWord(self, s: str) -> int:
#         s_arr = s.strip().split()
#         return len(s_arr[-1])
