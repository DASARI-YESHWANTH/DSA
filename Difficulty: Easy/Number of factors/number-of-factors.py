from math import *
class Solution:
    def countFactors (self, n):
        
        cnt=0
        
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                if n//i !=i:
                    cnt=cnt+2
                else:
                    cnt=cnt+1
        
        return cnt