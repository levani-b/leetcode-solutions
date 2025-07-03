# LeetCode Problem: 3304. Find the K-th Character in String Game I
# https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

class Solution:
    def kthCharacter(self, k: int) -> str:
        if k == 1:
            return 'a'
        
        operations = 0
        length = 1
        while length < k:
            length *= 2
            operations += 1

        half_length = length // 2
        
        if k <= half_length:
            return self.kthCharacter(k)
        else:
            corresponding_pos = k - half_length
            prev_char = self.kthCharacter(corresponding_pos)

            if prev_char == 'z':
                return 'a'
            else:
                return chr(ord(prev_char) + 1)
