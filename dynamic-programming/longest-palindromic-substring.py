class Solution:
    def longestPalindrome(self, s: str) -> str:
        mid=len(s)//2
        if len(s)%2==0:
            l,r = mid -1, mid
        else:
            l=r=mid
        if len(s)<2:
            return s
            
        while l>0 and r< len(s)-1:
                if s[l]==s[r]:
                    l=l-1
                    r=r+1
                elif len[s]==2:
                    return s[l]
        return s[l+1:r]