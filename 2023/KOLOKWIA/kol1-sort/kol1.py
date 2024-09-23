from kol1testy import runtests

def ksum(T,k,p):
    n=len(T)
    P=[]
    sum=0
    for i in range(p):
        P.append(T[i])
    P.sort()
    sum+=P[-k]


    for i in range(n-p):
        P.remove(T[i])
        P.append(T[i+p])
        wstawiany = T[i+p]
        j = p-2
        while j >= 0 and P[j] > wstawiany:
            P[j + 1] = P[j]
            j -= 1
        P[j + 1] = wstawiany
        sum+=P[-k]
    return sum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ksum, all_tests=True )
