class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count=0
        for i in range(len(s)):
            for j in range(i,len(t)):
                if s[i]==t[j]:
                    count+=1
                    j+=1
        if count==len(s):
            return True
        return False
        
        