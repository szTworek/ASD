from zad7testy import runtests

def maze(L):
    n=len(L)
    T=[[-1 for _ in range(n)] for _ in range(n)]
    T[0][0]=0
    i=1
    while i<n and L[i][0]!='#':
        T[i][0]=T[i-1][0]+1
        i+=1
    for c in range(1,n):
        for r in range(0,n):
            val = T[r][c - 1]
            if val==-1:
                continue
            x=r
            val_up=val
            while x>-1 and L[x][c]!='#':
                val_up+=1
                T[x][c]=max(T[x][c],val_up)
                x-=1
            x=r
            val_down=val
            while x<n and L[x][c]!='#':
                val_down+=1
                T[x][c]=max(T[x][c],val_down)
                x+=1

    return T[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( maze, all_tests = True )
