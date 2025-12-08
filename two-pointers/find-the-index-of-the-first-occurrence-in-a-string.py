class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l,r=0,len(needle)-1
        if haystack == needle:
            return 0
        while r<len(haystack):
            if needle[0]==haystack[l] and needle[len(needle)-1]==haystack[r]:
                return l
            l=l+1
            r=r+1
        return -1