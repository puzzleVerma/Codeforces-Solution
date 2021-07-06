#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

def lcm(a,b):
    hcf=math.gcd(a,b)
    pro=a*b
    return pro//hcf

for t in r(IN()):
    n=IN()
    ans=n*2
    ans%=mod
    div=2
    ind=3
    while div<=n:
        ans+=(n//div)
        ans%=mod
        div=lcm(div,ind)
        ind+=1
    print(ans)


