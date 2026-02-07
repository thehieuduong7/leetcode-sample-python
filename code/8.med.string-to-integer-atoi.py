class Solution:
    def myAtoi(self, s: str) -> int:
        if (s == ""):
            return 0
        start_index = 0
        end_index = len(s)-1
        while (start_index <= end_index and s[start_index] == " "):
            start_index += 1
        while (start_index <= end_index and s[end_index] == " "):
            end_index -= 1
        s = s[start_index: end_index+1]
        is_pos = True
        num = 0
        i = 0
        # check sign
        while (i < len(s) and s[i] in ["-", "+"]):
            is_pos = is_pos if s[i] == "+" else not is_pos
            i += 1
            break
        s = s[i:]
        i = 0
        while (i < len(s) and s[i] == "0"):
            i += 1
        s = s[i:]

        MAX_NUM = 2**31-1
        MIN_NUM = -2**31

        count = 0

        for i in s:
            if i <= "9" and i >= "0":
                num = num*10 + int(i)
                count += 1
                if (count > 8):
                    temp = num if is_pos else -num
                    if temp > MAX_NUM:
                        return MAX_NUM
                    elif temp < MIN_NUM:
                        return MIN_NUM
            else:
                break

        return num if is_pos else -num


if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi(" "))
    # print(solution.myAtoi("  21474836460  "))
    # print(solution.myAtoi("  -91283472332  "))

    # print(2**31-1)
"""

        for i in s:
        if is_head:
        if i == "-":
            is_pos = not is_pos
            s=s[1:]
        elif i == "0" and is_head:
            continue
        elif i <= "9" and i>="1":
            num = num*10 + int(i)
            is_head = False
        else:
            break;
    else:
        if i <= "9" and i>="1":
            num = num*10 + int(i)
        else:
            break;
"""
