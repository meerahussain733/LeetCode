class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hash_map={}
        for i in nums:
            if i in hash_map:
                hash_map[i]+=1
            else:
                hash_map[i]=1

        pairs=0
        for freq in hash_map.values():
            pairs+=freq*(freq-1)//2
        return pairs
        
        