class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0  # Pointer for the last unique element
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]  # Move unique element forward
        
        return i + 1  # Length of unique 