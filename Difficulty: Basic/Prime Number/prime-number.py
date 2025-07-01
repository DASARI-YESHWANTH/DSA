from math import *
class Solution:
    def isPrime(self, n):
        cnt=0
        
        if n==1:
            return False
        
        for i in range(1,int(sqrt(n))+1):
            if n%i==0:
                if n//i !=i:
                    cnt=cnt+2
                else:
                    cnt=cnt+1
        if cnt>2:
            return False
        return True