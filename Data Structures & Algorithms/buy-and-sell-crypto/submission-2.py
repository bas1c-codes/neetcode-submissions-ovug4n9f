class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i=0
        j=1
        k=[0]
        while j<len(prices):
            if prices[i]>=prices[j]:
                i=j
                j+=1
            else:
                k.append(prices[j]-prices[i])
                j+=1
        print(k)
        return max(k)

        