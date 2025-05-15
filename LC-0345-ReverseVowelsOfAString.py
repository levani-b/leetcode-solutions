# LeetCode Problem: 345. Reverse Vowels Of A String
# https://leetcode.com/problems/reverse-vowels-of-a-string/


def reverseVowels(s: str) -> str:
    vowels = {'a','e','i','o','u',"A",'E','I','O','U'}
    start = 0
    end = len(s)-1
    s = list(s)
    while end>start:
        while start < end and s[start] in vowels:
            start += 1

        while start < end and s[end] in vowels:
            end-=1
        
        s[start], s[end] = s[end],s[start]
        start +=1
        end-=1
    return s
                
