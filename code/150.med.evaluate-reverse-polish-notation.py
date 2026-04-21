# https://leetcode.com/problems/evaluate-reverse-polish-notation/


"""

    Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22


"""


from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            '+': lambda a, b: a+b,
            '-': lambda a, b: a-b,
            '*': lambda a, b: a*b,
            '/': lambda a, b: int(a/b),
        }
        for token in tokens:
            if token in ('+', '-', '*', '/'):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(operators[token](num1, num2))
            else:
                stack.append(int(token))
        return stack[0]


print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
print(Solution().evalRPN(["10", "6", "9", "3", "+",
      "-11", "*", "/", "*", "17", "+", "5", "+"]))
