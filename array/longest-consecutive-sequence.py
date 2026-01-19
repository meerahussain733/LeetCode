class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        if not nums:
            return 0
        
        max_count=0
        count=1
        
        sort_num=sorted(num_set)
        if len(sort_num)==1:
            return 1
        for i in range(len(sort_num)-1):
            if sort_num[i]+1 ==sort_num[i+1]:
                count+=1
                max_count=max(max_count,count)
            else:
                count=1
                max_count=max(max_count,count)
        return max_count