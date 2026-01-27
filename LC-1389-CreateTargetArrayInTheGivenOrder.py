# LeetCode Problem: 1389. Create Target Array in The Given Order
# https://leetcode.com/problems/create-target-array-in-the-given-order/

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
      target = []

      for i in range(len(nums)):
        idx = index[i]
        num = nums[i]
        target.insert(idx, num)

      return target  