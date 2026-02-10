class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for i in image:
            l,r=0,len(image)-1
            while l <= r:
                i[l], i[r] = 1 ^ i[r], 1 ^ i[l]
                l += 1
                r -= 1
        return image



