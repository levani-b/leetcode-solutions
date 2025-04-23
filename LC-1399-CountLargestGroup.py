# LeetCode Problem: 1399. Count Largest Group
# https://leetcode.com/problems/count-largest-group/

def countLargestGroup(n):
        def get_sum(x):
            sum = 0
            while(x != 0):       
                sum = sum + (x % 10)
                x = x//10
            return sum 
        
        group = {}
        for i in range(1,n+1):
            digit_sum = get_sum(i)
            if digit_sum in group:
                group[digit_sum] += 1
            else:
                group[digit_sum] = 1
        
        max_size = max(group.values())
        count = 0
        for value in group.values():
            if value == max_size:
                count += 1
        return count