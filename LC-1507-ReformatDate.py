# LeetCode Problem: 1507. Reformat Date
# https://leetcode.com/problems/reformat-date/

class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            "Jan": 1, "Feb": 2, "Mar": 3, "Apr": 4,
            "May": 5, "Jun": 6, "Jul": 7, "Aug": 8,
            "Sep": 9, "Oct": 10, "Nov": 11, "Dec": 12
        }        
        date = date.split()
        year = date[-1]
        month = str(months[date[1]])
        day = ''
        for ch in date[0]:
            if ch.isdigit():
                day += ch

        if len(day) == 1:
            day = '0' + day

        if len(month) == 1:
            month = '0' + month
        return f'{year}-{month}-{day}'