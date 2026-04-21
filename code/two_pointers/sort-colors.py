
# https://leetcode.com/problems/sort-colors/

from typing import List


class Solution:
    # def sortColors(self, nums: List[int]) -> None:
    #     """
    #     Do not return anything, modify nums in-place instead.
    #     """
    #     data = {
    #         0: 0,
    #         1: 0,
    #         2: 0
    #     }
    #     n = len(nums)
    #     for i in nums:
    #         data[i] += 1

    #     for i in range(n):
    #         if(data[0]):
    #             nums[i] = 0
    #             data[0] -=1
    #         elif(data[1]):
    #             nums[i] = 1
    #             data[1] -=1
    #         else:
    #             nums[i] = 2
    #             data[2] -=1

    #     return nums
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = -1
        r = len(nums)
        i = 0
        while(i<r):
            if(nums[i]==0):
                l+=1
                nums[i], nums[l] = nums[l], nums[i]
                # 0 is on the left, next nums
                i+=1
            elif(nums[i]==2):
                r-=1
                nums[i], nums[r] = nums[r], nums[i]
                # may be switch 2 to 2, wait for next round
            else:
                i+=1


        return nums

if __name__ == "__main__":
    solution = Solution()
    print(solution.sortColors([2,0,2,1,1,0]))
