# https://leetcode.com/problems/first-missing-positive/description/?envType=problem-list-v2&envId=hash-table

from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nextNumHash = {

        }
        for num in nums:
            nextNumHash[num] = nextNumHash.get(num+1) or num+1
            if (nextNumHash.get(num-1)):
                nextNumHash[num-1] = nextNumHash.get(num)

        i = 1
        while(nextNumHash.get(i)):
            i = nextNumHash.get(i)

        return i


print(Solution().firstMissingPositive([1, 2, 0]))
print(Solution().firstMissingPositive([3, 4, -1, 1]))
print(Solution().firstMissingPositive([1, 2, 6, 3, 5, 4]))

