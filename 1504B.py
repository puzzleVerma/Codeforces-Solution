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
    a=S()
    b=S()
    ind=n
    z1=0
    z2=0
    check1=[0 for i in r(n)]
    check2=[0 for i in r(n)]
    for i in r(n):
        if a[i]=="0":
            z1+=1
        if b[i]=="0":
            z2+=1
        if (i%2) and (z1==((i+1)//2)):
            check1[i]=1
        if (i%2) and (z2==((i+1)//2)):
            check2[i]=1
    if z1!=z2:
        print("NO")
        continue
    for i in r(n):
        if a[n-1-i]==b[n-1-i]:
            ind=n-i-1
        else:
            break
    if ind==0:
        print("YES")
        continue
    flag=0
    ans=0
    for i in r(ind):
        if (a[ind-1-i]==b[ind-1-i]):
            if flag==1:
                continue
            if (check1[ind-1-i] and check2[ind-1-i]):
                flag=1
            else:
                print("NO")
                ans=1
                break
        else:
            flag=0
    if ans==0:
        print("YES")
