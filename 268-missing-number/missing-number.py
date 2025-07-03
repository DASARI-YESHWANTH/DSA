class Solution(object):
    def missingNumber(self, nums):
        l=len(nums)
        sum1=sum(nums)
        sum2=0.5*l*(l+1)
        return int(sum2)-sum1

        