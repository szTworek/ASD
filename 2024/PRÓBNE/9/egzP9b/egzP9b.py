from egzP9btesty import runtests
import sys
sys.setrecursionlimit(100000)

def DFS(G,d):
    result=[]
    def DFS_visit(G,u):


        for i in range(len(G[u])):
            if d[u][i]==False:
                d[u][i]=True
                DFS_visit(G,G[u][i])
                result.insert(0,G[u][i])
    DFS_visit(G,0)
    return [0]+result

def dyrektor(G,R):
    for i in range(len(R)):

        for j in range(len(R[i])):
            G[i].remove(R[i][j])
    d=[[] for _ in range(len(G))]
    for i in range(len(G)):
        for j in range(len(G[i])):
            d[i].append(False)


    res=DFS(G,d)
    return res
	
runtests(dyrektor, all_tests=True)
