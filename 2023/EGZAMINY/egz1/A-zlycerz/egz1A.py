from egz1Atesty import runtests

from queue import PriorityQueue

def gold(G,V,s,t,r):
    n=len(G)
    def Dijkstra1(s): # koszt jaki rycerz ponosi docierajac do kazdego z wierzcholkow przed obrabowaniem zamku
        def Relax(v1,v2,w):
            if distance[v2]>distance[v1]+w:
                distance[v2]=distance[v1]+w
                q.put((distance[v2],v2))
        q=PriorityQueue()
        n=len(G)

        distance=[float('inf') for _ in range(n)]
        distance[s]=0
        q.put((0,s))
        while not q.empty():
            v1=q.get()[1]
            for v2,w in G[v1]:
                Relax(v1,v2,w)
        return distance
    przed=Dijkstra1(s)
    def Dijkstra2(s,r):
        def Relax(v1,v2,w):
            if distance[v2]>distance[v1]+w+r:
                distance[v2]=distance[v1]+w+r
                q.put((distance[v2],v2))
        q=PriorityQueue()
        n=len(G)

        distance=[float('inf') for _ in range(n)]
        distance[s]=0
        q.put((0,s))
        while not q.empty():
            v1=q.get()[1]
            for v2,w in G[v1]:
                w*=2
                Relax(v1,v2,w)
        return distance
    po=Dijkstra2(t,r)
    result=[None for _ in range(n)]
    for i in range(n):
        result[i]=przed[i]+po[i]-V[i]
    return min(result)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )
