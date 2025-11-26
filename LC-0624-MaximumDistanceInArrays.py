# LeetCode Problem: 624. Maximum Distance in Arrays
# https://leetcode.com/problems/maximum-distance-in-arrays/

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        min_val = arrays[0][0]
        max_val = arrays[0][-1]
        for i in range(1,len(arrays)):
            res = max(res, max(abs(arrays[i][-1]- min_val),abs(max_val - arrays[i][0])))
            max_val = max(max_val, arrays[i][-1])
            min_val = min(arrays[i][0], min_val)
        return res