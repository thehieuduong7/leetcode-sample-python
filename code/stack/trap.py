# https://leetcode.com/problems/trapping-rain-water/


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        while (i < j and height[i] <= height[i+1]):
            i += 1

        while (i < j and height[j-1] >= height[j]):
            j -= 1
        size = 0
        min_height = min(height[i], height[j])
        while (i < j):
            if (height[i] < height[j]):
                next_index = i+1
                i += 1
            else:
                next_index = j-1
                j -= 1
            gap = min_height - height[next_index]
            if (gap > 0):
                size += gap
            else:
                min_height = min(height[i], height[j])

        return size


print(Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
print(Solution().trap([4, 2, 0, 3, 2, 5]))
