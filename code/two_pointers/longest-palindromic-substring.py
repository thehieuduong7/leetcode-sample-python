class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        f = [[True]*n for _ in range(n)]
        for i in range(2, n):
            for j in range:


# print(Solution().longestPalindrome("babad"))
print(Solution().longestPalindrome("bananas"))

# print(Solution().longestPalindrome("cxaabacxcabaaxcabaaxd"))
