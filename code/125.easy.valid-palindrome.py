# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ''.join(c for c in s.lower() if c.isalnum())

        n = len(cleaned)
        if n == 1:
            return True
        if n % 2:
            i = n//2-1
            j = i+2
        else:
            i = n//2-1
            j = i+1
        while i >= 0:
            if cleaned[i] != cleaned[j]:
                return False
            i -= 1
            j += 1

        return True


print(Solution().isPalindrome("race a car"))
print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
print(Solution().isPalindrome(" "))
print(Solution().isPalindrome("ab"))
print(Solution().isPalindrome("0P"))

