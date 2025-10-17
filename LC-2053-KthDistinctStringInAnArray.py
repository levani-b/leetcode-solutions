# LeetCode Problem: 2053. Kth Distinct String in an Array
# https://leetcode.com/problems/kth-distinct-string-in-an-array/

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        res = []
        for s in arr:
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1

        distincts = []
        for st, count in freq.items():
            if count == 1:
                distincts.append(st)

                
        
        if k <= len(distincts):
            return distincts[k - 1]
        return ""