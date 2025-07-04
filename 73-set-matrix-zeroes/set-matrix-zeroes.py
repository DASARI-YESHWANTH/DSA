class Solution(object):
    def setZeroes(self, matrix):
        m=len(matrix)
        n=len(matrix[0])
        
        def zeros(matrix,row,col):
            m=len(matrix)
            n=len(matrix[0])
            for i in range(m):
                if matrix[i][col] !=0:
                    matrix[i][col]=float('inf')
            for i in range(n):
                if matrix[row][i] !=0:
                    matrix[row][i]=float('inf')
            
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    zeros(matrix,i,j)

        for i in range(m):
            for j in range(n):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=0
        return matrix