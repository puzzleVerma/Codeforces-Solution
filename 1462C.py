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
    if n>45:
        print(-1)
        continue
    elif n<10:
        print(str(n))
        continue
    ans=""
    ele=9
    while n>ele:
        ans+=str(ele)
        n-=ele
        ele-=1

    ans+=str(n)
    ans=list(ans)
    ans.sort()
    print(''.join([ele for ele in ans]))

