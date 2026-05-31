class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cols = len(grid[0])
        rows = len(grid)
        visit = set()
        res = 0
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == "1":
                    res +=1
                    self.dfs(r, c, grid, visit)
                    
                    

        return res

    def dfs(self, r, c, grid, visit):


        if r < 0 or c < 0 or r == len(grid) or c == len(grid[0]) or (r, c) in visit or grid[r][c] == "0":
            return 

        visit.add((r, c))

        self.dfs(r+1, c, grid, visit)
        self.dfs(r-1, c, grid, visit)
        self.dfs(r, c+1, grid, visit)
        self.dfs(r, c-1, grid, visit)


        