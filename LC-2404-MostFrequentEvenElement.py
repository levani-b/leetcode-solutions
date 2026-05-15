# LeetCode Problem: 2404. Most Frequent Even Element
# https://leetcode.com/problems/most-frequent-even-element/

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        freq = {}
        for num in nums:
            if num % 2 == 0:
                if num in freq:
                    freq[num] += 1
                else:
                    freq[num] = 1
        
        if not freq:
            return -1

        most_freq = 0
        for count in freq.values():
            if count > most_freq:
                most_freq = count
        
        res = -1
        for num, count in freq.items():
            if count == most_freq:
                if res == -1 or num < res:
                    res = num

        return res