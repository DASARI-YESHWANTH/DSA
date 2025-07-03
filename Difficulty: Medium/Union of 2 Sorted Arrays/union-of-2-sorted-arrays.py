#User function Template for python3

class Solution:
    
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        arr=[]
        
        for i in b:
                a.append(i)
        a.sort()  
        
        i=0
        for j in range(i+1,len(a)):
            if a[i] != a[j]:
                i=i+1
                a[i],a[j]=a[j],a[i]
                
        a[:]=a[:i+1]
        
                
                
        return a
        