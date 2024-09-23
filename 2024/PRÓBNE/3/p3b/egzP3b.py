from egzP3btesty import runtests 
from queue import PriorityQueue


def Prim(G):
    n = len(G)
    visited = [False for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = PriorityQueue()  # queue=[waga,wierzcholek1,wierzcholek2]
    MST = []
    visited[0] = True
    for v1, w in G[0]:
        queue.put([-w, 0, v1])
    while not all(visited):
        w, v1, v2 = queue.get()
        w = -w
        if visited[v2] == False:
            MST.append([v1, v2, w])
            visited[v2] = True

            for v3, w_prim in G[v2]:
                if visited[v3] == False:
                    queue.put([-w_prim, v2, v3])
                    parent[v3] = v2
    return MST


def lufthansa(G):
    MaxST = Prim(G)
    flight = 0
    for v1, v2, w in MaxST:
        G[v1].remove((v2, w))
        G[v2].remove((v1, w))
    redundant = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            redundant = max(redundant, G[i][j][1])

    for i in range(len(G)):
        for j in range(len(G[i])):
            if G[i][j][0] > i:
                flight += G[i][j][1]
    flight -= redundant

    return flight

runtests ( lufthansa, all_tests=True )