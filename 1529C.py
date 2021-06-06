#######puzzleVerma#######


import sys
input=sys.stdin.readline


IN=lambda:int(input())
r=range

test=IN()
for t in r(test):
    n=IN()
    ltree=[0]*n
    rtree=[0]*n

    for i in r(n):
        a,b=map(int,input().split())
        ltree[i]=a
        rtree[i]=b

    dd=[[] for i in r(n)]
    for i in r(n-1):
        a,b=map(int,input().split())
        a-=1
        b-=1
        dd[a].append(b)
        dd[b].append(a)
    q=[0]
    p=[-1]*n
    p[0]=n
    check=[]
    while q:
        c=q.pop()
        check.append(c)
        for i in dd[c]:
            if p[i]==-1:
                p[i]=c
                q.append(i)

    dpl=[0.0]*n
    dpr=[0.0]*n
    for i in check[1:][::-1]:
        par=p[i]
        dpl[par]+=max(dpl[i]+abs(ltree[par]-ltree[i]),dpr[i]+abs(ltree[par]-rtree[i]))
        dpr[par]+=max(dpl[i]+abs(rtree[par]-ltree[i]),dpr[i]+abs(rtree[par]-rtree[i]))
    print(int(max(dpl[0],dpr[0])))





# import sys
# import io, os
# input=sys.stdin.readline
# t=int(input())
# for tests in range(t):
#     n=int(input())
#     L=[0]*n
#     R=[0]*n
#     for i in range(n):
#         l,r=map(int,input().split())
#         L[i]=l
#         R[i]=r
#     E=[[] for i in range(n)]
#     for i in range(n-1):
#         x,y=map(int,input().split())
#         x-=1
#         y-=1
#         E[x].append(y)
#         E[y].append(x)

#     ROOT=0

#     QUE=[ROOT] 
#     Parent=[-1]*(n+1)
#     Parent[ROOT]=n
#     TOP_SORT=[]

#     while QUE:
#         x=QUE.pop()
#         TOP_SORT.append(x)
#         for to in E[x]:
#             if Parent[to]==-1:
#                 Parent[to]=x
#                 QUE.append(to)

#     DPL=[0.0]*n
#     DPR=[0.0]*n
#     #print(Parent)
#     #print(TOP_SORT)
#     for x in TOP_SORT[1:][::-1]:
#         p=Parent[x]

#         DPL[p]+=max(DPL[x]+abs(L[p]-L[x]),DPR[x]+abs(L[p]-R[x]))
#         DPR[p]+=max(DPL[x]+abs(R[p]-L[x]),DPR[x]+abs(R[p]-R[x]))

#     print(int(max(DPL[0],DPR[0])))
