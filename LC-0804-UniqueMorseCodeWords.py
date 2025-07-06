# LeetCode Problem: 804. Unique Morse Code Words
# https://leetcode.com/problems/unique-morse-code-words/

from typing import List


class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        unique_transformations = set()
    
    
        for word in words:
            transformation = ""
            for char in word:
                char_index = ord(char) - ord('a')
                transformation += morse_code[char_index]
            
            unique_transformations.add(transformation)
        
        return len(unique_transformations)

