from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        result=0
        queue=deque()
        indegrees=[0]*numCourses
        adj_lst=[[] for _ in range(numCourses)]
        for u,v in prerequisites:
            adj_lst[v].append(u)
            indegrees[u]+=1
        
        for i in range(numCourses):
            if indegrees[i]==0:
                queue.append(i)
            
        while queue:
            curr=queue.popleft()

            result+=1
            for node in adj_lst[curr]:
                indegrees[node]-=1
                if indegrees[node]==0:
                    queue.append(node)
    
        return result==numCourses
            
        