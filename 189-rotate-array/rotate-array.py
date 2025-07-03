class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        # nums[:]=nums[n-k:]+nums[0:n-k]
        # return nums
        def reverse(arr,l,r):
            while l<r:
                arr[l], arr[r] = arr[r], arr[l]
                l += 1
                r -= 1
        reverse(nums,n-k,n-1)    
        reverse(nums,0,n-k-1)
        reverse(nums,0,n-1)
        return nums
    
