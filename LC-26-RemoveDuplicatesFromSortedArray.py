def removeDuplicates(nums):
        nums[:] = sorted(set(nums))
        return len(nums)