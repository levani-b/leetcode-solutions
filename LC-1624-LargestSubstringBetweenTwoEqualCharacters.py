# LeetCode Problem: 1624. Largest Substring Between Two Equal Characters
# https://leetcode.com/problems/largest-substring-between-two-equal-characters/

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        largest_substring = -1
        freq = {}
        
        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]].append(i)
            else:
                freq[s[i]] = [i]
        
        for char, indexes in freq.items():
            curr_substring = 0
            if len(indexes)>1:
                curr_substring = indexes[-1] - indexes[0] - 1
            
            if curr_substring > largest_substring and len(indexes) > 1:
                largest_substring = curr_substring
        
        return largest_substring