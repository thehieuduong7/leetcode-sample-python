

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        cols = []
        dg = []
        udg = []
        board = [["."]*n for i in range(n)]
        ans = []
        def backtracking(row: int):
            if row == n:
                copy_board = ["".join(row_board) for row_board in board]
                ans.append(copy_board)
                return

            for j in range(n):
                sum_dg=row+j
                minus_udg=row-j
                if (j in cols or sum_dg in dg or minus_udg in udg):
                    continue

                cols.append(j);
                dg.append(sum_dg)
                udg.append(minus_udg)
                board[row][j]='Q'

                backtracking(row+1)

                cols.remove(j);
                dg.remove(sum_dg)
                udg.remove(minus_udg)
                board[row][j]='.'

        backtracking(0)
        return ans



if __name__ == "__main__":
    print(Solution().solveNQueens(4))
    # print(conflict_location(l1,l2))
