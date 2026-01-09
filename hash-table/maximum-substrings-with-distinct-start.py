class Solution:
    def maxDistinct(self, s: str) -> int:
        hash_set=set(s)
        return len(hash_set)
                


        