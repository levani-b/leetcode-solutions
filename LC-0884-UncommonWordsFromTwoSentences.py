# LeetCode Problem: 884. Uncommon Words From Two Sentences
# https://leetcode.com/problems/uncommon-words-from-two-sentences/

from typing import List


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list = s1.split()
        s2_list = s2.split()

        freq = {}
        for word in (s1_list + s2_list):
            if word in freq:
                freq[word] += 1
            else:
                freq[word] = 1
        
        res = []
        for word, count in freq.items():
            if count == 1:
                res.append(word)
        
        return res