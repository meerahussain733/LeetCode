class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_profit=0
        max_profit=0
        for current in range(1,len(prices)):
                if prices[current]<prices[min_profit]:
                    min_profit=current
                else:
                    max_profit=max(max_profit,prices[current]-prices[min_profit])
        return max_profit
        