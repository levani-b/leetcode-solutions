# LeetCode Problem: 229. Majority Element Ii
# https://leetcode.com/problems/majority-element-ii/

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            
        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        threshold = len(nums) // 3
        result = []
        if count1 > threshold:
            result.append(candidate1)
        if count2 > threshold:
            result.append(candidate2)
        
        return result

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         res = []
#         freq = {}
#         for num in nums:
#             if num in freq:
#                 freq[num] += 1
#             else:
#                 freq[num] = 1
        
#         threshold = len(nums) / 3
#         for num, count in freq.items():
#             if count > threshold:
#                 res.append(num)
        
#         return res