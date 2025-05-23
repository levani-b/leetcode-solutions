# LeetCode Problem: 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

def mergeAlternately(word1: str, word2: str) -> str:
    res = ''
    i,j = 0,0
    while i < len(word1) and j < len(word2):
        res += word1[i] + word2[j]  
        i += 1
        j += 1
    res += word1[i:] +word2[j:] 
    return res