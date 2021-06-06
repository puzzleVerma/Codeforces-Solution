#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    a,b=LI()
    t=a+b
    s=S()
    s=list(s)
    flag=1
    if ((a%2==1) and (b%2==1)):
        flag=0
    if flag==0:
        print(-1)
        continue
    aa=0
    ab=0
    for i in range(a+b):
        if s[i]=="0":
            if s[a+b-1-i]=="1":
                flag=0
                break
            aa+=1
        elif s[i]=="1":
            if s[a+b-1-i]=="0":
                flag=0
                break
            ab+=1
    la=a-aa
    lb=b-ab
    if ((la<0) or (lb<0)):
        flag=0
    if flag==0:
        print(-1)
        continue

    for i in range(a+b):
        if s[i]=="?" and s[t-1-i]=="0":
            if la>=1:
                s[i]="0"
                la-=1
            else:
                flag=0
                break
        elif s[i]=="0" and s[t-1-i]=="?":
            if la>=1:
                s[t-1-i]="0"
                la-=1
            else:
                flag=0
                break
        elif s[i]=="?" and s[t-1-i]=="1":
            if lb>=1:
                s[i]="1"
                lb-=1
            else:
                flag=0
                break
        elif s[i]=="1" and s[t-1-i]=="?":
            if lb>=1:
                s[t-1-i]="1"
                lb-=1
            else:
                flag=0
                break
        
    for i in range((t+1)//2):
        if (s[i]=="?" and s[t-1-i]=="?" and i!=(a+b-1-i)):
            if ((la>=lb) and (la>=2)):
                s[i]="0"
                s[t-1-i]="0"
                la-=2
            elif ((lb>=la) and (lb>=2)):
                s[i]="1"
                s[t-1-i]="1"
                lb-=2
            else:
                flag=0
                break
        elif (s[i]=="?" and s[t-1-i]=="?" and i==(a+b-1-i)):
            if ((a%2==1) and (la>=1)):
                s[i]="0"
                la-=1
            elif ((b%2==1) and (lb>=1)):
                s[i]="1"
                lb-=1
            else:
                flag=0
                break
        

    if flag==0:
        print(-1)
        continue
    else:
        for i in range(a+b):
            print(s[i],end="")
        print()