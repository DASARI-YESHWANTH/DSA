from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n=numCourses
        total=0
        result=[]
        adj_lst=[[] for _ in range(n)]
        queue=deque()
        indegrees=[0]*n
        for u,v in prerequisites:
            adj_lst[v].append(u)
            indegrees[u]+=1
        for i in range(n):
            if indegrees[i]==0:
                queue.append(i)
        while queue:
            curr=queue.popleft()
            result.append(curr)
            total+=1
            for node in adj_lst[curr]:
                indegrees[node]-=1
                if indegrees[node]==0:
                    queue.append(node)
        if total != n:
            return []
        return result
        