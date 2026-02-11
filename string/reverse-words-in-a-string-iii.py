class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        reverse_l=[]
        for i in s:
            reverse_l.append(i[::-1])
        return ' '.join(reverse_l)