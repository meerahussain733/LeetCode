class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        l,h=0,len(nums)-1
        while l<=h:
            mid=(h+l)//2
            if nums[mid]==target:
                return mid
            if nums[mid]> target:
                h=mid-1
            else:
                l=mid+1
        return l
        
        