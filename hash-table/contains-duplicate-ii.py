class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        for index, number in enumerate(nums):
            if number in window:
                return True
            window.add(number)

            if index >= k:
                window.remove(nums[index-k])
        
        return False
    