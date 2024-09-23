from egz1atesty import runtests

def snow( S ):
    S.sort(reverse=True)
    dni=0
    res=0
    for i in range(len(S)):
        if S[i]-dni>0:
            res+=S[i]-dni
            dni+=1
        else:break

    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
