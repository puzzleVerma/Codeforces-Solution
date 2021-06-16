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
    grid=[]
    for i in range(n):
        l=S()
        l=list(l)
        grid+=[l]
    grid1=[[0]*m for i in range(n)]
    grid2=[[0]*m for i in range(n)]
    c=["R","W"]
    if m%2==1:
        i=0
        j=0
        ind=0

        while i<n:
            while j<m:
                grid1[i][j]=c[ind]
                ind=1-ind
                j+=1
            i+=1
            j=0
    
        i=0
        j=0
        ind=1

        while i<n:
            while j<m:
                grid2[i][j]=c[ind]
                ind=1-ind
                j+=1
            i+=1
            j=0
    else:
        i=0
        j=0
        st=0
        while i<n:
            ind=st
            while j<m:
                grid1[i][j]=c[ind]
                # print(c[ind])
                ind=1-ind
                j+=1
            i+=1
            j=0
            st=1-st

        i=0
        j=0
        st=1
        while i<n:
            ind=st
            while j<m:
                grid2[i][j]=c[ind]
                ind=1-ind
                j+=1
            i+=1
            j=0
            st=1-st

    flag=0
    ans=0
    for i in range(n):
        for j in range(m):
            if ((grid[i][j]==".") or (grid[i][j]==grid1[i][j])):
                pass
            else:
                flag=1
                break
        if flag==1:
            break
    else:
        ans=grid1

    flag=0
    for i in range(n):
        for j in range(m):
            if ((grid[i][j]==".") or (grid[i][j]==grid2[i][j])):
                pass
            else:
                flag=1
                break
        if flag==1:
            break
    else:
        ans=grid2

    if ans==0:
        print("NO")
    else:
        print("YES")
        for ele in ans:
            print(''.join([it for it in ele]))
