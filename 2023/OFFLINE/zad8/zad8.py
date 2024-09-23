from zad8testy import runtests

from queue import PriorityQueue


def modification(T):
    n = len(T)
    m = len(T[0])
    parent = [[None for _ in range(m)] for _ in range(n)]
    stain = [0 for _ in range(m)]

    def f(r, c):
        nonlocal n, m
        if r - 1 > -1 and T[r - 1][c] != 0 and parent[r - 1][c] == None:
            parent[r - 1][c] = parent[r][c]
            stain[parent[r][c]] += T[r - 1][c]
            f(r - 1, c)
        if c - 1 > -1 and T[r][c - 1] != 0 and parent[r][c - 1] == None:
            parent[r][c - 1] = parent[r][c]
            stain[parent[r][c]] += T[r][c - 1]
            f(r, c - 1)
        if r + 1 < n and T[r + 1][c] != 0 and parent[r + 1][c] == None:
            parent[r + 1][c] = parent[r][c]
            stain[parent[r][c]] += T[r + 1][c]
            f(r + 1, c)
        if c + 1 < m and T[r][c + 1] != 0 and parent[r][c + 1] == None:
            parent[r][c + 1] = parent[r][c]
            stain[parent[r][c]] += T[r][c + 1]
            f(r, c + 1)

    for i in range(0, m):
        if parent[0][i] == None:
            parent[0][i] = i
            if T[0][i] != 0:
                stain[i] += T[0][i]
                f(0, i)
    return stain


def plan(T):
    stain = modification(T)
    Q = PriorityQueue()
    zasieg = stain[0]
    pos = 1
    n = len(stain)
    result = 1
    if zasieg >= n - 1:
        return result
    while zasieg < n - 1:
        while zasieg >= pos and pos < n - 1:
            Q.put(-stain[pos])
            pos += 1
        tank = Q.get()
        zasieg -= tank
        result += 1
    return result


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True )

