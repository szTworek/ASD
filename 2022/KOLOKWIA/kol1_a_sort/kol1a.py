from kol1atesty import runtests

def MergeSort(A):
    n=len(A)
    if n>1:
        i=n//2
        L=A[:i]
        R=A[i:]
        MergeSort(L)
        MergeSort(R)
        j=k=0
        while j<i and k<n-i:
            if L[j]<=R[k]:

                A[j+k]=L[j]
                j+=1
            else:
                A[j+k]=R[k]
                k+=1
        while j<i:
            A[j+k]=L[j]
            j+=1
        while k<n-i:
            A[j+k]=R[k]
            k+=1

def g(T):
    n=len(T)
    A=[]
    for i in range(n):
        word=T[i]
        for j in range(len(word)//2):
            if ord(word[j])>ord(word[-j-1]):
                A.append(word)
                break
            elif ord(word[j])<ord(word[-j-1]):
                A.append(word[::-1])
                break
        else: A.append(word)
    m=len(A)
    MergeSort(A)
    strongest=current=1
    for i in range(1,m):
        if A[i]==A[i-1]:
            current+=1
        else:
            if current>strongest:
                strongest=current
            current=1
    return strongest



# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )
