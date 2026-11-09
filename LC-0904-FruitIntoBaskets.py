# LeetCode Problem: 904. Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        freq = {}
        left = 0
        longest = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            if fruit in freq:
                freq[fruit] += 1
            else:
                freq[fruit] = 1

            while len(freq) > 2:
                left_fruit = fruits[left]
                freq[left_fruit] -= 1

                if freq[left_fruit] == 0:
                    del freq[left_fruit]

                left += 1

            longest = max(longest, right - left + 1)

        return longest
