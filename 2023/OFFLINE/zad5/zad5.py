from zad5testy import runtests

from queue import PriorityQueue
def neighbor_list(E,S, n):
    G=[[] for _ in range(n)]
    for e in E:
        u,v,w=e
        G[u].append([v,w])
        G[v].append([u,w])

    for i in range(len(S)):
        for j in range(i+1,len(S)):
            if i==j:
                continue
            G[S[i]].append([S[j],0])
            G[S[j]].append([S[i], 0])


    return G

def Dijkstra(G,s):
    def Relax(u,v,w):
        if distance[v]>distance[u]+w:
            distance[v]=distance[u]+w
            parent[v]=u
            queue.put((distance[v],v))
    n=len(G)
    distance=[float('inf') for _ in range(n)]
    parent=[None for _ in range(n)]
    queue=PriorityQueue()
    distance[s]=0
    queue.put((0,s))
    while not queue.empty():
        u=queue.get()[1]
        for v,w in G[u]:
            Relax(u,v,w)

    return distance

def spacetravel(n, E, S, a, b):
    G=neighbor_list(E,S,n)
    distance=Dijkstra(G,a)
    if distance[b]!=float('inf'):
        return distance[b]
    else:
        return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = False )