#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


n=IN()
dia=LI()
flag=1

board=[[0 for i in range(j+1)]for j in range(n)]

for i in range(n):
    board[i][i]=dia[i]

for i in range(1,dia[0]):
    board[i][0]=dia[0]

for i in range(1,dia[-1]):
    board[-1][n-i-1]=dia[-1]

for i in range(1,n-1):
    if flag==0:
        break
    check=dia[i]-1
    cr=i
    cc=i
    while check:
        if (cc>=0 and cr<n and (board[cr][cc-1]==0)):
            board[cr][cc-1]=dia[i]
            cc-=1
        elif (cc>=0 and cr<n and (board[cr+1][cc]==0)):
            board[cr+1][cc]=dia[i]
            cr+=1
        else:
            flag=0
            break
        check-=1

if flag==0:
    print(-1)
else:
    for ele in board:
        for it in ele:
            print(it,end=" ")
        print()
