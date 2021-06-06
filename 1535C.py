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
    s=S()
    s=list(s)
    ans=1
    cur=1
    q=0
    l=len(s)
    if l==1:
        print(1)
        continue
    if s[0]=="?":
        ck=-1
        q+=1
    elif s[0]=="0":
        ck=1
    else:
        ck=2

    for i in r(1,l):
        if s[i]=="?":
            q+=1
            if ck!=-1:
                ck+=1
            cur+=1
            ans+=cur
        else:
            if (s[i-1]=="?"):
                if ck==-1:
                    cur+=1
                elif (str(ck%2)==s[i]):
                    cur+=1
                else:
                    cur=1+q
            else:
                if (s[i]!=s[i-1]):
                    cur+=1
                else:
                    cur=1
            ck=int(s[i])+1
            q=0
            ans+=cur

    print(ans)