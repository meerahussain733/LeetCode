class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        hash_set=set()
        L=[]
        for i in nums:
            if i in hash_set:
                L.append(i)
            hash_set.add(i)
        return L

        