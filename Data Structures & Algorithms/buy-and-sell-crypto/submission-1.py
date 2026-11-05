class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)==0:
            return 0 
        elif len(prices)==1:
            return 0
        elif len(prices)==2:
            if prices[0]>prices[1]:
                return 0
            else:
                a=prices[1]-prices[0]
                return a
        else:
            maximum=0
            for i in range(len(prices)):
                for j in range(i+1,len(prices)):
                    if maximum<prices[j]-prices[i]:
                        maximum=prices[j]-prices[i]
            return maximum
