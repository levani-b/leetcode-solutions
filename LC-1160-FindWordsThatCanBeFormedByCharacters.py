# LeetCode Problem: 1160. Find Words That Can Be Formed By Characters
# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_count = {}
        for char in chars:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1
        
        total_len = 0
        for word in words:
            temp = char_count.copy()
            valid = True
            for ch in word:
                if ch not in temp or temp[ch] == 0:
                    valid = False
                    break
                temp[ch] -= 1
            if valid:
                total_len += len(word)
        
        return total_len