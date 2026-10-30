# LeetCode Problem: 769. Max Chunks To Make Sorted
# https://leetcode.com/problems/max-chunks-to-make-sorted/

class Solution:
    def maxChunksToSorted(self, arr: list[int]) -> int:
        count = 0
        max_seen_num = float('-inf')
        for i in range(len(arr)):
            if max_seen_num < arr[i]:
                max_seen_num = arr[i]
            
            if max_seen_num == i:
                count += 1

        return count
            
