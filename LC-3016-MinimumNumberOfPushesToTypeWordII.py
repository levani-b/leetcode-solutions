# LeetCode Problem: 3016. Minimum Number Of Pushes To Type Word II
# https://leetcode.com/problems/minimum-number-of-pushes-to-type-word-ii/

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq = {}
        for char in word:
            if char in freq:
                freq[char] += 1
            else:
                freq[char] = 1
       
        res = 0
        sorted_freq = sorted(freq.values(), reverse = True)
        for i, count in enumerate(sorted_freq):
            push = (i // 8) + 1
            res += count * push
        
        return res