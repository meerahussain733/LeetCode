class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        if not nums:
            return 0
        count=1
        sort_num=sorted(num_set)
        for i in range(len(sort_num)-1):
            if sort_num[i]+1 ==sort_num[i+1]:
                count+=1
        return count
        