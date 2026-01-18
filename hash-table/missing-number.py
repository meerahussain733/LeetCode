class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        new=set(nums)
        target=len(nums)
        for i in range(len(nums)):
            if target-i not in new:
                return target-i
        return 0
        