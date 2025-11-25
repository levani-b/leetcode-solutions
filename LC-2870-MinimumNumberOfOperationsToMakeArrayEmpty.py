# LeetCode Problem: 2870. Minimum Number Of Operations To Make Array Empty
# https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        oper = 0
        for num, count in freq.items():
            if count == 1:
                return -1
            if count % 3 == 0:
                oper += count // 3
            elif count % 3 == 1:
                oper += (count // 3 - 1) + 2
            else:  
                oper += (count // 3) + 1
        

        return oper