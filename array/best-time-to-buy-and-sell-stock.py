class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #brute force
        max_profit=0
        for i in range(len(prices)-1):
            cur_profit=0
            for j in range(i+1,len(prices)):
                if prices[i]<prices[j]:
                    cur_profit=prices[j]-prices[i]
                max_profit=max(max_profit,cur_profit)
        return max_profit
        