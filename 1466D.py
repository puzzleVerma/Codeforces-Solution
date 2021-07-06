#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range


for t in r(IN()):
    n=IN()
    weight=[0]
    weight+=LI()
    deg=[-1 for i in range(n+1)]
    for i in range(n-1):
        a,b=[int(i) for i in input().split()]
        deg[a]+=1
        deg[b]+=1
    newlist=[[i,j] for i,j in zip(weight,deg)]
    newlist.sort(reverse=True)
    answer=[sum(weight)]
    for i in newlist:
        for j in range(i[1]):
            answer.append(answer[-1]+i[0])
    print(*answer)