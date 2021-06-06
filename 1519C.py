#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    u=LI()
    s=LI()
    us=[[] for i in range(n+1)]
    l=[0 for i in range(n+1)]

    for i in range(n):
        us[u[i]]+=[s[i]]
        l[u[i]]+=1

    for i in range(1,n+1):
        us[i]=sorted(us[i],reverse=True)
        for j in range(1,l[i]):
            us[i][j]+=us[i][j-1]

    ans=[0 for i in range(n)]
    for i in range(1,n+1):
        for j in range(1,l[i]+1):
            ind=l[i]-(l[i]%j)-1
            ans[j-1]+=us[i][ind]


    print(*ans)




