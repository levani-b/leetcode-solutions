# LeetCode Problem: 1299. Replace Elements With Greatest Element On Right Side
# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/


def replaceElements(arr):
    if len(arr) == 1:
        return [-1]
            
    maxN = -1
    for i in range(len(arr) -1, -1, -1):
        temp = arr[i]
        arr[i] = maxN
        maxN = max(temp, maxN)
    return arr