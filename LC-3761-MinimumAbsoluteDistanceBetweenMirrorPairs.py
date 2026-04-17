# LeetCode Problem: 3761. Minimum Absolute Distance Between Mirror Pairs
# https://leetcode.com/problems/minimum-absolute-distance-between-mirror-pairs/

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        def reverse(num):
            reversed_num = 0
            while num > 0:
                digit = num % 10
                reversed_num = (reversed_num * 10) + digit
                num //= 10
            return reversed_num
        
        reversed_map = {}
        min_dist = float('inf')
        
        for i, num in enumerate(nums):
            if num in reversed_map:
                min_dist = min(min_dist, i - reversed_map[num])
            
            rev = reverse(num)    
            reversed_map[rev] = i
        
        return min_dist if min_dist != float('inf') else -1