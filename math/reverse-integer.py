class Solution:
    def reverse(self, x: int) -> int:
        sign =-1 if x<0 else 1
        x=abs(x)
        rev=0
        while x>0:
            reminder=x%10
            rev=rev*10 +reminder
            x=x//10
        
        if -2**31 <= rev <= 2**31-1:
            return sign*rev
        return 0
        

        
        