class Solution:
    def climbStairs(self, n: int) -> int:
        if n==1:
            return 1
        return (n*(self.climbStairs(n-1)))//(n-1)
        