# https://leetcode.com/problems/text-justification/description/
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        lines = [[words[0]]]
        i = j = 1
        while (i < len(words)):
            last_line = lines[-1]
            current_size = sum([len(word) for word in last_line])
            if (current_size + len(last_line) + 1 + len(words[i]) <= maxWidth + 1):
                last_line.append(words[i])
            else:
                lines.append([words[i]])
            i += 1

        def justify(line: List[str], maxWidth: int, left_justify=True):
            if left_justify or len(line) == 1:
                temp = " ".join(line)
                if (len(temp) > maxWidth):
                    temp = temp[: -1]
                else:
                    temp = temp + " "*(maxWidth-len(temp))
                return temp

            len_text = sum([len(word) for word in line])
            fill_width = maxWidth - len_text
            size_space = fill_width//(len(line)-1)
            mod_space = fill_width % (len(line)-1)
            for i in range(len(line)-1):
                line[i] = line[i] + " "*size_space
            for i in range(mod_space):
                line[i] = line[i] + " "
            return "".join(line)
        ans = []
        for i in range(len(lines)):
            ans.append(justify(lines[i], maxWidth, i == len(lines)-1))
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.fullJustify(
        ["What","must","be","acknowledgment","shall","be"], 16))
    print(solution.fullJustify(["Science", "is", "what", "we", "understand", "well", "enough", "to",
                                "explain", "to", "a", "computer.", "Art", "is", "everything", "else", "we", "do"],
                               20))
