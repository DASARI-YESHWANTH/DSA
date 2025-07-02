class Solution:
    def largest(self, arr):
        
        lar=arr[0]
        
        for i in range(len(arr)):
            lar=max(lar,arr[i])
        return lar
        
