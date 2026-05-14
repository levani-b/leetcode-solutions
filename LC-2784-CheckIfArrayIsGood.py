# LeetCode Problem: 2784. Check If Array Is Good
# https://leetcode.com/problems/check-if-array-is-good/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) != max(nums) + 1:
            return False
        
        freq = {} 
        max_num = max(nums)

        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1
        
        for num in range(1, max_num + 1):
            if num not in freq:
                return False
            if num == max_num:
                if freq[num] != 2:
                    return False
            else:
                if freq[num] != 1:
                    return False
        
        return True