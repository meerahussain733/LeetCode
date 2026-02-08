class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):return False
        if len(s) == 0:return True
        c=0
        for i in range(0,len(t)):
            if c <= len(s) -1:
                if s[c]==t[i]:
                    c+=1
        return  c == len(s) 
        