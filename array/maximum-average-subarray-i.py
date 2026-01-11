class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_avg=0
        n=len(nums)
        for i in range(n-k+1):
            cur_avg=0
            for j in range(k):
                cur_avg+=nums[i+j]
            max_avg=max(max_avg,cur_avg)
        return max_avg/k
        