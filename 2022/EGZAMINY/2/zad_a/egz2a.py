from egz2atesty import runtests


def coal(A, T):
    n=len(A)
    M=[T for i in range(n)]

    for i in range(n):
        j=0
        while  A[i]>M[j]:
            j+=1
        M[j]-=A[i]
        if i==n-1:
            res=j
    return res





# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
