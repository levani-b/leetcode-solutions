# LeetCode Problem: 151. Reverse Words In A String
# https://leetcode.com/problems/reverse-words-in-a-string/

def reverseWords(s: str) -> str:
        res = []
        words = s.strip().split()
        for i in range(len(words)-1, -1, -1):
            res.append(words[i])
        return ' '.join(res)