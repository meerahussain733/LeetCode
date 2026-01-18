class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        l=0
        h=len(nums)-1
        nums=sorted(nums)
        target=len(nums)
        while l<=h:
            if (nums[l]+nums[h]) == target:
                l+=1
                h-=1
            elif (nums[l]+nums[h])<target:
                return nums[h]+1
            else:
                return nums[l]-1
