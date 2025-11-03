# LeetCode Problem: 2559. Count Vowel Strings In Ranges
# https://leetcode.com/problems/count-vowel-strings-in-ranges/

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {'a', 'e', 'i', 'o','u'}

        prefix = [0]
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                prefix.append(prefix[-1] + 1)
            else:
                prefix.append(prefix[-1])
        
        res = []
        for l, r in queries:
            count = prefix[r +  1] - prefix[l]
            res.append(count)
        
        return res