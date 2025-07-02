#User function Template for python3

class Solution:
    def printGfg(self, n):
        def gfg(i):
            if i>n:
                return
            print("GFG",end=" ")
            gfg(i+1)
        return gfg(1)