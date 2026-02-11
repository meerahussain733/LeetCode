class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for row in words:
            if row ==row[::-1]:
                return row
        return ''
        