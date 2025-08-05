import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, V, edges, src):
        # code here
        distance=[float('inf') for _ in range(V)]
        adj_lst=[[] for _ in range(V)] 
        distance[src]=0
        priority_queue=[[src,0]]
        
        for u,v,d in edges:
            adj_lst[u].append([v,d])
        
        while priority_queue:
            curr,dist=heapq.heappop(priority_queue)
            for node,weight in adj_lst[curr]:
                dist_trav=dist+weight
                if dist_trav < distance[node]:
                    distance[node]=dist_trav
                    priority_queue.append([node,dist_trav])
                    
        return distance