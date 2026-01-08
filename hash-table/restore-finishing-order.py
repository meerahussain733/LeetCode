class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        hash_map={}
        for i in range(len(order)):
            hash_map[order[i]]=i
        return sorted(friends, key=lambda x: hash_map[x])

        


        