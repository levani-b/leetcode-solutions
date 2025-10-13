# LeetCode Problem: 2273. Find Resultant Array After Removing Anagrams
# https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        def are_anagrams(word1, word2):
            if len(word1) != len(word2):
                return False
            
            hash_word1 = {}
            hash_word2 = {}
            for char in word1:
                if char in hash_word1:
                    hash_word1[char] += 1
                else:
                    hash_word1[char] = 1
            
            for char in word2:
                if char in hash_word2:
                    hash_word2[char] += 1
                else:
                    hash_word2[char] = 1
            
            return hash_word1 == hash_word2

        result = [words[0]]
        for i in range(1, len(words)):
            if not are_anagrams(result[-1], words[i]):
                result.append(words[i])
        return result

