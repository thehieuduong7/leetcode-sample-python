# https://leetcode.com/problems/maximum-subarray/

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum_arr = [nums[0]]

        for i in range(1, len(nums)):
            temp_max = max(nums[i], sum_arr[-1] + nums[i])
            sum_arr.append((temp_max))

        return max(sum_arr)

if __name__ == "__main__":
    print(Solution().maxSubArray([-2, 1]))



