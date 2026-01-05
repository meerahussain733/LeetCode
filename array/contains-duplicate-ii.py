class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #brute force
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True 
        return False
        