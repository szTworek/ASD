# Szymon Tworek
# 1. pierwotna lista zostaje przekszatłcona na listę zawierającą listy [wartość z T, zliczanie rangi]
# 2. przeksztalcona lista jest przekazywana do funkcji MergeSort ktora sortuje wartosci elementów
# 3. W funkcji Merge jeżeli liczba z "prawej" listy merge'a jest wieksza od tej z "lewej" wtedy współrzedna
# odpowiadająca za zliczanie rangi jest zwiekszana o dlugość "lewej" listy - indeks mniejszego elementu w niej
# 4. po posortowaniu i zliczeninu rang wszystkich elementów wybieramy najwiekszą z rang
# złożoność czasowa algorytmu to O(nlogn)
# zlożoność pamięciowa algorytmu to O(n)

from kol1testy import runtests


def maxrank(T):
  max_ = 0
  for i in range(len(T)):
    T[i] = [T[i], 0]
  MergeSort(T, 0, len(T) - 1)
  for i in range(len(T)):
    max_ = max(T[i][1], max_)
  return max_


def MergeSort(A, p, r):
  if p < r:
    q = (p + r) // 2
    MergeSort(A, p, q)
    MergeSort(A, q + 1, r)
    Merge(A, p, q, r)


def Merge(A, p, q, r):
  n1 = q - p + 1
  n2 = r - q
  L = [0] * (n1 + 1)
  R = [0] * (n2 + 1)
  for i in range(n1):
    L[i] = A[p + i]
  for i in range(n2):
    R[i] = A[q + i + 1]
  L[n1] = [float('-inf'), 0]
  R[n2] = [float('-inf'), 0]
  i = 0
  j = 0
  for k in range(p, r + 1):

    if L[i][0] >= R[j][0]:
      A[k] = L[i]
      i += 1
    else:
      A[k] = R[j]
      if L[i][0] != float('-inf'):
        R[j][1] += len(L) - 1 -i
      j += 1



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maxrank, all_tests = True )
