from egzP1atesty import runtests 

def titanic(W,M,D):

    morse=[]

    for i in range(len(W)):
        for j in range(len(M)):
            if W[i]==M[j][0]:
                x=0
                while x<len(M[j][1]):
                    morse.append(M[j][1][x])
                    x+=1
    D.remove(4)
    D.remove(19)
    n=len(morse)
    przedzial=[]
    for ind,l in enumerate(D):

        for i in range(n):
            if len(M[l][1])+i>n:
                continue
            x=0
            flag=False
            while x<len(M[l][1]) and M[l][1][x]==morse[i+x]:
                x+=1
            if x==len(M[l][1]):
                flag=True
            if flag==True:
                przedzial.append([i,i+x-1])
    przedzial.sort(key=lambda x:x[1])
    DP=[0 for i in range(n)]
    x=0


    for i in range(n):
        DP[i]=DP[i-1]+1
        while x<len(przedzial) and i==przedzial[x][1]:
            DP[i]=min(DP[i],DP[przedzial[x][0]-1]+1)
            x+=1

    return DP[n-1]

runtests ( titanic, recursion=False )