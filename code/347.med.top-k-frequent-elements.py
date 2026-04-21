from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        for i in nums:
            countDict[i] = countDict.get(i, 0) + 1

        reverseCountDict = {}
        for key, value in countDict.items():
            if value in reverseCountDict:
                reverseCountDict[value].append(key)
            else:
                reverseCountDict[value] = [key]

        sortedValues = sorted(reverseCountDict.keys(), reverse=True)

        sortedKey = []
        for i in sortedValues:
            sortedKey += reverseCountDict.get(i, [])

        return sortedKey[0: k]


print(Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2))

print(Solution().topKFrequent([1], 2))

print(Solution().topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
