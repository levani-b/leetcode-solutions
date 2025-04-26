# LeetCode Problem: 392. Is Subsequence
# https://leetcode.com/problems/is-subsequence/

def isSubsequence(self, s: str, t: str) -> bool:
    res = ''
    i,j = 0,0

    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            res += t[j]
            i += 1
        j+=1
    return res == s