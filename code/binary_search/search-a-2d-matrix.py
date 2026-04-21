# https://leetcode.com/problems/search-a-2d-matrix/description/

"""
"""

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left_row, right_row = 0, len(matrix)-1
        mid_row = 0
        while (left_row <= right_row):
            mid_row = (right_row+left_row) // 2
            if (matrix[mid_row][0] > target):
                right_row = mid_row-1
            elif (matrix[mid_row][-1] < target):
                left_row = mid_row+1
            else:
                break

        left_row, right_row = 0, len(matrix[mid_row])-1
        while (left_row <= right_row):
            mid = (right_row+left_row)//2
            if (matrix[mid_row][mid] == target):
                return True
            elif matrix[mid_row][mid] < target:
                left_row = mid+1
            else:
                right_row = mid-1
        return False


print(Solution().searchMatrix(
    [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3))
print(Solution().searchMatrix([[1]], 2))

print(Solution().searchMatrix([[1], [3]], 1))
