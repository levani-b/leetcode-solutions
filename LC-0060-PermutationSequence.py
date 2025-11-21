# LeetCode Problem: 60. Permutation Sequence
# https://leetcode.com/problems/permutation-sequence/

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        factorial = [1]
        for i in range(1, n):
            factorial.append(factorial[-1] * i)

        numbers = list(range(1, n + 1))

        k -= 1
    
        result = []
        for i in range(n):
            index = k // factorial[n - i - 1]
            
            result.append(str(numbers[index]))
            
            numbers.pop(index)
            
            k %= factorial[n - i - 1]
    
        return ''.join(result)