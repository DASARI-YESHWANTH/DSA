class Solution(object):
    def search(self, nums, target):
        if target not in nums:
            return -1
        s=0
        e=len(nums)-1
        mid=(s+e)//2
        while s<=e:
            mid=(s+e)//2
            if nums[mid]<target:
                s=mid+1
            elif nums[mid]==target:
                return mid
            else:
    
                e=mid-1