class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def FoundIsland(row, col):
            if grid[row][col] == '1':
                grid[row][col] = '0'
                if row>0:
                    FoundIsland(row-1, col)
                if row<rows-1:
                    FoundIsland(row+1, col)
                if col>0:
                    FoundIsland(row, col-1)
                if col<cols-1:
                    FoundIsland(row, col+1)
                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    FoundIsland(row, col)
                    count += 1
                    
        return count
                
                
        
                
            
        