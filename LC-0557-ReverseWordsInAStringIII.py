# LeetCode Problem: 557. Reverse Words In A String III
# https://leetcode.com/problems/reverse-words-in-a-string-iii/

class Solution:
    def reverseWords(self, s: str) -> str:
        list_of_words = s.split()
        res = []
        for word in list_of_words:
            word_lst = list(word)
            l = 0
            r = len(word_lst) - 1

            while l < r:
                word_lst[l], word_lst[r] = word_lst[r], word_lst[l]
                l += 1
                r -= 1
            res.append(''.join(word_lst))

        return ' '.join(res)
