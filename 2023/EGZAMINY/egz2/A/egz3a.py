from egz3atesty import runtests

from queue import PriorityQueue


def modG(G):
  n = len(G)
  newG = [[] for _ in range(n)]
  for i in range(n):
    for j in range(i, n):
      if G[i][j] != -1:
        newG[i].append([j, G[i][j]])
        newG[j].append([i, G[i][j]])
  return newG


def goodknight(G, s, t):
  G = modG(G)

  def Dijkstra():
    nonlocal s, t
    n = len(G)

    def Relax(v1, v2, w, sleep):
      if sleep - w < 0 and distance[16 - w][v2] > distance[sleep][v1] + w + 8:
        distance[16 - w][v2] = distance[sleep][v1] + w + 8
        q.put([distance[16 - w][v2], 16 - w, v2])
      elif sleep - w >= 0 and distance[sleep - w][v2] > distance[sleep][v1] + w:
        distance[sleep - w][v2] = distance[sleep][v1] + w
        q.put([distance[sleep-w][v2], sleep - w, v2])

    q = PriorityQueue()
    distance = [[float('inf') for _ in range(n)] for _ in range(17)]
    distance[16][s] = 0
    q.put([distance[16][s], 16, s])
    while not q.empty():
      d, sleep, v1 = q.get()
      for v2, w in G[v1]:
        Relax(v1, v2, w, sleep)
    res = float('inf')
    for i in range(17):
      res = min(res, distance[i][t])
    return res

  return Dijkstra()
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( goodknight, all_tests = True)
