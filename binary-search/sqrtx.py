class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1:
            return 1
        elif x==0:
            return 0
        else:
            return int(x**0.5)
        