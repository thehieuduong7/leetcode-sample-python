# https://leetcode.com/problems/product-of-array-except-self/

#! You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        rightAccumulate = 1
        leftAccumulate = 1

        for i in range(n):
            #! just update value, don't need *= leftAccumulate
            result[i] = leftAccumulate
            leftAccumulate *= nums[i]

        for i in range(n-1, -1, -1):
            result[i] *= rightAccumulate
            rightAccumulate *= nums[i]

        return result


print(Solution().productExceptSelf([1, 2, 3, 4]))
print(Solution().productExceptSelf([-1, 1, 0, -3, 3]))
