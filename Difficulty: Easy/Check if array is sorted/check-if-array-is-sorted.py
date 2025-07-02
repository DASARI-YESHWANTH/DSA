class Solution:
    def arraySortedOrNot(self, arr) -> bool:
        l=len(arr)
        for i in range (l-1):
                if arr[i]>arr[i+1]:
                    return False
        return True