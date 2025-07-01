class Solution:
    def reverse(self, x) :
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        res = 0

        while x != 0:

           if x > 0 :
            pop = x % 10 
            x = x // 10
            res=res*10+pop
           
           else:
            pop= x % -10
            x = (x - pop) // 10
            res=res*10+pop

        if res > INT_MAX :
                return 0
        elif res < INT_MIN:
                return 0
        else:
            return res
            

        
