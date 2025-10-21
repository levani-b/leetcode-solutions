# LeetCode Problem: 929. Unique Email Addresses
# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniques = set()
        for email in emails:
            normalized_email = ''
            local_name,domain_name = email.split('@')

            for char in local_name:
                if char == '+':
                    break
                elif char != '.':
                    normalized_email += char
            
            normalized_email += f'@{domain_name}'
            uniques.add(normalized_email)
        return len(uniques)