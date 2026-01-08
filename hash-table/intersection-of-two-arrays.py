class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_set1=set(nums1)
        hash_set2=set(nums2)
        res=[]
        for i in hash_set1:
            if i in hash_set2:
                res.append(i)
        return res
            
              
        

        