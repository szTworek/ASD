# Szymon Tworek
# Poczatkowo tworzona jest podtablica Tpom zawierajaca p elementów z ktorych wybrany zostanie k-ty najwiekszy element.
# Nastepnie tablica jest sortowana, co pomaga w pozniejszej zamianie elementow w podtablicy.
# W petli za pomoca binary search szukny jest elemement do usuniecia a takze miejsce w ktorym powinien znalezc
# sie dodany elemement.
# Szacowana złożoność czasowa tego algorytmu to O(np)
# Szacowana złożoność pamięciowa tego algorytmu to O(p)
from zad2testy import runtests

def partition(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i+=1
            A[i],A[j]=A[j],A[i]
    A[i+1],A[r]=A[r],A[i+1]
    return i+1


def quicksort(A,p,r):
    if p<r:
        q=partition(A,p,r)
        quicksort(A,p,q-1)
        quicksort(A,q+1,r)

def binary_search_insert(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return left

def ksum(T,k,p):
    Tpom=T[:p]

    quicksort(Tpom,0,p-1)
    result=Tpom[p-k]
    for i in range(0,len(T)-p):
        Tpom.pop(binary_search_insert(Tpom,T[i]))
        Tpom.insert(binary_search_insert(Tpom,T[i+p]),T[i+p])
        result+=Tpom[p-k]
    return result




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
