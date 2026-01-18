class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        set contains unique numbers,
        target=len(nums)
        '''
        target=len(nums)
        nums_set=set(nums)
        for i in nums_set:
            if target-i in nums_set:
                pass
            else:
                return target-i
        