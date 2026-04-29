# LeetCode Problem: 271. Encode And Decode Strings
# https://leetcode.com/problems/encode-and-decode-strings/

class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ''
        for word in strs:
            word_to_add = f'{len(word)}#{word}'
            encoded += word_to_add      
        return encoded
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res