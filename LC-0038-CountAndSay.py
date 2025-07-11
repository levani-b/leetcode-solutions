# LeetCode Problem: 38. Count And Say
# https://leetcode.com/problems/count-and-say/

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        prev = "1"
        for _ in range(2, n + 1):
            result = ""
            count = 1
            for i in range(1, len(prev)):
                if prev[i] == prev[i - 1]:
                    count += 1
                else:
                    result += str(count) + prev[i - 1]
                    count = 1
            result += str(count) + prev[-1] 
            prev = result
        
        return prev
