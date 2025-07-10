#User function Template for python3

class Solution:
    def minPartition(self, N):
        supply=[ 1, 2, 5, 10, 20, 50, 100, 200, 500, 2000 ]
        i=len(supply)-1
        lst=[]
        while N>0:
            if supply[i]>N:
                i=i-1
            else:
                N-=supply[i]
                lst.append(supply[i])
        return lst