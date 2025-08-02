from collections import deque
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        queue=deque()
        result=[]
        v=len(graph)
        adj_lst=[[] for _ in range(v)]
        indegrees=[0]*v

        for node in range(v):
            for i in graph[node]:
                adj_lst[i].append(node)
                indegrees[node]+=1
        for j in range(v):
            if indegrees[j]==0:
                queue.append(j)
        while queue:
            curr=queue.popleft()
            result.append(curr)
            for node in adj_lst[curr]:
                indegrees[node]-=1
                if indegrees[node]==0:
                    queue.append(node)
        result.sort()
        return result