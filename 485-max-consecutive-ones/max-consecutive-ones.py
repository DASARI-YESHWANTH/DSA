class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        cnt=0
        mcnt=0
        for i in range(len(nums)):
            if nums[i]==1:
                cnt+=1
            else:
                mcnt=max(mcnt,cnt)
                cnt=0


        return max(mcnt,cnt)