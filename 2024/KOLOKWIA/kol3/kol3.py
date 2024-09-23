from kol3testy import runtests


def orchard(T,m):
    n=len(T)
    DP=[[float('inf') for _ in range(m)] for _ in range(n)]
    DP[0][0]=1
    DP[0][T[0]%m]=0
    for row in range(n-1):
        for col in range(m):
            if DP[row][col]!=float('inf'):
                DP[row+1][(col+T[row+1])%m]=min(DP[row][col],DP[row+1][(col+T[row+1])%m])
                DP[row+1][col]=min(DP[row+1][col], DP[row][col]+1)

    return DP[n-1][0]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(orchard, all_tests=True)
