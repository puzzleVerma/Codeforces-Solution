#######puzzleVerma#######


import sys
import math
mod = 10**9+7


LI=lambda:[int(k) for k in input().split()]
input = lambda: sys.stdin.readline().rstrip()
IN=lambda:int(input())
S=lambda:input()


for t in range(IN()):
    n=IN()
    mat=[0 for i in range(n*n)]
    if n==2:
        print(-1)
    else:
            ins=n*n
            pos=0
            while ins:
                mat[pos%(n*n)]=n*n-ins+1
                pos+=2
                ins-=1
                if ((n%2==0) and (ins==(n*n)//2)):
                    pos+=1
            for i in range(n*n):
                print(mat[i],end=" ")
                if ((i+1)%n==0):
                    print()