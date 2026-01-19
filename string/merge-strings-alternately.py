class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1=0
        p2=0
        new=''
        while p1<len(word1) and p2<len(word2):
            new+=word1[p1]
            p1+=1
            new+=word2[p2]
            p2+=1
        if len(word1)>len(word2):
            new=new+word1[p1:]
        else:
            new=new+word2[p2:]

        return new


        