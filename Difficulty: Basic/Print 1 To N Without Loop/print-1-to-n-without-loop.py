class Solution:    
    def printNos(self,n):
        
        def recurse(i):
        
            if i>n:
                return
            
            print(i,end=" ")
            recurse(i+1)
        return recurse(1)