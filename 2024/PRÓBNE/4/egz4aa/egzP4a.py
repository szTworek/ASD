from egzP4atesty import runtests 

def mosty(T):
    n=len(T)
    DP=[[float('inf') for _ in range(n)] for _ in range(n)]
    T.sort()
    for i in range(n):
        DP[i][0]=min(DP[i-1][0],T[i][1])

    res=1
    for m in range(1,n):
        for i in range(m,n):
            DP[i][m]=DP[i-1][m]
            if T[i][1]>DP[i-1][m-1]:


                DP[i][m]=min(T[i][1],DP[i][m])
                res=m


    return res+1

runtests ( mosty, all_tests=True)