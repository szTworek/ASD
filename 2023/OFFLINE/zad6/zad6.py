from zad6testy import runtests
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
    while BFS(G,s,t,parent):
        current_flow=float('inf')
        current=t
        while current!=s:
            current_flow=min(current_flow,G[parent[current]][current])
            current=parent[current]
        max_flow+=current_flow
        v=t
        while v!=s:
            u=parent[v]
            G[u][v]-=current_flow
            G[v][u]+=current_flow
            v=parent[v]
    return max_flow
def binworker( M ):
    n=len(M)
    newM=[[0 for _ in range(2*n+2) ] for _ in range(2*n+2)]
    for i in range(1,n+1):
        newM[0][i]=1
        newM[n+i][2*n+1]=1
    for i in range(1,n+1):
        x=0
        while x<len(M[i-1]):
            newM[i][M[i-1][x]+n+1]=1
            x+=1

    return EdmondsKarp(newM,0,2*n+1)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( binworker, all_tests = True )
