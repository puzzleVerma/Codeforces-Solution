#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()
r=range

n,k=LI()
s=S()
if n==1:
    print(s*k)
    sys.exit()
lim=n
ref=s[0]
i=1
while i<n:
    if s[i]<ref:
        pass
    elif s[i]>ref:
        lim=i
        break
    else:
        ii=0
        jj=i
        while s[ii]==s[jj]:
            ii+=1
            jj+=1
            if jj==n:
                lim=i
                i=jj
                break
        else:
            if s[ii]<s[jj]:
                lim=i
                i=jj
                break
            else:
                i=jj
                pass
    i+=1
ans=s[:lim]
ans*=(k//lim+1)
ans=ans[:k]
print(ans)

        
        
        
