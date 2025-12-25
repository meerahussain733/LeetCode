class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        map={}
        for i in nums:
            if i in map:
                map[i]+=1
            else:
                map[i]=1
        return max(map,key=map.get)