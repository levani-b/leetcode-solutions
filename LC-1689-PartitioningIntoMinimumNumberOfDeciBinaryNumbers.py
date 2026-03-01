# LeetCode Problem: 1689. Partitioning Into Minimum Number of Deci-Binary Numbers
# https://leetcode.com/problems/partitioning-into-minimum-number-of-deci-binary-numbers/

class Solution:
    def minPartitions(self, n: str) -> int:
        for char in "987654321":
            if char in n:
                return int(char)
        
        return 0
    

# class Solution:
#     def minPartitions(self, n: str) -> int:
#         nums_needed = 0

#         for i in range(len(n)):
#             nums_needed = max(int(n[i]), nums_needed)
        
#         return nums_needed