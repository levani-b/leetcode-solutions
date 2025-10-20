# LeetCode Problem: 1701. Average Waiting Time
# https://leetcode.com/problems/average-waiting-time/

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total = 0
        remain_time = 0
        for customer in customers:
            start = customer[0]
            if remain_time > customer[0]:
                start = remain_time
                
            finish_time = start + customer[1]
            waiting_time = finish_time - customer[0]
            remain_time = finish_time
            total += waiting_time
        
        return total / len(customers)