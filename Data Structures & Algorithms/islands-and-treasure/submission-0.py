class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS = len(grid)
        COLS = len(grid[0])
        visit = set()
        q = deque()
        INF = 2147483647

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
        distance = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()

                neighbours = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in neighbours:
                    nr = r + dr
                    nc = c + dc
                    if (nr < 0 or nc <0 or nr >= ROWS or nc >= COLS or grid[nr][nc] != INF or (nr, nc) in visit):
                        continue
                    grid[nr][nc] = distance +1
                    q.append((nr, nc))
                    visit.add((nr, nc))
            distance +=1


        
        