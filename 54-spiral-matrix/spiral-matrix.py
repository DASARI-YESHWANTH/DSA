class Solution(object):
    def spiralOrder(self, matrix):
        result=[]
        m=len(matrix)
        n=len(matrix[0])
        t=0
        l=0
        b=m-1
        r=n-1
        while t<=b and l<=r:
            for i in range(l,r+1):
                result.append(matrix[t][i])
            t+=1
            for i in range(t,b+1):
                result.append(matrix[i][r])
            r-=1
            if t<=b:
                for i in range(r,l-1,-1):
                    result.append(matrix[b][i])
                b-=1
            if l<=r:
                
                for i in range(b,t-1,-1):
                    result.append(matrix[i][l])
                l+=1
        return result
            
            
