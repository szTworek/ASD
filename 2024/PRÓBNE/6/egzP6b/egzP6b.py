from egzP6btesty import runtests 

def jump(M):
    chess_set = {"UL":(-1,2), "UR":(1,2), "RU":(2,1), "RD":(2,-1), "DR":(1,-2), "DL":(-1,-2), "LD":(-2,-1), "LU":(-2,1)}
    act=(0,0)
    d={act:1}

    for i in M:
        move=chess_set[i]

        act=(act[0]+move[0],act[1]+move[1])
        cond=d.pop(act,0)
        if cond==0:
            d[act]=1

    return len(d)
    
runtests(jump, all_tests = True)