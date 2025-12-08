class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        l,r=0,len(needle)-1
        if len(needle)==0:
            return 0
        while r<len(haystack):
            if haystack[l:r+1] ==needle:
                return l
            l=l+1
            r=r+1
        return -1