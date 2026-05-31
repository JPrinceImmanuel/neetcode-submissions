class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0
        max_area = 0
        visit = set()
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visit and grid[r][c] == 1:
                    res = self.dfs(r, c, grid, visit)
                    
                    
                    max_area= max(res, max_area)
                    

        return max_area


    def dfs(self, r, c, grid, visit):

        if r <0 or c< 0 or r == len(grid) or c == len(grid[0]) or (r, c) in visit or grid[r][c] == 0:
            return 0


        visit.add((r, c))
        return (1+
        self.dfs(r+1, c, grid, visit)+
        self.dfs(r-1, c, grid, visit)+
        self.dfs(r, c+1, grid, visit)+
        self.dfs(r, c-1, grid, visit)
        )