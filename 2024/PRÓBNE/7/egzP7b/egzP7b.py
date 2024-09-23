from egzP7btesty import runtests 
	
def ogrod(S,V):
    n=len(S)
    res=0
    DP=[[0 for _ in range(n)] for _ in range(n)]
    for p in range(n):
        Val=V[:]
        for k in range(p,n):
            DP[p][k]=DP[p][k-1]+Val[S[k]-1]
            if Val[S[k]-1]>0:
                Val[S[k]-1]=-Val[S[k]-1]
            else:
                Val[S[k]-1]=0
            res=max(res,DP[p][k])
    return res
    
runtests(ogrod, all_tests = True)