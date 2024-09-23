from kol2testy import runtests


def modG(G):
    n=len(G)
    newG=[]

    for i in range(n):
        j=0
        while j < len(G[i]):
            newG.append([i, G[i][j][0], G[i][j][1]])
            j+=1
    newG.sort(key=lambda x:x[2])
    i=1
    while i<len(newG):
        newG.pop(i)
        i+=1
    return newG

def beautree(G):
    def ismst(parent):
        x = Find(0)
        for i in range(len(parent)):
            if Find(i) != x:
                return False
        return True
    G=modG(G)

    GS=sorted(G,key= lambda x:x[2])
    n=max(max(G[i][0],G[i][1]) for i in range(len(G)))+1


    def Find(v):
        if parent[v]!=v:
            parent[v]=Find(parent[v])
        return parent[v]

    def Union(v1,v2):
        v1=Find(v1)
        v2=Find(v2)
        if v1==v2:
            return
        elif rank[v1]>rank[v2]:
            parent[v2]=v1
        else:
            parent[v1]=v2
            if rank[v1]==rank[v2]:
                rank[v2]+=1
    for i in range(len(G)):
        mst = []
        res=0
        parent = [x for x in range(n)]
        rank = [0 for _ in range(n)]
        for e in range(i,len(G)):
            v1,v2,w=GS[e]
            if Find(v1)!=Find(v2):
                res+=w
                mst.append([v1,v2,w])
                Union(v1, v2)
            elif Find(v1)==Find(v2):
                Union(v1, v2)
                if ismst(parent) == False:
                    res=None
                    break
                else:
                    return res

            else:
                return res
        if res!=None and ismst(parent)==True:
            print(res)
            return res
    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( beautree, all_tests = True )
