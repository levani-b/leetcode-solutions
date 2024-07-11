# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

def removeDuplicates( nums):
        l = 1
        for r in range(1,len(nums)):
                if nums[r] != nums[r-1]:
                        nums[l] = nums[r]
                        l+=1
        return l


# def removeDuplicates(nums):
#         nums[:] = sorted(set(nums))
#         return len(nums)