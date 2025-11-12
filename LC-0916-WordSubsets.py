# LeetCode Problem: 916. Word Subsets
# https://leetcode.com/problems/word-subsets/

from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        words1_dict = {}
        for word in words1:
            char_count = {}
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            words1_dict[word] = char_count

        
        freq_words2 = {}
        for word in words2:
            char_count = {}
            for char in word:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            
            for char, count in char_count.items():
                if char not in freq_words2 or count > freq_words2[char]:
                    freq_words2[char] = count
        
        res = []
        for word, char_count in words1_dict.items():
            is_universal = True
            for char, required_count in freq_words2.items():
                if char not in char_count or char_count[char] < required_count:
                    is_universal = False
                    break
            
            if is_universal:
                res.append(word)
        
        return res