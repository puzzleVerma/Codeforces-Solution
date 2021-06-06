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
    s=S()
    sp=[]
    for i in range(n):
        if s[i]=="*":
            sp+=[i+1]
    spl=(len(sp))
    mid=spl//2
    ans=0
    for i in range(spl):
        ans+=(abs(sp[mid]-sp[i])-abs(mid-i))
    print(ans)


