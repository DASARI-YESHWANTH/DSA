class Solution(object):
    def rearrangeArray(self, nums):
        arr1=[]
        arr2=[]
        arr3=[]
        l=len(nums)
        for i in range(l):

            if nums[i]>0:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])
        for i in range(len(arr1)+len(arr2)):
            if i%2==0:
                arr3.append(arr1[i//2])
            else:
                arr3.append(arr2[i//2])
        nums[:]=arr3
        return nums