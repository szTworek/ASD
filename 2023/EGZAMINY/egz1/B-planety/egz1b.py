from egz1btesty import runtests

def planets( D, C, T, E ):
    n=len(D)
    DP=[[float('inf') for _ in range(n)] for _ in range(E+1)]
    for i in range(E+1):
        DP[i][0]=C[0]*i
    if T[0][0]!=0:
        DP[0][T[0][0]]=T[0][1]

    for p in range(1,n):
        dist=D[p]-D[p-1]

        if dist>E:
            continue
        DP[0][p] = min(DP[0][p], DP[0 + dist][p - 1])
        for e in range(1,E+1):
            if E>=dist+e:
                DP[e][p]=min(DP[e][p],DP[e+dist][p-1],DP[e-1][p]+C[p])
            else:
                DP[e][p]=min(DP[e][p],DP[e-1][p]+C[p])
        if T[p][0] != p:
            DP[0][T[p][0]] = min(T[p][1]+DP[0][p],DP[0][T[p][0]])
    res=float('inf')
    for i in range(E+1):
        res=min(res,DP[i][n-1])
    return res
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
