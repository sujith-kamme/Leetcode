def minPathSum(self, grid: List[List[int]]) -> int:
        '''
        https://leetcode.com/problems/minimum-path-sum/
        '''
        m = len(grid)
        n = len(grid[0])

        for i in range(1,m):
            grid[i][0] += grid[i-1][0]
        
        for j in range(1,n):
            grid[0][j] += grid[0][j-1]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]= min((grid[i][j]+grid[i-1][j]), (grid[i][j]+grid[i][j-1]))
        
        return grid[-1][-1]