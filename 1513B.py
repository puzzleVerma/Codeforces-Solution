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
    arr=LI()
    andd=arr[0]
    for ele in arr:
        andd&=ele
    same=0
    for ele in arr:
        if ele==andd:
            same+=1
    if same<=1:
        print(0)
        continue
    else:
        ans=1
        ans*=same
        ans%=mod
        same-=1
        ans*=same
        ans%=mod
        for i in range(1,n-1):
            ans*=i
            ans%=mod
    print(ans)
