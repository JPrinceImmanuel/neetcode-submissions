class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        for i in range(len(board)):
            seen = set()
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in seen:
                        return False
                    seen.add(board[i][j])
            
       
        for y in range(len(board[0])):
            seen2 = set()
            for x in range(len(board)):
                if board[x][y] != ".":
                    if board[x][y] in seen2:
                        print(x)
                        print(y)
                        return False
                    seen2.add(board[x][y])
        print("GI")
        def cal(a,b):
            seen3 = set()
            for i in range(3):
                for j in range(3):
                    if board[a+i][b+j] != ".":
                        if board[a+i][b+j] in seen3:
                            return False
                        seen3.add(board[a+i][b+j])
            
            return True

        for x in range(0, 9, 3):
            for y in range(0, 9, 3):
                ans = cal(x,y)
                if ans == False:
                    return False                                  
        

        return True

        