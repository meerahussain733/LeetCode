class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        start=nums[0]
        nums[1:]=sorted(nums[1:])
        return start+nums[1]+nums[2]
        