class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visit = set()
        length = 0


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    queue.append((r,c))

        while queue:
            for _ in range(len(queue)):
                r, c = queue.popleft()

                neighbours = [[0,1], [0, -1], [1, 0], [-1, 0]]
                for dr, dc in neighbours:
                    rows = r+ dr
                    cols = c + dc
                    if rows < 0 or cols <0 or rows == ROWS or cols == COLS or grid[rows][cols] != 2147483647 or (rows, cols) in visit:
                        continue
                    grid[rows][cols] = length +1
                    queue.append((rows, cols))
                    visit.add((rows, cols))

            length +=1

                    



        