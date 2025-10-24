# LeetCode Problem: 2490. Circular Sentence
# https://leetcode.com/problems/circular-sentence/

class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentence_list = sentence.split(' ')

        if sentence[0] != sentence[-1]:
            return False
        
        for i in range(len(sentence_list)-1):
            if sentence_list[i][-1] != sentence_list[i+1][0]:
                return False
        
        return True