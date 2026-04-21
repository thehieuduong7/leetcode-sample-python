# https://leetcode.com/problems/container-with-most-water/description/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_value = min(height[i], height[j]) * (j-i)
        while (i < j):
            hoz = j-i
            if height[i] < height[j]:
                min_height = height[i]
                i += 1
            else:
                min_height = height[j]
                j -= 1
            max_value = max(max_value, min_height*hoz)
        return max_value


print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print(Solution().maxArea([1, 1]))
