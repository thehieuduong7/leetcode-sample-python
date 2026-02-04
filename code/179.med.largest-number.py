from typing import List


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted = nums.copy()

        def partition(arr, low, high):
            pivot = arr[high]
            i = low - 1
            for j in range(low, high):
                a = str(arr[j])
                b = str(pivot)
                if a + b > b + a:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            # move pivot into middle
            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1

        def quicksort(arr, low, high):
            if low < high:
                i = partition(arr, low, high)
                quicksort(arr, low, i-1)
                quicksort(arr, i+1, high)
        quicksort(nums, 0, len(nums)-1)
        if (nums[0] == 0):
            return "0";
        return "".join([str(num) for num in nums])


if __name__ == "__main__":
    solution = Solution()
    print(solution.largestNumber([0, 0]))
    print(solution.largestNumber([3, 30, 34, 5, 9]))
