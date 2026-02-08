class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        c=0
        for i in s:
            if i in t:
                c+=1
        if c==len(s):
            return True 
        return False
        