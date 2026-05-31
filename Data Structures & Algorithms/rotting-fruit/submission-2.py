class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r,c))

        length = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                directions = [[0,1], [0,-1], [1,0], [-1, 0]]

                for dr, dc in directions:
                    rows = r + dr
                    cols = c + dc
                    if rows < 0 or cols < 0 or rows == ROWS or cols == COLS or (rows, cols) in visit or grid[rows][cols] != 1:
                        continue
                    grid[rows][cols] = 2
                    visit.add((rows, cols))
                    q.append((rows, cols))
            if q:
                length +=1

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    return -1

        return length

        
        