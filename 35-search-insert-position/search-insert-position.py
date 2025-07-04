class Solution(object):
    def searchInsert(self, nums, target):
        l=len(nums)
        s=0
        e=l-1
        index=-1
        while s<=e:
            mid=(s+e)//2
            if nums[mid]<target:
                index=max(index,mid)
                s=mid+1
                
            elif nums[mid]==target:
                return mid
            
            else:
                e=mid-1
        return index+1
# class Solution(object):
#     def searchInsert(self, nums, target):
#         s = 0
#         e = len(nums) - 1
#         index = len(nums)

#         while s <= e:
#             mid = (s + e) // 2  # fix here: use 'e' instead of 'l'
#             if nums[mid] >= target:
#                 index = mid
#                 e = mid - 1
#             else:
#                 s = mid + 1

#         return index
