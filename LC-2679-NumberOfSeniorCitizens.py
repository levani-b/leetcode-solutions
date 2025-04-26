# LeetCode Problem: 2679. Number Of Senior Citizens
# https://leetcode.com/problems/number-of-senior-citizens/

def countSeniors(details):
        count = 0
        for age in details:
            age = int(age[11:13])
            if age > 60:
                count += 1
    
        return count