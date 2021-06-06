#######puzzleVerma#######


import sys
import math
LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for i in range(IN()):
    n,k=LI()
    if k>((n-1)//2):
        print(-1)  
        continue
    else:
        dig=1
        las=n
        for i in range(n):
            if i%2==1 and k>0:
                print(las,end=" ")
                las-=1
                k-=1
            else:
                print(dig,end=" ")
                dig+=1
        print()