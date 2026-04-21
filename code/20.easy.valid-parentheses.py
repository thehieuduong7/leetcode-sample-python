# https://leetcode.com/problems/valid-parentheses/description/

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pair = {
            "}": "{",
            ")": "(",
            "]": "["
        }
        for i in s:
            if i in pair:
                if not stack or pair[i] != stack[-1]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return not bool(stack)


print(Solution().isValid("""([)]"""))
print(Solution().isValid("""([])"""))
