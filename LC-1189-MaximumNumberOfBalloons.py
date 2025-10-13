# LeetCode Problem: 1189. Maximum Number of Balloons
# https://leetcode.com/problems/maximum-number-of-balloons/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        def get_char_count(txt):
            count = {}
            for char in txt:
                if char in count:
                    count[char] += 1
                else:
                    count[char] = 1
            return count
        
        balloon_count = get_char_count('balloon')
        text_count = get_char_count(text)

        max_balloons = float('inf')

        for char, needed in balloon_count.items():
            if char not in text_count:
                return 0
            max_balloons = min(max_balloons, text_count[char] // needed)
        
        return max_balloons