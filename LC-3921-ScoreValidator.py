# LeetCode Problem: 3921. Score Validator
# https://leetcode.com/problems/score-validator/

class Solution:
    def scoreValidator(self, events: list[str]) -> list[int]:
        score = 0
        counter = 0
        res = []
        for event in events:
            if event == 'W':
                counter += 1
            elif event == 'WD' or event == 'NB':
                score += 1
            else:
                score += int(event)
            if counter == 10:
                break
        res.append(score)
        res.append(counter)
            
        return res