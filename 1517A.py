#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for i in range(IN()):
    n=IN()
    if n%2050==0:
        res=n//2050
        res=str(res)
        ans=0
        for ele in res:
            ans+=int(ele)
        print(ans)
    else:
        print(-1)