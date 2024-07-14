# https://leetcode.com/problems/build-array-from-permutation/

def buildArray(self, nums):
        new_arr = []
        for i in range(len(nums)):
            new_arr.append(nums[nums[i]])
        
        return new_arr