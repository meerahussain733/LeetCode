class Solution:
    def romanToInt(self, s: str) -> int:
        h = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
        val=0
        if len(s)==1:
            return h[s[0]]
        for char in range(len(s)-1):
            if h[s[char]]>=h[s[char+1]]:
                val=val+h[s[char]]
                char+=1
            else:
                val=val-h[s[char]]
                char+=1
            if char==len(s)-1:
                val=val+h[s[char]]
                return val

    
        

        