class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if not nums:
            return 0
        return nums[len(nums)-1]
        