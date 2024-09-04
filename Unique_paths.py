def uniquePaths(self, m: int, n: int) -> int:
        '''
        https://leetcode.com/problems/unique-paths/description/
        '''
        grid = [[1]*n for i in range(2)]
        for i in range(1,m):
            for j in range(1,n):
                grid[i&1][j] = grid[(i-1)&1][j] + grid[i&1][j-1]
        return grid[(m-1)&1][-1]
