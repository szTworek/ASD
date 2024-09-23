from egz1btesty import runtests
from collections import deque
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = None       # pole do wykorzystania przez studentow

def BFS_list(G,s):
    n=len(G)
    visited=[False for _ in range(n)]
    distance=[-1 for _ in range(n)]
    parent=[None for _ in range(n)]
    queue=deque()
    queue.append(s)
    visited[s]=True
    distance[s]=0
    while queue:
        curr=queue.popleft()
        for i in G[curr]:
            if visited[i]==False:
                queue.append(i)
                visited[i]=True
                distance[i]=distance[curr]+1
                parent[i]=curr
    #print(distance)
    return max(distance)

def graph(A):
    G=[[]]
    index=0
    def rek(A,ind):
        nonlocal G,index


        if A.left!=None:
            index+=1
            G[ind].append(index)
            G.append([])
            rek(A.left,index)

        if A.right!=None:
            index+=1
            G[ind].append(index)
            G.append([])
            rek(A.right,index)

    rek(A,0)
    return G

def wideentall(T):
    G=graph(T)
    n=BFS_list(G,0)+1
    #print(G)
    #print(n)
    szer=[0 for _ in range(n)]
    def DFS_visit(v,poz):
        szer[poz]+=1
        for e in G[v]:
            DFS_visit(e,poz+1)
    DFS_visit(0,0)
    #print(szer)
    ladne=0

    for i in range(n):
        if szer[i]>=ladne:
            ladne=szer[i]
            poziom=i
    res=0
    okej=[False for _ in range(len(G))]
    okej[0]=True
    def DFS_visit2(v,poz):
        nonlocal res
        if poz==poziom:
            res+=len(G[v])
            G[v]=[]
            #print(len(G[v]),v,poziom,poz)
            okej[v]=True
            return True
        else:
            for e in G[v]:
                if DFS_visit2(e,poz+1):
                    okej[v]=True
                elif okej[v]!=True:
                    okej[v]=False
            return okej[v]
    def delete(v):
        nonlocal res
        for e in G[v]:
            if okej[e]==False:
                res+=1
                continue
            delete(e)



    DFS_visit2(0,0)
    delete(0)
    #print(okej)
    return res

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )