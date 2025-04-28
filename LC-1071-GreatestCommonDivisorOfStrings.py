# LeetCode Problem: 1071. Greatest Common Divisor Of Strings
# https://leetcode.com/problems/greatest-common-divisor-of-strings/

def gcdOfStrings(str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1: 
            return ''
        
        def gcd(l1, l2):
            while l2 != 0:
                tmp = l2
                l2 = l1 %  l2
                l1 = tmp
            return l1
        
        gcd_len = gcd(len(str1), len(str2))
        gcreatest_comm_divisor = str1[:gcd_len]
        return gcreatest_comm_divisor