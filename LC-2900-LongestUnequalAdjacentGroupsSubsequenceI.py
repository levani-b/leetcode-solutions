# LeetCode Problem: 2900. Longest Unequal Adjacent Groups Subsequence I
# https://leetcode.com/problems/longest-unequal-adjacent-groups-subsequence-i/

from typing import List


def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        if not words:
            return []

        res = [words[0]]
        last_g = groups[0]
        for i in range(1,len(words)):
            if groups[i] != last_g:
                res.append(words[i])
                last_g = groups[i]
        return res
