# LeetCode Problem: 2965. Find Missing And Repeated Values
# https://leetcode.com/problems/find-missing-and-repeated-values/

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        repeated = -1
        total_sum = 0
        seen = set()

        seen = set()
        for i in range(n):
            for j in range(n):
                if grid[i][j] in seen:
                    repeated = grid[i][j]
                seen.add(grid[i][j])
                total_sum += grid[i][j]
        
        expected_sum = n * n * (n * n + 1) // 2 
        missing = expected_sum - total_sum + repeated

        return [repeated, missing]