#User function Template for python3

class Solution:
    def evenlyDivides(self, n):
        lst=[]
        p=n
        while p>0:
            pop=p%10
            if pop != 0:
                lst.append(pop)
            p=p//10
       
        c=0
        for i in lst:
            if n%i == 0:
                c+=1
        return c