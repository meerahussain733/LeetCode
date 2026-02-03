class Solution:
    def firstUniqChar(self, s: str) -> int:
        hash=[0]*26
        for c in s:
            hash[ord(c)-ord('a')]+=1
        for i,c in enumerate(s):
            if hash[ord(c)-ord('a')]==1:
                return i
        return -1

        