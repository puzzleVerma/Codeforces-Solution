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
    arr=[int(i+1) for i in range(n)]
    ans=[0]*n
    if (n%2):
        for i in range(n-1):
            if i%2==0:
                ans[i]=arr[i+1]
            else:
                ans[i]=arr[i-1]
        ans[-1]=arr[-1]
        ans[-1],ans[-2]=ans[-2],ans[-1]
    else:
        for i in range(n):
            if i%2==0:
                ans[i]=arr[i+1]
            else:
                ans[i]=arr[i-1]
    print(*ans)