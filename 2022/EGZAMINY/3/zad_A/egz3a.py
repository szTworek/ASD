from egz3atesty import runtests


def snow(T, I):
    newList = []
    for e in I:
        o, z = e
        newList.append((o, 0))
        newList.append((z, 1))
    newList.sort()
    cnt = 0
    res = 0
    for i in newList:
        if i[1] == 0:
            cnt += 1
        else:
            cnt -= 1
        res = max(res, cnt)

    return res




# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = True )
