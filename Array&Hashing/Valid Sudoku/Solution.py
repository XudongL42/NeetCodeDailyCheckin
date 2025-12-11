class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate cols
        for i in range(9):
            check_dup = set()
            for j in range(9):
                if board[i][j] != "." and board[i][j] in check_dup:
                    return False
                check_dup.add(board[i][j])

        # validate rols
        for i in range(9):
            check_dup = set()
            for j in range(9):
                if board[j][i] != "." and board[j][i] in check_dup:
                    return False
                check_dup.add(board[j][i])

        # validate subbox
        for n in range(3):
            for m in range(3):
                check_dup = set()
                for i in range(3):
                    for j in range(3):
                        cur_element = board[i+3*n][j+3*m]
                        if cur_element != "." and cur_element in check_dup:
                            return False
                        check_dup.add(cur_element)

        return True