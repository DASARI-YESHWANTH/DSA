class Solution(object):
    def rearrangeArray(self, nums):
        l=len(nums)
        result=[0]*l
        p,n=0,1
        for i in range(l):
            if nums[i]>0 :
                result[p]=result[p]+nums[i]
                p=p+2

            else:
                result[n]=result[n]+nums[i]
                n=n+2
    
        return result
            