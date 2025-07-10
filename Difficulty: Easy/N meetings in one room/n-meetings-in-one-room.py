#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        result=[]
        result=list(zip(start,end))
        result.sort(key=lambda x:(x[1],x[0]))
        count=1
        last_time=result[0][1]
        n=len(result)
        for i in range(1,n):
            if result[i][0]>last_time:
                count+=1
                last_time=result[i][1]
    
        return count