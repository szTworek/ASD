from zad8testy import runtests


def parking(X, Y):
  n = len(X)
  m = len(Y)
  DP = [[float('inf') for _ in range(n)] for _ in range(m)]
  q = float('inf')
  for i in range(m):
    q = min(q, abs(X[0] - Y[i]))
    DP[i][0] = q

  for x in range(1, n):
    q = float('inf')
    for y in range(x, m):
      q = min(q, DP[y - 1][x - 1] + abs(X[x] - Y[y]))
      DP[y][x] = q

  q = float('inf')
  for i in range(n - 1, m):
    q = min(q, DP[i][n - 1])
  return q

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( parking, all_tests = True )
