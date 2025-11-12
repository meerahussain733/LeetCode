class Solution:
    def longestPalindrome(self, s: str) -> int:
        hmap=set()
        res=0
        for c in s:
            if c in hmap:
                hmap.remove(c)
                res+=2
            else:
                hmap.add(c)
        
        if hmap:
            res+=1
        else:
            res
        return res


        