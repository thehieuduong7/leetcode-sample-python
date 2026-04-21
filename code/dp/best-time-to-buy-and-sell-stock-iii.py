from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        f1 = -prices[0];
        f2 = 0
        f3 = -prices[0]
        f4 = 0
        n = len(prices)

        for i in range(n):
            if i ==0:
                continue

            f1 = max(f1, -prices[i])
            f2 = max(f2, f1 + prices[i])
            f3 = max(f3, f2 - prices[i])
            f4 = max(f4, f3 + prices[i])

            # print(f1, f2, f3, f4)
        return f4





if __name__ == "__main__":
    solution = Solution()
    print(solution.maxProfit([3,3,5,0,0,3,1,4]))
    # print(solution.maxProfit([7,6,4,3,1]))
    # print(solution.maxProfit([1]))

