# LeetCode Problem: 14. Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/

from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res