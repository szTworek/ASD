from kol2atesty import runtests

def drivers(P,B):
    n=len(P)
    T=[]
    P=[[P[i][0],P[i][1],i] for i in range(n)]
    P.sort(key=lambda x:x[0])
    j=0
    for i in range(n):
        if  P[i][1]==True and P[i][0]<B:
            T.append([P[i][2],0])
            x=i+1
            while x<n and P[x][0]<B and P[x][1]==False:
                T[j][1]+=1
                x+=1
            j+=1
    T.append([n+1,0])

    DP=[[[float('inf'),None] for _ in range(len(T))] for _ in range(2)]

    DP[0][0]=[0,None]
    DP[0][1]=[0,None]
    DP[0][2]=[0,None]
    #wiersz 0 to jacek
    #wiesz 1 to marian
    t=len(T)
    ile=T[0][1]
    x=1
    while x<4 and x<t:
        DP[1][x]=[ile,0]
        ile+=T[x][1]
        x+=1

    for i in range(1,t):

        ile=DP[0][i][0]+T[i][1]
        x=1
        while x < 4 and i+x < t:
            if ile<DP[1][i+x][0]:
                DP[1][i+x] = [ile, i]
            ile += T[i+x][1]
            x += 1
        ile=DP[1][i][0]
        x=1
        while x<4 and i+x<t:
            if ile<DP[0][i+x][0]:
                DP[0][i+x]=[ile,i]
            x+=1


    def odczyt():
        res=[]
        if DP[0][-1][0]<DP[1][-1][0]:
            first=DP[0][-1][1]
            kierowca=0
        else:
            first=DP[1][-1][1]
            kierowca=1

        def rek(i,kier):
            if i==None:
                return
            res.append(T[i][0])
            rek(DP[abs(kier-1)][i][1],abs(kier-1))
        rek(first,kierowca)
        return res
    result=odczyt()
    result.reverse()
    return result

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( drivers, all_tests = True )