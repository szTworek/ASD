# Szymon Tworek
# 1. Pierwszym krokiem jest zliczenie ilości występowania danych liczb z przedziału [1,n] na obu współrzędnych dla
#     każdego punktu do list C1 i C2;
# 2. Przekształcenie wyników w listach C1 i C2 na sumy prefixowe;
# 3. Korzystając ze wzoru P[i] = C1[P[i][0] - 1] + C2[P[i][1] - 1] - n + 1 wyliczamy wartosci dla kazdego punktu,
#     a następnie zwracamy najwiekszą wartość która jest maksymalną liczbą punktów zdominowanych przez jeden punkt.
# 4. Szacowana złożoność algorytmu to O(n).

from zad3testy import runtests


def dominance(P):
  n = len(P)
  C1 = [0] * (n + 1)
  C2 = [0] * (n + 1)
  for i in range(n):
    C1[P[i][0]] += 1
  for i in range(1, n + 1):
    C1[i] += C1[i - 1]
  for i in range(n):
    C2[P[i][1]] += 1
  for i in range(1, n + 1):
    C2[i] += C2[i - 1]

  for i in range(n):
    P[i] = C1[P[i][0] - 1] + C2[P[i][1] - 1] - n + 1

  return max(P)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( dominance, all_tests = True )
