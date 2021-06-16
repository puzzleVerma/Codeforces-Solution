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
    c=LI()
    a=LI()
    b=LI()
    frd=[0 for i in range(n-2)]
    en=[0 for i in range(n-1)]
    for i in reversed(range(2,n)):
        frd[i-2]=c[i-1]-1
        frd[i-2]-=abs(b[i]-a[i])

    for i in reversed(range(1,n)):
        en[i-1]=abs(b[i]-a[i])
    # print(frd)
    # print(en)
    ans=0
    temp=c[-1]-1
    for i in reversed(range(1,n-1)):
        temp+=2
        ans=max(ans,temp+en[i])
        if en[i]==0:
            temp=c[i]-1
            continue
        temp+=frd[i-1]
        temp=max(temp,c[i]-1)
        # print(ans,temp)
    temp+=2
    temp+=en[0]
    ans=max(ans,temp)
    print(ans)
