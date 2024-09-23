from egzP6atesty import runtests


def Partition(A,p, r):
    x=A[r][1]
    i=p-1
    for j in range(p,r):
        if A[j][1]>=x:
            i+=1
            A[i],A[j]=A[j],A[i]

    A[i+1],A[r]=A[r],A[i+1]
    return i+1

def QuickSelect(A,p,r,k):

    if p==r :
        return A[p]
    q=Partition(A,p,r)
    if q==k:
        return A[q]
    elif q<k :
        return QuickSelect(A,q+1,r,k)
    else:
        return QuickSelect(A,p,q-1,k)


def letters(x):
    res=0
    for i in range(len(x)):
        if 122>=ord(x[i])>=97:
            res+=1
    return res
def google(H,s):
    n=len(H)
    k=0
    for i in range(n):
        k=max(k,len(H[i]))
    T=[[] for _ in range(k+1)]
    for i in H:
        T[len(i)].append([i,letters(i)])

    for i in range(k,-1,-1):

        if len(T[i])>=s:

            res=QuickSelect(T[i],0,len(T[i])-1,s-1)
            return res[0]
        else:
            s-=len(T[i])


runtests ( google, all_tests=True )