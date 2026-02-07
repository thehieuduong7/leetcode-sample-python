from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_index = 0
        profit = 0

        for i in range(1, len(prices)):
            if (prices[i] > prices[i-1]):
                profit += prices[i] - prices[buy_index]
            buy_index = i

        return profit





if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([7,1,5,3,6,4]))
    # print(solution.maxProfit([7,6,4,3,1]))
    # print(solution.maxProfit([1]))

