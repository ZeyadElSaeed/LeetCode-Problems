class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        if image[sr][sc] == color:
            return image
        
        rows = len(image)
        cols = len(image[0])
        old_color= image[sr][sc]
        
        def bfs(row, col):
            if image[row][col] == old_color:
                image[row][col] = color
                if row > 0:
                    bfs(row - 1, col)
                if row < rows - 1:
                    bfs(row + 1, col)
                if col > 0:
                    bfs(row, col-1)
                if col < cols - 1:
                    bfs(row, col+1)
        bfs(sr, sc)       
        return image
                    
                
        
        
        
        
        
        
        