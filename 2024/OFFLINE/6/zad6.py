from zad6testy import runtests
from queue import PriorityQueue
def make_graph(G):

    n=len(G)
    newG=[[] for _ in range(2*n)]
    for i in range(n):
        for j in range(i,n):
            if G[i][j]!=0:
                newG[2*i].append([2*j,G[i][j]])
                newG[2*j].append([2*i,G[i][j]])
    pom = [row[:] for row in newG]
    for i in range(0,2*n,2):
        for v,w in pom[i]:

            for u,ww in pom[v]:
                if u!=i:
                    newG[i].append([u+1,max(w,ww)])
    for i in range(1,2*n,2):
        newG[i]=pom[i-1]
    return newG

def Dijkstra(G,s):
    def Relax(u,v,w):
        if distance[v]>distance[u]+w:
            distance[v]=distance[u]+w

            queue.put((distance[v],v))
    n=len(G)
    distance=[float('inf') for _ in range(n)]

    queue=PriorityQueue()
    distance[s]=0
    queue.put((0,s))
    while not queue.empty():
        u=queue.get()[1]
        for v,w in G[u]:
            Relax(u,v,w)

    return distance

def jumper( G, s, w ):
    newG=make_graph(G)
    result=Dijkstra(newG,2*s)

    return min(result[2*w],result[2*w+1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( jumper, all_tests = True )