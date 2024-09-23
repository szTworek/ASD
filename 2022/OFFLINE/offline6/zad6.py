from collections import deque
from zad6testy import runtests



def BFS_list(G, s, t):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [-1 for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = deque()
    queue.append(s)
    visited[s] = True
    distance[s] = 0
    while queue:
        curr = queue.popleft()
        for i in G[curr]:

            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[curr] + 1
                parent[i] = curr

    return parent, distance[t]


def mod_BFS(G, s, t, remove):
    n = len(G)
    visited = [False for _ in range(n)]
    distance = [float('inf') for _ in range(n)]
    parent = [None for _ in range(n)]
    queue = deque()
    queue.append(s)
    visited[s] = True
    distance[s] = 0
    while queue:
        curr = queue.popleft()
        for i in G[curr]:
            if (curr == remove[0] and i == remove[1]) or (curr == remove[1] and i == remove[0]):
                continue
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                distance[i] = distance[curr] + 1
                parent[i] = curr

    return distance[t]



def longer(G, s, t):
    tab = []

    def path(v, parent):
        if parent[v] == None:
            return
        tab.append((v,parent[v]))
        path(parent[v], parent)



    parent, shortest = BFS_list(G, s, t)
    path(t, parent)

    for i in tab:
        print(i)
        without = mod_BFS(G, s, t, i)
        if without == None or shortest < without:
            return i
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )