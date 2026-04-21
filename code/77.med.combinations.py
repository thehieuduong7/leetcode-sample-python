from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        temp = [i+1 for i in range(k)]
        ans = [temp.copy()]

        def generate():
            i = k-1
            while(i>=0 and temp[i]==n-k+i+1):
                i=i-1
            if i < 0:
                return True;
            else:
                temp[i]+=1
                for j in range(k-i-1):
                    temp[i+j+1] = temp[i]+j+1
                return False

        while(not generate()):
            ans.append(temp.copy())

        return ans




if __name__ == "__main__":
    solution = Solution()
    print(solution.combine(5,3))
