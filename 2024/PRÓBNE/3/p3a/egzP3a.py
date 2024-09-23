from egzP3atesty import runtests
from math import inf

class Node:
  def __init__(self, wyborcy, koszt, fundusze):
    self.next = None
    self.wyborcy = wyborcy 
    self.koszt = koszt 
    self.fundusze = fundusze 
    self.x = None

def wybory(T):
    m=len(T)
    TT=[[] for _ in range(m)]
    for i in range(m):
        p=T[i]
        while p!=None:
            TT[i].append((p.wyborcy,p.koszt,p.fundusze))
            p=p.next
    DP=[[[0 for _ in range(TT[i][0][2]+1) ] for _ in range(len(TT[i]))] for i in range(m)]
    for i in range(m):
        fundusze=TT[i][0][2]
        for n in range(len(TT[i])):
            for p in range(fundusze+1):
                okrag=TT[i][n]
                koszt=okrag[1]
                wyborcy=okrag[0]
                if koszt>p:
                    DP[i][n][p]=DP[i][n-1][p]
                    continue
                if n==0:
                    DP[i][n][p]=wyborcy
                    continue

                DP[i][n][p]=max(wyborcy+DP[i][n-1][p-koszt],DP[i][n-1][p])
    res=0
    for i in range(m):
        res+=DP[i][-1][-1]
    return res

runtests(wybory, all_tests = True)