# LeetCode Problem: 274. H Index
# https://leetcode.com/problems/h-index/

class Solution:
    def hIndex(self, citations: list[int]) -> int:
        n = len(citations)
        for h in range(n, -1, -1):
            count = 0
            for num in citations:
                if num >= h:
                    count += 1
            if count >= h:
                return h
