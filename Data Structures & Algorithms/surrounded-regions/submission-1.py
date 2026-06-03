class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        q = deque()

        for r in range(rows):
            for c in range(cols):
                if (r == rows -1 or c == cols-1 or r==0 or c==0) and board[r][c] == "O":
                    board[r][c] = "T"
                    q.append((r, c))

        

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1], [1,0], [0,-1], [-1, 0]]
                for dr, dc in directions:
                    nr = r+dr
                    nc = c+dc

                    if nr < 0 or nc < 0 or nr == rows or nc == cols:  # fix 3
                        continue
                    if board[nr][nc] == "O":
                        board[nr][nc] = "T"
                        q.append((nr, nc))

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"

                    

        


        


        

        