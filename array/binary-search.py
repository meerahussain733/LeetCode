class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,h=0,len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if target==nums[mid]:
                return mid
            elif target <= nums[mid]:
                h=mid-1
            else:
                l=mid+1
        return -1