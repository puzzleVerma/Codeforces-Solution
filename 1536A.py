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
    arr.sort()
    if arr[0]<0:
        print("NO")
    else:
        ll=arr[-1]
        print("YES")
        print(ll+1)
        ans=[int(i) for i in range(ll+1)]
        print(*ans)