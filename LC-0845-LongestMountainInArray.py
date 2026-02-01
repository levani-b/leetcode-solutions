# LeetCode Problem: 845. Longest Mountain In Array
# https://leetcode.com/problems/longest-mountain-in-array/

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        max_length = 0

        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:

                left = i
                while left > 0 and arr[left] > arr[left - 1]:
                    left -= 1
                
                right = i
                while right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    right += 1
                
                length = right - left + 1
                max_length = max(max_length, length)
        return max_length