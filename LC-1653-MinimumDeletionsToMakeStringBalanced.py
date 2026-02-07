# LeetCode Problem: 1653. Minimum Deletions To Make String Balanced
# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        min_deletion = float('inf')
        b_count = 0
        a_count = s.count('a')

        for i in range(len(s) + 1):
            
            min_deletion = min(min_deletion, a_count + b_count)

            if i < len(s):
                if s[i] == 'b':
                    b_count += 1
                else:
                    a_count -= 1

        return min_deletion 