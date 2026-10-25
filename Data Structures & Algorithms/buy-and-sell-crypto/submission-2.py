class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        maxi=-float('inf')
        buy=0
        for sell in range(buy+1,n):
            profit=prices[sell]-prices[buy]
            maxi=max(profit,maxi)
            while prices[buy]>prices[sell]:
                buy+=1
        if maxi>0:
            return maxi
        else:
            return 0