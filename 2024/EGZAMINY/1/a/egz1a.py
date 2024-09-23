from egz1atesty import runtests

from queue import PriorityQueue
from math import floor
def newG(G):
    n=0
    for i in range(len(G)):
        n=max(n,G[i][0],G[i][1])

    new=[[] for _ in range(n+1)]
    for i in range(len(G)):
        v1,v2,w=G[i]
        new[v1].append([v2,w])
        new[v2].append([v1,w])


    return new,n+1

def bikes(B,n):
    newB=[1 for _ in range(n)]
    for i in range(len(B)):
        v,p,q=B[i]
        if p/q<1:
            newB[v]=min(p/q,newB[v])
    return newB





def armstrong(B,G,s,t):
    G,n=newG(G)
    B=bikes(B,n)
    def Dijkstra1(s):


        def Relax(u, v, w):
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                queue.put((distance[v], v))

        n = len(G)
        distance = [float('inf') for _ in range(n)]

        queue = PriorityQueue()
        distance[s] = 0
        queue.put((0, s))
        while not queue.empty():
            u = queue.get()[1]
            for v, w in G[u]:
                Relax(u, v, w)

        return distance
    przed=Dijkstra1(s)

    po=Dijkstra1(t)
    res=[float('inf') for i in range(n)]
    for i in range(n):
        res[i]=przed[i]+(po[i]*B[i])
    return floor(min(res))

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( armstrong, all_tests = True )
