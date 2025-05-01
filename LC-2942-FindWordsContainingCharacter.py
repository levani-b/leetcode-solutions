# LeetCode Problem: 2942. Find Words Containing Character
# https://leetcode.com/problems/find-words-containing-character/

from typing import List


def findWordsContaining(words: List[str], x: str) -> List[int]:
    res = []
    for i in range(len(words)):
        if x in words[i]:
            res.append(i)

    return res