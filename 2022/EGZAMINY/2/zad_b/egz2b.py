from egz2btesty import runtests

def magic(C):
    n=len(C)
    DP=[-1 for _ in range(n)]
    DP[0]=0
    for i in range(n-1):
        chest=C[i][0]
        if DP[i]==-1:
            continue
        for j in range(1,4):
            room=C[i][j][1]
            if room<i:
                continue
            gold=C[i][j][0]
            if DP[i]+chest<gold or room==-1 or chest-gold>10:
                continue
            if chest>=gold:
                plus=chest-gold
                plus=min(plus,10)

                DP[room]=max(DP[room],DP[i]+plus)
            else:
                minus=gold-chest
                DP[room]=max(DP[room],DP[i]-minus)



    return DP[n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True)
