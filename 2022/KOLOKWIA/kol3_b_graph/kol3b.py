from kol3btesty import runtests

from queue import PriorityQueue


def airports(G, A, s, t):
    G.append([])
    n = len(G)
    for i in range(n-1):
        G[i].append((n-1, A[i]))
        G[n-1].append((i, A[i]))

    def Dijkstra(G, s):
        def Relax(u, v, w):
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                parent[v] = u
                queue.put((distance[v], v))

        n = len(G)
        distance = [float('inf') for _ in range(n)]
        parent = [None for _ in range(n)]
        queue = PriorityQueue()
        distance[s] = 0
        queue.put((0, s))
        while not queue.empty():
            u = queue.get()[1]
            for v, w in G[u]:
                Relax(u, v, w)

        return distance

    result = Dijkstra(G, s)
    return result[t]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )