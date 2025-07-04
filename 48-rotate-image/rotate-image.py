class Solution(object):
    def rotate(self, matrix):
        
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                if i != j:
                    matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        # return matrix
        # # transpose(matrix)
        # # i=0
        for i in range(n):
            for j in range(n//2):
                    matrix[i][j],matrix[i][n-1-j]=matrix[i][n-1-j],matrix[i][j]
            i+=1
        return matrix
