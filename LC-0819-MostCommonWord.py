# LeetCode Problem: 819. Most Common Word
# https://leetcode.com/problems/most-common-word/

from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for ch in "!?',;.":
            paragraph = paragraph.replace(ch, " ")
        paragraph = paragraph.lower()
        
        paragraph_list = paragraph.split()
        par_dict = {}
        for word in paragraph_list:
            new_word = word.lower()
            if new_word not in banned:
                if new_word in par_dict:
                    par_dict[new_word] += 1
                else:
                    par_dict[new_word] = 1
        
        max_count = 0
        most_frequent_word = None
        for word, count in par_dict.items():
            if count > max_count:
                max_count = count
                most_frequent_word = word
        return most_frequent_word