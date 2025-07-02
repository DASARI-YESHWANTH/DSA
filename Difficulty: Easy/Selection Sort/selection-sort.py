class Solution: 
    def selectionSort(self, arr):
        
        l=len(arr)
        for i in range(l):
            min_index=i
            for j in range(i+1,l):
                if arr[min_index]>arr[j]:
                    min_index=j
                    
            arr[i],arr[min_index]=arr[min_index],arr[i]
        return arr