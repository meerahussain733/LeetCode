class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        set contains unique numbers,
        target=len(nums)
        '''
        nums_set=set()
        for i in range(len(nums)+1):
            nums_set.add(i)
        for i in nums_set:
            if i not in nums:
                return i