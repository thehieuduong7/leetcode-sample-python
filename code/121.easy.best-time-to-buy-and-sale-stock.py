from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max_profit = 0
        # for i in range(len(prices)):
        #     if (i == 0 ):
        #         max_profit = 0
        #         min_value = prices[i]
        #         continue


        #     max_profit = max(max_profit, prices[i] - min_value)
        #     min_value = min(min_value, prices[i])
        # return max_profit
        f1 = -prices[0]
        f2 = 0
        for i in range(1,len(prices)):
            f1 = max(f1, - prices[i])
            f2 = max(f2, f1 + prices[i])

        return f2



if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    print(solution.maxProfit([7,6,4,3,1]))

