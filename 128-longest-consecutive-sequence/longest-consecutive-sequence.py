class Solution(object):
    def longestConsecutive(self, nums):
        nums.sort()

        cnt=1
        mcnt=1
        if nums==[]:
            return 0
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                if nums[i]==nums[i-1]+1 :
                    cnt+=1
                    mcnt=max(mcnt,cnt)

                else:
                    cnt=1




        # arr=[]
        # hash={}
        # l=len(nums)
        # for i in range(l):
        #     if nums[i] in hash:
        #         hash[nums[i]]+=1
        #     else:
        #         hash[nums[i]]=0
        # for i in hash:
        #     arr.append(i) 
        # arr.sort()
        # cnt=1
        # mcnt=1
        # if len(arr)==1:
        #     return 1
        # elif arr==[]:
        #     return 0
        # for i in range(1,len(arr)):
        #     if arr[i]-arr[i-1]==1 :
        #         cnt+=1
        #         mcnt=max(cnt,mcnt)
        #     else:
        #         cnt=1
        return mcnt