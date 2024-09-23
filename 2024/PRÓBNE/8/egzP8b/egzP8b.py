from egzP8btesty import runtests


def floyd_warshall(G):
    n=len(G)
    parent=[[None for _ in range(n)] for _ in range(n)]
    distance=[[float('inf') for _ in range(n)] for _ in range(n)]
    for v1 in range(n): # przekształcenie z listy sasiedztwa na macierz odleglosci pomiedzy kazdym wierzcholkiem
        distance[v1][v1]=0
        for x in G[v1]:
            v2,w=x
            distance[v1][v2]=w
            parent[v1][v2]=v1
    for k in range(n):
        for v1 in range(n):
            for v2 in range(n):
                if distance[v1][v2]>distance[v1][k]+distance[k][v2]:
                    distance[v1][v2]=distance[v1][k]+distance[k][v2]
                    parent[v1][v2]=parent[k][v2]

    return distance

def robot(G,P):
    G=floyd_warshall(G)
    res=0
    for i in range(1,len(P)):
        res+=G[P[i-1]][P[i]]
    return res
    
runtests(robot, all_tests = True)
