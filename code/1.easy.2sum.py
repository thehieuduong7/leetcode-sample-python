# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            need = target-nums[i]
            if (hash.get(need)!=None):
                return [hash.get(need), i]
            hash[nums[i]] = i



print(Solution().twoSum([2,7,11,15],9))
