# LeetCode Problem: 1859. Sorting The Sentence
# https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
            words = s.split()
            word_positions = []
            
            for word in words:
                position = int(word[-1])
                original_word = word[:-1]
                word_positions.append((position, original_word))
            
            word_positions.sort(key=lambda x: x[0])
            sorted_words = [word for position, word in word_positions]
            return ' '.join(sorted_words)
