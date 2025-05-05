# LeetCode Problem: 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    hashL = {}
    hashT = {}

    for i in range(len(s)):
        if s[i] in hashL:
            hashL[s[i]] += 1
        else:
            hashL[s[i]] = 1
        
        if t[i] in hashT:
            hashT[t[i]] += 1
        else:
            hashT[t[i]] = 1
    
    return hashL == hashT

