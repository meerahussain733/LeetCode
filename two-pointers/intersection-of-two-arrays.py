class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set=set()
        res=[]
        for i in nums1:
            if i not in hash_set:
                hash_set.add(i)
        for i in hash_set:
            if i in nums2:
                res.append(i)
        return res    
        

        