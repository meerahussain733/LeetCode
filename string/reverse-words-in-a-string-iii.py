class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split(" ")
        t=''
        for i in s:
            i=i[::-1]
            t=t+i+' '
        return t[:len(t)-1]