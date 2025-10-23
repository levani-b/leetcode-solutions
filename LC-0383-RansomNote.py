# LeetCode Problem: 383. Ransom Note
# https://leetcode.com/problems/ransom-note/

from typing import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False
        
        notes_count = Counter(ransomNote)
        magazine_count = Counter(magazine)

        for char, count in notes_count.items():
            if magazine_count[char] < count:
                return False
            
        return True