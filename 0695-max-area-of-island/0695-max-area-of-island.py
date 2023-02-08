class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def scan(row, col):
            if not(0<=row<rows and 0<=col<cols and (row,col) not in visited and grid[row][col]):
                return 0
            visited.add( (row,col) )
            return ( 1 +scan(row+1,col)+scan(row-1,col)+scan(row,col+1)+scan(row,col-1) )
        
        return max(scan(row,col)
                  for row in range(rows)
                  for col in range(cols))
                        
                
                
                
        