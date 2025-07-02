#User function Template for python3

class Solution:
    def printNos(self, n):
        def gfg(i):
            if i<=0:
                return
            print(i,end=" ")
            gfg(i-1)
        return gfg(n)