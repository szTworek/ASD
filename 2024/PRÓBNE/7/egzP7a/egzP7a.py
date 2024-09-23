from egzP7atesty import runtests 

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


def akademik(T):
    n=len(T)
    def graf():
        n=len(T)

        G=[[0 for _ in range(2*n+2)] for _ in range(2*n+2)]
        v=2*n+2
        # 0 - wierzcholek bufor
        # 1 -> n indeksy po jednej stronie grafu
        # n+1 -> 2*n indeksy po drugiej stronie grafu
        # 2*n+1 - koncowy wierzcholek bufor
        for i in range(n):
            # if n>=i>0:
            #     G[0][i]=1
            # if n<i<2*n+1:
            #     G[2*n+1][i]=1
            G[0][i+1]=1
            G[n+1+i][2*n+1]=1
        los=0
        for i in range(n):
            flag=False
            for j in range(3):
                if T[i][j]==None:
                    continue
                flag=True
                G[i+1][n+1+T[i][j]]=1
            if flag==False:
                los+=1

        return G,los

    G,los=graf()
    # print(G)
    max_flow=EdmondsKarp(G,0,(2*n)+1)
    # print(max_flow)
    res=n-max_flow-los
    return res

runtests ( akademik )