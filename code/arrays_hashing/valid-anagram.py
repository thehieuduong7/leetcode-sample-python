class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_dict = {}
        for i in s:
            if (char_dict.get(i)):
                char_dict[i] += 1
            else:
                char_dict[i] = 1

        for i in t:
            if (char_dict.get(i) != None):
                char_dict[i] -= 1
            else:
                return False

        for i in char_dict.values():
            if i != 0:
                return False

        return True
