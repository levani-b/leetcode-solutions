# LeetCode Problem: 2243. Calculate Digit Sum of a String
# https://leetcode.com/problems/calculate-digit-sum-of-a-string/

class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ''

            for i in range(len(s), k):
                group = s[i:i+k]
                digit_sum = 0
                for num in group:
                    digit_sum += int(num)
                
                new_s += str(digit_sum)
            
            s = new_s
        
        return s
