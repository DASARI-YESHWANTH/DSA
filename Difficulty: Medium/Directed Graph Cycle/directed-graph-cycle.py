class Solution:
    def isCycle(self, V, edges):
        # code here
        result=[]
        queue=deque()
        indegrees=[0]*V
        adj_lst=[[] for _ in range(V)]
        for u,v in edges:
            adj_lst[u].append(v)
            indegrees[v]+=1
        
        for i in range(V):
            if indegrees[i]==0:
                queue.append(i)
        while queue:
            curr=queue.popleft()
            result.append(curr)
            for node in adj_lst[curr]:
                indegrees[node]-=1
                if indegrees[node]==0:
                    queue.append(node)
        if len(result)!=V:
            return True
        return False