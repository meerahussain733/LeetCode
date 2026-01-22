class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        n=len(height)
        for i in range(n):
            l_max=r_max=height[i]
            for j in range(i):
                l_max=max(l_max,height[j])
            for k in range(i+1,n):
                r_max=max(r_max,height[k])
            res+=min(l_max,r_max)-height[i]
        return res
        
        