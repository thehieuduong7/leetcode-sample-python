# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortNum = sorted(nums)

        values = []
        for i in range(len(sortNum)-2):
            if sortNum[i] > 0:
                break
            if i > 0 and sortNum[i] == sortNum[i-1]:
                continue

            left, right = i+1, len(sortNum)-1
            while (left < right):
                sum = sortNum[i] + sortNum[left] + sortNum[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    values.append([sortNum[i], sortNum[left], sortNum[right]])
                    left += 1
                    right -= 1
                    while (left < right and sortNum[left] == sortNum[left-1]):
                        left += 1

                    #
                    while (left < right and sortNum[right] == sortNum[right+1]):
                        right -= 1
        return values


print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
print(Solution().threeSum([0, 0, 0]))
print(Solution().threeSum([-1, 0, 1, 0]))
print(Solution().threeSum([0, 0, 0, 0]))
print(Solution().threeSum([-2, 0, 1, 1, 2]))
