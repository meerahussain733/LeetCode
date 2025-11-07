class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        l,r=0,n-1
        k=[]
        while l!=r:
            vol=(r-l)*(min(height[r],height[l]))
            k.append(vol)
            if height[l] < height[r]:
                l=l+1
            else:
                r=r-1
        return max(k)
            
