# LeetCode Problem: 557. Reverse Words In A String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        def reverse_word(word):
            word_list = list(word)
            l,r = 0, len(word) - 1
            while l < r:
                word_list[l], word_list[r] = word_list[r], word_list[l]
                l += 1
                r -= 1
            
            return ''.join(word_list)
        
        words = s.split()
        for i in range(len(words)):
            words[i] = reverse_word(words[i])
        
        return ' '.join(words)