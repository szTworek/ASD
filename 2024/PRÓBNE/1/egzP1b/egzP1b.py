from egzP1btesty import runtests 

from queue import PriorityQueue
def graph(G):

    n=0
    for i in range(len(G)):
        n=max(n,G[i][0],G[i][1])
    n+=1
    newG=[[] for _ in range(n)]
    for v1,v2,w in G:
        newG[v1].append([v2,w])
        newG[v2].append([v1,w])
    return newG



def turysta(G,D,L):
    G=graph(G)
    def Dijkstra():
        nonlocal D,L
        def Relax(v1,v2,w,visit):
            nonlocal L
            if v2==L:
                if distance[v2][visit]>distance[v1][visit]+w:
                    distance[v2][visit]=distance[v1][visit]+w
                return
            if distance[v2][visit+1]>distance[v1][visit]+w:
                distance[v2][visit + 1] = distance[v1][visit] + w
                q.put((distance[v2][visit+1],visit+1,v2))
        n=len(G)
        distance=[[float('inf') for _ in range(4)] for _ in range(n)]
        visited=[[False for _ in range(4)] for _ in range(n)]
        distance[D][0]=0
        for i in range(3):
            visited[D][i+1]=True
            visited[L][i]=True

        q=PriorityQueue()
        q.put((0,0,D))
        while not q.empty():
            dist,visit,v1=q.get()
            for v2,w in G[v1]:
                if visit==3 and v2!=L:
                    continue
                if visit==3 or not visited[v2][visit+1]:
                    Relax(v1,v2,w,visit)
            visited[v1][visit]=True
        return distance

    return Dijkstra()[L][-1]

runtests ( turysta )