class Solution(object):
    def rotate(self,nums,k):
        n=len(nums)
        nums[:]=nums[n-k:n]+nums[:n-k]
    def search(self, nums, target):
        l=0
        h=len(nums)-1
        while l<=h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[l]<=nums[mid]:
                    if nums[l]<=target<=nums[mid]:
                        h=mid-1
                    else:
                        l=mid+1
                else:
                    if nums[mid]<=target<=nums[h]:
                        l=mid+1
                    else:
                        h=mid-1



        return -1
        
        