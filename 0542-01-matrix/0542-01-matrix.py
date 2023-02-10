class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        
        rows = len(mat)
        cols = len(mat[0])
        
        for row in range(rows):
            for col in range(cols):
                if mat[row][col] > 0:
                    top = mat[row-1][col] if row-1 >= 0 else math.inf
                    left= mat[row][col-1] if col-1 >= 0 else math.inf
                    mat[row][col] = min( top+1, left+1)
                    
        for row in range(rows-1, -1, -1):
            for col in range(cols-1, -1, -1):
                if mat[row][col] > 0:
                    bottom = mat[row+1][col] if row+1 < rows else math.inf
                    right= mat[row][col+1] if col+1 < cols else math.inf
                    mat[row][col] = min( mat[row][col], bottom+1, right+1)
                    
        
                    
                
        return mat
                
                
            
        