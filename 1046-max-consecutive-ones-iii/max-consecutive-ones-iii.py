class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxi=0
        l=0
        r=0
        n=len(nums)
        zeros=0
        while r<n:
            if nums[r]==0:
                zeros+=1
            if zeros>k:
                if nums[l]==0:
                    zeros-=1
                l=l+1
            if zeros<=k:
                maxi=max(maxi,r-l+1)
            r=r+1
        return maxi
