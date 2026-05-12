# LeetCode Problem: 831. Masking Personal Information
# https://leetcode.com/problems/masking-personal-information/

class Solution:
    def maskPII(self, s: str) -> str:
        def mask_email(email):
            res = ''
            email = email.split('@')
            res += email[0][0].lower() + '*****' + email[0][-1].lower() + "@" + email[1].lower()
            return res
        
        def mask_number(num):
            phone_num = ''
            for ch in num:
                if ch.isdigit():
                    phone_num += ch
            
            res = ''
            country_code = phone_num[:-10]
            country_code = "*" * len(country_code)
            last_nums = phone_num[-4:]
            if len(phone_num) > 10:
                res += '+' + country_code + '-***-***-' + last_nums
            else:
                res += '***-***-' + last_nums

            return res
        
        if '@' in s:
            return mask_email(s)
        else:
            return mask_number(s)
