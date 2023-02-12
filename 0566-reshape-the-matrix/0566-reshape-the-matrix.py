class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        cols = len(mat[0])
        
        if rows*cols != r*c:
            return mat
        
        new_mat = [[0 for i in range(c)] for j in range(r)]
        i = 0
        j = 0
        for row in mat:
            for element in row:
                new_mat[i][j] = element
                j += 1
                if j >= c:
                    j = 0
                    i += 1
        
        return new_mat
        