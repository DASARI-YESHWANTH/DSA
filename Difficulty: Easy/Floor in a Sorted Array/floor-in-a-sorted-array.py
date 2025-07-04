class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self, arr, x):
        s=0
        e=len(arr)-1
        index=-1
        while s<=e:
            mid=(s+e)//2
            
            if x>=arr[mid]:
                index=max(mid,index)
                s=mid+1
                 
            else:
                e=mid-1
        return index
            