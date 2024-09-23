from zad9testy import runtests

from collections import deque

def BFS(G,s,t,parent):
    queue=deque()
    n=len(G)
    visited=[False for _ in range(n)]
    queue.append(s)
    visited[s]=True
    while queue:
        u=queue.popleft()
        if u==t: return True
        for v in range(n):
            if not visited[v] and G[u][v]!=0:
                parent[v]=u
                if v==t:
                    return True
                visited[v]=True
                queue.append(v)
    return visited[t]

def EdmondsKarp(G,s,t):
    max_flow=0
    n=len(G)
    parent=[-1 for _ in range(n)]
    graph = [row[:] for row in G]
    while BFS(graph,s,t,parent):
        current_flow=float('inf')
        current=t
        while current!=s:
            current_flow=min(current_flow,graph[parent[current]][current])
            current=parent[current]
        max_flow+=current_flow
        v=t
        while v!=s:
            u=parent[v]
            graph[u][v]-=current_flow
            graph[v][u]+=current_flow
            v=parent[v]
    return max_flow

def maxflow( G,s ):
    maxi = 0
    for i, j, k in G: maxi = max(max(maxi, i), j )
    n = maxi+2
    newG = [[0]*n for _ in range(n)]
    for skad, dokad, ile in G:
        newG[skad][dokad] = ile

    n-=1
    res = 0
    for i in range(n):
        for j in range(i+1, n):
            if i != s and j != s and i != j:
                newG[i][n], newG[j][n] = float('inf'), float('inf')
                currflow = EdmondsKarp(newG, s, n)
                res = max(res, currflow)
                newG[i][n] = newG[j][n] = 0
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxflow, all_tests = True )