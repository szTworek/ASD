from egzP2atesty import runtests 

def zdjecie(T,m,k):
    rzedy=[[] for _ in range(m)]
    rzedy[m-1]=k
    for i in range(m-2,-1,-1):
        rzedy[i]=rzedy[i+1]+1
    index=[0 for _ in range(len(rzedy))]
    for i in range(1,len(rzedy)):
        index[i]=rzedy[i-1]+index[i-1]



    T2=T[:]
    T2.sort(key= lambda x:x[1],reverse= True)

    rzad=0
    for i in range(len(T)):

        T[i]=T2[index[rzad]]
        index[rzad]+=1
        rzedy[rzad]-=1
        if rzedy[rzad]==0:
            rzad=-1
            m-=1
        rzad+=1
        if m==0:
            break
        rzad%=m
    return None

runtests ( zdjecie, all_tests=False )