# LeetCode Problem: 1352. Product of the Last K Numbers
# https://leetcode.com/problems/product-of-the-last-k-numbers/

class ProductOfNumbers:

    def __init__(self):
        self.pref_stream = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.pref_stream = [1]
        else:
            curr_num = self.pref_stream[-1] * num
            self.pref_stream.append(curr_num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.pref_stream):
            return 0

        l = len(self.pref_stream) - k - 1
        return self.pref_stream[-1] // self.pref_stream[l]
