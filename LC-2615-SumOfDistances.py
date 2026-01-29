# LeetCode Problem: 2615. Sum Of Distances
# https://leetcode.com/problems/sum-of-distances/

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)

        hasht = {}

        for i in range(len(nums)):
            if nums[i] not in hasht:
                hasht[nums[i]] = []
            hasht[nums[i]].append(i)
        
        for indices in hasht.values():
            if len(indices) <= 0:
                continue
            
            prefix_sum = [0]
            for idx in indices:
                prefix_sum.append(prefix_sum[-1] + idx)
            
            for k in range(len(indices)):
                i = indices[k]

                count_before = k
                sum_before = prefix_sum[k]
                dist_before = i * count_before - sum_before

                count_after = len(indices) - k - 1
                sum_after = prefix_sum[-1] - prefix_sum[k+1]
                dist_after = sum_after - i * count_after
                
                arr[i] = dist_before + dist_after
        
        return arr