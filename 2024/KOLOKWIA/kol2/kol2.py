from kol2testy import runtests

from queue import PriorityQueue
def dijkstra(G, s, t):
    q = PriorityQueue()
    dist = [[float("inf") for _ in range(17)] for __ in range(len(G))]
    for i in range(17):  # inicjalizacja dystansu w wierzchołku startowym
        dist[s][i] = 0

    def relax(u, v, weight, energy):
        if weight > energy:  # gdy brakuje nam energii zeby przejść do v
            if dist[u][energy] + weight + 8 < dist[v][16 - weight]:
                dist[v][16 - weight] = dist[u][energy] + weight + 8
                q.put((dist[v][16 - weight], v, 16 - weight))
        else:
            if dist[u][energy] + weight < dist[v][energy - weight]:
                dist[v][energy - weight] = dist[u][energy] + weight
                q.put((dist[v][energy - weight], v, energy - weight))

    q.put((0, s, 16))  # (distance,vertice,energy)
    visited = [[False for _ in range(17)] for __ in range(len(G))]
    while not q.empty():
        d, u, energy = q.get()
        if visited[u][energy]:
            continue
        visited[u][energy] = True
        for v, weight in G[u]:
            relax(u, v, weight, energy)
    return min(dist[t])
def warrior(G,s,t):
    n=0
    for i in range(len(G)):
        n=max(n,G[i][0],G[i][1])
    n+=1
    pom=[[] for _ in range(n)]
    for e in G:
        v1,v2,w=e
        pom[v1].append([v2,w])
        pom[v2].append([v1,w])
    return dijkstra(pom,s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( warrior, all_tests = True )
