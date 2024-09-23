from kolutesty import runtests

def ice_cream( T ):
    T.sort(reverse=True)
    res=0
    min=0
    for i in range(len(T)):
        if T[i]-min<=0:
            break
        res+=T[i]-min
        min+=1


    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( ice_cream, all_tests = True )
