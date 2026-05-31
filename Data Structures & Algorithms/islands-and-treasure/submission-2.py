class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r,c))
        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1], [0,-1], [1,0], [-1, 0]]

                for dr, dc in directions:
                    rows = r + dr
                    cols = c + dc
                    if rows < 0 or cols < 0 or rows == ROWS or cols == COLS or (rows, cols) in visit or grid[rows][cols] != 2147483647:
                        continue
                    grid[rows][cols] = length + 1
                    visit.add((rows, cols))
                    q.append((rows, cols))

            length +=1
                    



        