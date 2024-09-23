from zad7testy import runtests


def macierz(G):
    n=len(G)
    graf=[[-1 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for x in range(2):
            j=0
            while j<len(G[i][x]):
                graf[i][G[i][x][j]]=x
                j+=1
    return graf




def droga(G):

    pom=[]
    def parenttab(parent,x):
        if x==0:

            return pom
        pom.append(x)
        return parenttab(parent,parent[x])
    G=macierz(G)
    def DFS_visit(G,u,v,licz):

        n=len(G)
        visited[u]=True
        parent[u]=v
        wyjscie = 0
        if wyjscie == G[u][v]:
            wyjscie += 1
        if licz==n:

            for i in range(n):
                if visited[i]==False:
                    return
            if G[u][0]==wyjscie:

                parent[0]=u
                return True
        if v == -1:
            for i in range(n):
                if G[u][i]!=-1:
                    # print(parent)
                    if DFS_visit(G,i,u,licz+1)==True:
                        return True
        else:

            for i in range(n):
                if G[u][i]==wyjscie and visited[i]==False:
                    if DFS_visit(G,i,u,licz+1)==True:
                        return True
        visited[u]=False
        return False






    n=len(G)

    parent=[None for _ in range(n)]

    visited = [False for _ in range(n)]

    if DFS_visit(G,0,-1,1)==True:

        result=parenttab(parent,parent[0])

        result.append(0)
        result.reverse()
        return result

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( droga, all_tests = True)