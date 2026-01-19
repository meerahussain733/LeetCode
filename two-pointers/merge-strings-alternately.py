class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        p1=p2=0
        new=[]
        while p1<len(word1) and p2<len(word2):
            new.append(word1[p1])
            new.append(word2[p2])
            p1+=1
            p2+=1
        if len(word1)>len(word2):
            new.append(word1[p1:])
        else:
            new.append(word2[p2:])

        return ''.join(new)


        