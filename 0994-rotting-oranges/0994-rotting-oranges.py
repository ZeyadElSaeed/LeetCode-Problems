class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        rotten_index = []
        fresh_count = 0
        
        #track the number of fresh ones and indices of rotten
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 2:
                    rotten_index.append( (row,col) )
                elif grid[row][col] == 1:
                    fresh_count += 1
        
        minutes = 0
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        #we end if all fresh are rotten or the rotten can't affect the ramainings
        while len(rotten_index)>0 and (fresh_count > 0):
            minutes += 1
            # we loop until queue is empty to endicate one round( minute )
            for i in range(len(rotten_index)):
                rotten_X , rotten_Y = rotten_index.pop(0)   
                for dx, dy in directions:
                    x = rotten_X + dx
                    y = rotten_Y + dy

                    if x<0 or x>= rows or y<0 or y>= cols:
                        continue
                    if grid[x][y] == 0 or grid[x][y] == 2:
                        continue

                    fresh_count -= 1
                    grid[x][y] = 2
                    rotten_index.append( (x,y) )
        
        return minutes if fresh_count == 0 else -1
            
            
            
                    
                    
        