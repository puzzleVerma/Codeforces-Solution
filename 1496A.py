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
    n,k=LI()
    s=S()
    ans="YES"
    for i in range(k):
        if s[i]!=s[n-1-i]:
            ans="NO"
            break
    if 2*k+1>n:
        ans="NO"
    
    print(ans)