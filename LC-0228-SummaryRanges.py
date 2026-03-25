# LeetCode Problem: 228. Summary Ranges
# https://leetcode.com/problems/summary-ranges/

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        range_start = nums[0]

        for i in range(1,len(nums)):
            if nums[i] - 1 != nums[i - 1]:
                ranges.append([range_start, nums[i - 1]])
                range_start = nums[i]

        ranges.append([range_start, nums[-1]])
        
        res = []
        for r in ranges:
            if r[0] == r[1]:
                res.append(str(r[0]))
            else:
                res.append(f'{str(r[0])}->{str(r[1])}')
        
        return res