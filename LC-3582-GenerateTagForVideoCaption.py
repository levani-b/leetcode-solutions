# LeetCode Problem: 3582. Generate Tag For Video Caption
# https://leetcode.com/problems/generate-tag-for-video-caption/

class Solution:
    def generateTag(self, caption: str) -> str:
        words = caption.split()
        cleaned_words = []

        for i, word in enumerate(words):
            cleaned = ''
            for char in word:
                if char.isalpha():
                    cleaned += char

            if cleaned == '':
                continue
            
            if i == 0:
                cleaned_words.append(cleaned.lower())
            else:
                cleaned_words.append(cleaned.capitalize())
        
        tag = f"#{''.join(cleaned_words)}"

        if len(tag) > 100:
            tag = tag[:100]

        return tag