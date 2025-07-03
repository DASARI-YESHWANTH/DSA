class Solution(object):
    def missingNumber(self, nums):
        # largest=nums[0]
        # for i in range(1,len(nums)):
        #     largest=max(largest,nums[i])
        for i in range (0,len(nums)+1):
            if i not in nums:
                return i

        