class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        hash_map={}
        for i in range(len(friends)):
            for j in range(len(order)):
                if friends[i]==order[j]:
                    hash_map[friends[i]]=j
        return sorted(friends, key=lambda x: hash_map[x])

        


        