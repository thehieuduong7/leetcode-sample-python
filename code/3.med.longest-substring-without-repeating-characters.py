# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

# class Solution:
#     """
#     """

#     def lengthOfLongestSubstring(self, s: str) -> int:
#         i, j = 0, 0
#         n = len(s)
#         current_char = {}
#         max_size = 0
#         while (j < n):
#             if (current_char.get(s[j])):
#                 current_char.pop(s[i])
#                 i += 1
#             else:
#                 current_char[s[j]] = 1
#                 j += 1
#                 max_size = max(max_size, j-i)

#         return max_size

class Solution:
    """
    """

    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        last_seen = {}
        max_size = 0
        for r, char in enumerate(s):
            if char in last_seen and last_seen[char] >= l:
                l = last_seen[char]+1
            last_seen[char] = r
            max_size = max(max_size, r-l+1)

        return max_size


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("abcabcbb"))  # Expected output: 3
    print(solution.lengthOfLongestSubstring("bbbbb"))  # Expected output: 1
