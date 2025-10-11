class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:
            return s
        def update_point(l,r):
            while l>=0 and r< len(s) and s[l]==s[r]:
                        l=l-1
                        r=r+1
            return s[l+1:r]
        longest = ""
        for i in range(len(s)):
            odd_s = update_point(i, i)
            even_s = update_point(i, i + 1)
            if len(odd_s) > len(longest):
                longest = odd_s
            if len(even_s) > len(longest):
                longest = even_s
        return longest