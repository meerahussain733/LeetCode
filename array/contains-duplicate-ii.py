class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #brute force
        for i in range(len(nums)-k):
            for j in range(i+1,k+i+1):
                if nums[i]==nums[j] and abs(i-j)<=k:
                    return True 
            i+=k-1
        return False
        