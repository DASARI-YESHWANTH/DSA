class Solution:
    def frequencyCount(self, arr):
        hash={}
        arr1=arr.sort()
        arr2=[]
        for i in range (0,len(arr)):
            hash[arr[i]]=hash.get(arr[i],0)+1
       
        # if 1 in hash.keys():     
        #     arr2.append(hash[arr[1]])
        # else:
        #     arr2.append(0)
        for j in range (0,len(arr)):
            if j+1 in hash.keys():
                arr2.append(hash[j+1]) 

            
            else:
                arr2.append(0)
        
                
        return arr2

