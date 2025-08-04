from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        # code here
        v=len(adj)
        dist=[-1 for _ in range(v)]
        queue=deque()
        dist[src]=0
        distance=0
        queue.append((src,distance))
        while queue:
            curr,distance_l=queue.popleft()
            for node in adj[curr]:
                if dist[node]== -1:
                    dist[node]=distance_l+1
                    queue.append((node,distance_l+1))
        return dist
