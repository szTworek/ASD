from zad4testy import runtests

from math import inf


def Flight(L, start, goal, t):

  N = max([u for v, u, p in L]) + 1
  g = [[] for _ in range(N)]
  for x, y, p in L:
    g[x].append((y, p))
    g[y].append((x, p))

  visited = [False] * N

  def dfs(v, lo=-inf, up=inf):
    if v == goal: return True
    visited[v] = True
    for u, p in g[v]:
      if visited[u]: continue
      lo2 = max(lo, p - t)
      up2 = min(up, p + t)
      if lo2 <= up2 and dfs(u, lo2, up2):
        return True
    visited[v] = False
    return False

  r = dfs(start)
  return r


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( Flight, all_tests = True )
