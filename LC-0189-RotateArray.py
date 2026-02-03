# LeetCode Problem: 189. Rotate Array
# https://leetcode.com/problems/rotate-array/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1
            return arr

        n = len(nums)
        k = k % n
        reverse(nums,0,n-k-1)
        reverse(nums,n-k,n-1)
        reverse(nums, 0, n - 1)