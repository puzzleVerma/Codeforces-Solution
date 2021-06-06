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
    n,m=LI()
    s=S()
    ans=list(s)
    ind=[]
    z=[]
    for i in r(n):
        if s[i]=="1":
            ind+=[i]
    # curr=ind[0]-1
    # mm=m
    # while mm:
    #     if curr>=0:
    #         ans[curr]="1"
    #     else:
    #         break
    #     curr-=1
    #     mm-=1
    # curr=ind[-1]+1
    # mm=m
    # while mm:
    #     if curr<n:
    #         ans[curr]="1"
    #     else:
    #         break
    #     curr+=1
    #     mm-=1

    for ele in ind[:]:
        for j in r(1,m+1):
            if ele-j>=0:
                ans[ele-j]="1"
            if ele+j<n:
                ans[ele+j]="1"
            if (ele-j<0 and ele+j>=n):
                break
    for i in r(1,len(ind)):
        dif=ind[i]-ind[i-1]-1
        if dif<(2*m):
            if dif%2:
                ans[ind[i]-(dif+1)//2]="0"

    print(''.join([ele for ele in ans]))