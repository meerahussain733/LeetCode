class Solution:
    def maxDistinct(self, s: str) -> int:
        count=0
        hash_set=set()
        for i in s:
            if i not in hash_set:
                hash_set.add(i)
                count+=1
        return count
                


        