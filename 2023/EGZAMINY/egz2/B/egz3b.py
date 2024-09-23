from egz3btesty import runtests


def uncool(P):
  n = len(P)
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      if P[i][1] < P[j][0] or P[j][1] < P[i][0] or (P[i][0]>=P[j][0] and P[i][1]<=P[j][1]) or (P[j][0]>=P[i][0] and P[j][1]<=P[i][1]):
        continue
      else:
        return (i, j)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )
