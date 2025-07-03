class Solution(object):
    def maxSubArray(self, nums):
        n=len(nums)
        maxi=float("-inf")
        total=0
        if n==1:
            return nums[0]
        for i in range(n):
            total=total+nums[i]
            maxi=max(maxi,total)
            if total<0:
                total=0
            
        return maxi