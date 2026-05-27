class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for r in range(9):
            dup = set()
            for c in range(9):
                
                if board[r][c] == ".":
                    continue
                if board[r][c] in dup:
                    return False
                dup.add(board[r][c])


        for c in range(9):
            dup = set()
            for r in range(9):
       
                if board[r][c] == ".":
                    continue
                if board[r][c] in dup:
                    return False

                dup.add(board[r][c])

        for i in range(0, 9, 3):
            for j in range(0,9,3):
                seen = set()
                for x in range(3):
                    for y in range(3):
                        if board[i+x][j+y] in seen:
                            return False
                        if board[i+x][j+y] == ".":
                            continue
                        seen.add(board[i+x][j+y])

        return True
                
        