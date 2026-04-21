# https://leetcode.com/problems/largest-rectangle-in-histogram/description/

"""
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk = []
        max_area = 0

        #
        for i, h in enumerate(heights):
            start = i
            while (stk and stk[-1][1] >= h):
                start_index, height = stk.pop()
                # i is right boundary, so width = i - start_index
                max_area = max(max_area, height * (i-start_index))
                start = start_index
            stk.append((start, h))

        # handle the shortest point
        for i, h in stk:
            max_area = max(max_area, h * (len(heights)-i))

        return max_area


print(Solution().largestRectangleArea([2, 1, 5, 6, 2, 3]))
print(Solution().largestRectangleArea([2, 4]))
