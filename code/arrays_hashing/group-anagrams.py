from typing import List
# https://leetcode.com/problems/group-anagrams/


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = {}
        for i in strs:
            key = "".join(sorted(i))
            if result.get(key):
                result[key].append(i)
            else:
                result[key] = [i]

        return list(result.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


print(Solution().groupAnagrams([""]))



print(Solution().groupAnagrams(["a"]))
