class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        nums[:]=nums[n-k:]+nums[0:n-k]
        return nums
        
    