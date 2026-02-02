# LeetCode Problem: 524. Longest Word In Dictionary Through Deleting
# https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        def check_words(word):
            i = 0
            for char in s:
                if i < len(word) and char == word[i]:
                    i += 1
            
            return len(word) == i
        
        longest_word = ''
        res = []
        for word in dictionary:
            if check_words(word):
                if len(word) > len(longest_word) or (len(word) == len(longest_word) and word < longest_word):
                    longest_word = word
        return longest_word