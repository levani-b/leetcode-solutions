# o(n) 
def twoSum(nums, target):
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in nums[i+1:]:
            j = nums.index(diff, i + 1)
            
            return [i, j]



# o(n^2) / nested loops
# def twoSum(nums, target):
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums [j] == target:
#                 return [i, j]