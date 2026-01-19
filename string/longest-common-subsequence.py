class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        hash_set=set(text1)
        hash_set2=set(text2)
        count=0
        for i in hash_set2:
            if i in hash_set:
                count+=1
        return count
        