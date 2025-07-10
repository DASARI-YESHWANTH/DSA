class Solution:
    def fractionalknapsack(self, val, wt, capacity):
        #code here
        n=len(val)
        items=list(zip(val,wt))
        items.sort(key = lambda x:x[0]/x[1],reverse= True)
    
        total_val=0.0
        for val,wt in items:
            if capacity>=wt:
                total_val+=val
                capacity-=wt
            else:
                cost=(capacity/wt)*val
                total_val+=cost
                break
        return total_val